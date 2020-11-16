from tokenizer import *
from writer import *
from symbol import *


class CompilerError(Exception):
    def __init__(self, expect, found):
        self.expect = expect
        self.found = found

    def __str__(self):
        return ('Expected token of type {} and found {} of type {}'.format(self.expect, self.found,
                                                                           Tokenizer.get_token_type(self.found)))


class Compiler:

    def __init__(self, file, verbose=False):
        self.indent_lvl = 0
        self.t = Tokenizer(file)
        self.w = Writer(file)
        self.sym_table = SymbolTable()
        self.while_count = 0
        self.if_count = 0
        self.comp_class()
        if verbose:
            for l in self.w.out_str:
                print(l)
        self.w.write_to_file()

    def comp_class(self):
        self.t.advance()
        if self.t.cur_token != 'class':
            raise CompilerError('class', self.t.cur_token)

        self.t.advance()
        if self.t.cur_token_type != Token.identifier:
            raise CompilerError('identifier', self.t.cur_token)

        self.t.advance()
        if self.t.cur_token != '{':
            raise CompilerError('{', self.t.cur_token)

        self.t.advance()
        while self.t.cur_token not in ('constructor', 'function', 'method', '}'):
            if self.t.cur_token in ('static', 'field'):
                self.comp_class_var_dec()
            else:
                self.t.advance()

        while self.t.cur_token in ('constructor', 'function', 'method'):
            self.comp_sub_dec()
            self.t.advance()

    def comp_class_var_dec(self):
        if self.t.cur_token_type not in (Token.identifier, Token.keyword):  # Variable type (static/field)
            raise CompilerError('identifier or keyword', self.t.cur_token)
        scope = Kind.STATIC if self.t.cur_token == 'static' else Kind.FIELD

        self.t.advance()  # Variable type
        if self.t.cur_token_type not in (Token.identifier, Token.keyword):
            raise CompilerError('identifier', self.t.cur_token)
        var_type = self.t.cur_token

        self.t.advance()  # Variable name, more types
        while self.t.cur_token != ';':
            if self.t.cur_token == ',':
                pass
            elif self.t.cur_token_type == Token.identifier:
                self.sym_table.define(self.t.cur_token, var_type, scope)
            else:
                raise CompilerError('identifier, ","', self.t.cur_token)
            self.t.advance()

    def comp_sub_dec(self):
        if self.t.cur_token == '}':  # Handle no-body case
            return

        self.sym_table.start_subroutine()
        self.if_count = 0  # Reset counts to match provided compiler better.
        self.while_count = 0

        fcn_type = self.t.cur_token

        self.t.advance()  # Return type
        if self.t.cur_token_type not in (Token.identifier, Token.keyword):
            raise CompilerError('identifier or keyword', self.t.cur_token)

        return_type = self.t.cur_token

        self.t.advance()  # Subroutine name
        if self.t.cur_token_type != Token.identifier:
            raise CompilerError('identifier', self.t.cur_token)
        fcn_name = self.t.cur_token

        self.t.advance()  # Parameter list
        if self.t.cur_token != '(':
            raise CompilerError('(', self.t.cur_token)
        num_param = self.comp_param_list(fcn_type)

        if self.t.cur_token != ')':
            raise CompilerError(')', self.t.cur_token)

        self.comp_sub_body(return_type, fcn_name, fcn_type)

    def comp_param_list(self, fcn_type):
        num_param = 0

        if fcn_type == 'method':
            self.sym_table.define('this', self.w.out_fp.split('/')[-1].split('.')[0], Kind.ARG)

        self.t.advance()  # Var type
        while self.t.cur_token != ')':
            num_param += 1
            if self.t.cur_token_type not in (Token.identifier, Token.keyword):
                raise CompilerError('identifier or keyword', self.t.cur_token)
            var_type = self.t.cur_token

            self.t.advance()  # Var name
            if self.t.cur_token_type != Token.identifier:
                raise CompilerError('identifier', self.t.cur_token)
            self.sym_table.define(self.t.cur_token, var_type, Kind.ARG)

            self.t.advance()
            if self.t.cur_token == ',':
                self.t.advance()

        return num_param

    def comp_sub_body(self, return_type, fcn_name, fcn_type):
        self.t.advance()
        if self.t.cur_token != '{':
            raise CompilerError('{', self.t.cur_token)

        self.t.advance()  # Var Dec
        vars = 0
        while self.t.cur_token not in ('let', 'if', 'while', 'do', 'return'):
            new_vars = self.comp_var_dec()
            vars += new_vars

        self.w.write_function(fcn_name, vars)
        if fcn_type == 'constructor':
            self.w.write_push('constant', self.sym_table.get_var_count(Kind.FIELD))
            self.w.write_call('Memory.alloc', '1')
            self.w.write_pop('pointer', '0')
        elif fcn_type == 'method':
            self.w.write_push('argument', '0')
            # self.w.write_push('argument', self.sym_table.get_var_count(Kind.ARG))

            self.w.write_pop('pointer', '0')

        self.comp_statements(return_type)

        if self.t.cur_token != '}':
            raise CompilerError('}', self.t.cur_token)

    def comp_var_dec(self):
        cnt = 0
        if self.t.cur_token != 'var':
            raise CompilerError('var', self.t.cur_token)

        self.t.advance()  # Variable type
        if self.t.cur_token_type not in (Token.identifier, Token.keyword):
            raise CompilerError('identifier', self.t.cur_token)
        var_type = self.t.cur_token

        self.t.advance()  # Variable name, more vars of same type
        while self.t.cur_token != ';':
            if self.t.cur_token == ',':
                pass
            elif self.t.cur_token_type == Token.identifier:
                self.sym_table.define(self.t.cur_token, var_type, Kind.VAR)
                cnt += 1
            else:
                raise CompilerError('identifier, ","', self.t.cur_token)
            self.t.advance()

        self.t.advance()
        return cnt

    def comp_statements(self, return_type=None):
        while self.t.cur_token in ('let', 'if', 'while', 'do', 'return'):
            if self.t.cur_token == 'let':
                self.comp_let()
                self.t.advance()
            elif self.t.cur_token == 'if':
                self.comp_if()
            elif self.t.cur_token == 'while':
                self.comp_while()
                self.t.advance()
            elif self.t.cur_token == 'do':
                self.comp_do()
                self.t.advance()
            elif self.t.cur_token == 'return':
                if return_type == 'void':
                    self.w.write_push('constant', 0)
                self.comp_return()
                self.t.advance()
            else:
                raise CompilerError('let,if,while,do,return', self.t.cur_token)

    def comp_let(self):
        if self.t.cur_token != 'let':
            raise CompilerError('let', self.t.cur_token)

        self.t.advance()  # varName
        if self.t.cur_token_type != Token.identifier:
            raise CompilerError('identifier', self.t.cur_token)

        result = self.t.cur_token

        self.t.advance()  # [Expression] = expression, or = expression
        _pass = False
        if self.t.cur_token == '=':
            self.t.advance()
            self.comp_expression()
        elif self.t.cur_token == '[':
            _pass = True
            self.t.advance()
            self.comp_expression()
            self.w.write_push(self.sym_table.get_vm_seg(result),
                              self.sym_table.get_var_index(result))
            self.w.write_math('+')
            if self.t.cur_token != ']':
                raise CompilerError(']', self.t.cur_token)
            self.t.advance()

            if self.t.cur_token != '=':
                raise CompilerError('=', self.t.cur_token)
            self.t.advance()
            self.comp_expression()
            self.w.write_pop('temp', '0')
            self.w.write_pop('pointer', '1')
            self.w.write_push('temp', '0')
            self.w.write_pop('that', '0')
        else:
            raise CompilerError('=, [', self.t.cur_token)
        if not _pass:
            self.w.write_pop(self.sym_table.get_vm_seg(result), self.sym_table.get_var_index(result))
        if self.t.cur_token != ';':
            raise CompilerError(';', self.t.cur_token)

    def comp_if(self):
        local_if = self.if_count
        self.if_count += 1
        if self.t.cur_token != 'if':
            raise CompilerError('if', self.t.cur_token)

        self.t.advance()
        if self.t.cur_token != '(':
            raise CompilerError('(', self.t.cur_token)

        self.t.advance()
        self.comp_expression()

        if self.t.cur_token != ')':
            raise CompilerError(')', self.t.cur_token)
        # self.w.write_math('~')  # Not

        self.w.write_if("IF_TRUE{}".format(local_if))
        self.w.write_goto("IF_FALSE{}".format(local_if))
        self.w.write_label("IF_TRUE{}".format(local_if))

        self.t.advance()
        if self.t.cur_token != '{':
            raise CompilerError('{', self.t.cur_token)

        self.t.advance()
        self.comp_statements()

        if self.t.cur_token != '}':
            raise CompilerError('}', self.t.cur_token)
        self.w.write_goto("IF_END{}".format(local_if))

        self.t.advance()
        self.w.write_label("IF_FALSE{}".format(local_if))

        if self.t.cur_token == 'else':
            self.t.advance()
            if self.t.cur_token != '{':
                raise CompilerError('{', self.t.cur_token)
            # self.w.write_label("IF_FALSE{}".format(local_if))

            self.t.advance()
            self.comp_statements()

            if self.t.cur_token != '}':
                raise CompilerError('}', self.t.cur_token)
            self.t.advance()
        self.w.write_label("IF_END{}".format(local_if))

    def comp_while(self):
        local_while = self.while_count
        self.while_count += 1
        if self.t.cur_token != 'while':
            raise CompilerError('while', self.t.cur_token)
        self.w.write_label("WHILE_START{}".format(local_while))

        self.t.advance()
        if self.t.cur_token != '(':
            raise CompilerError('(', self.t.cur_token)

        self.t.advance()
        self.comp_expression()
        if self.t.cur_token != ')':
            raise CompilerError(')', self.t.cur_token)
        self.w.write_math('~')  # Not

        self.w.write_if("WHILE_END{}".format(local_while))

        self.t.advance()
        if self.t.cur_token != '{':
            raise CompilerError('{', self.t.cur_token)

        self.t.advance()
        self.comp_statements()

        if self.t.cur_token != '}':
            raise CompilerError('}', self.t.cur_token)

        self.w.write_goto("WHILE_START{}".format(local_while))
        self.w.write_label("WHILE_END{}".format(local_while))

    def comp_do(self):
        if self.t.cur_token != 'do':
            raise CompilerError('do', self.t.cur_token)

        self.t.advance()
        if self.t.cur_token_type != Token.identifier:
            raise CompilerError('identifier', self.t.cur_token)
        class_name = self.t.cur_token
        var_kind = self.sym_table.get_vm_seg(class_name)
        if var_kind:
            type, idx = self.sym_table.get_var(class_name)
            self.w.write_push(var_kind, idx)
        fcn_name = ''
        self.t.advance()
        if self.t.cur_token == '.':
            fcn_name += '.'
            self.t.advance()
            if self.t.cur_token_type != Token.identifier:
                raise CompilerError('identifier', self.t.cur_token)
            fcn_name += self.t.cur_token
            self.t.advance()
            num_param = self.comp_expr_list()
        elif self.t.cur_token == '(':
            num_param = self.comp_expr_list()
        else:
            raise ValueError('what do I do here')
        if var_kind:
            num_param += 1
            fcn_name = type + fcn_name
        else:
            fcn_name = class_name + fcn_name
        if fcn_name == class_name:  # same class method or fcn
            fcn_name = self.w.out_fp.split('/')[-1].split('.')[0] + '.' + fcn_name
            num_param += 1
            if num_param > 1:
                self.w.write_prev_push('pointer', '0', num_param)
            else:
                self.w.write_push('pointer', '0')

        self.w.write_call(fcn_name, num_param)
        self.w.write_pop('temp', 0)

        if self.t.cur_token != ';':
            raise CompilerError(';', self.t.cur_token)

    def comp_return(self):
        if self.t.cur_token != 'return':
            raise CompilerError('return', self.t.cur_token)

        self.t.advance()

        if self.t.cur_token != ';':
            self.comp_expression()
        self.w.write_return()

        if self.t.cur_token != ';':
            raise CompilerError(';', self.t.cur_token)

    def comp_expression(self):
        self.comp_term()  # term
        op_term = None
        while self.t.cur_token in ('+', '-', '*', '/', '&', '|', '>', '<', '=', '~'):  # (op term)*
            op_term = self.t.cur_token
            self.t.advance()
            self.comp_term()
        if op_term:
            if op_term == '*':
                self.w.write_call('Math.multiply', 2)
            elif op_term == '/':
                self.w.write_call('Math.divide', 2)
            else:
                self.w.write_math(op_term)

    def comp_term(self):
        if self.t.cur_token_type == Token.int_const:
            self.w.write_push('constant', self.t.cur_token)
            self.t.advance()
        elif self.t.cur_token_type == Token.string_const:
            self.w.write_push('constant', len(self.t.cur_token.strip('"')))
            self.w.write_call('String.new', 1)
            for c in self.t.cur_token.strip('"'):
                self.w.write_push('constant', ord(c))
                self.w.write_call('String.appendChar', 2)
            self.t.advance()
        elif self.t.cur_token == 'true':
            self.w.write_push('constant', '0')
            self.w.write_math('~')
            self.t.advance()
        elif self.t.cur_token == 'false':
            self.w.write_push('constant', '0')
            self.t.advance()
        elif self.t.cur_token == 'null':
            self.w.write_push('constant', '0')
            self.t.advance()
        elif self.t.cur_token == 'this':
            self.w.write_push('pointer', '0')
            self.t.advance()
        elif self.t.cur_token == '(':
            self.t.advance()
            self.comp_expression()
            if self.t.cur_token != ')':
                raise CompilerError(')', self.t.cur_token)
            self.t.advance()
        elif self.t.cur_token in ('-', '~'):
            token = self.t.cur_token
            self.t.advance()
            self.comp_term()
            self.w.write_math(token, neg=True)
        else:
            cur_token = self.t.cur_token
            self.t.advance()
            if self.t.cur_token == '[':  # [expression]
                self.t.advance()
                self.comp_expression()
                self.w.write_push(self.sym_table.get_vm_seg(cur_token),
                                  self.sym_table.get_var_index(cur_token))
                self.w.write_math('+')
                self.w.write_pop('pointer', '1')
                self.w.write_push('that', '0')
                self.t.advance()
            elif self.t.cur_token == '.':
                cur_token += '.'
                self.t.advance()
                if self.t.cur_token_type != Token.identifier:
                    raise CompilerError('identifier', self.t.cur_token)
                cur_token += self.t.cur_token
                self.t.advance()
                num_param = self.comp_expr_list()
                var = self.sym_table.get_var(cur_token.split('.')[0])
                if var:
                    self.w.write_push('this', var[1])
                    self.w.write_call(var[0] + '.' + cur_token.split('.')[1], num_param+1)
                else:
                    self.w.write_call(cur_token, num_param)
            elif self.t.cur_token == '(':
                self.comp_expr_list()
            else:
                self.w.write_push(self.sym_table.get_vm_seg(cur_token),
                                  self.sym_table.get_var_index(cur_token))

    def comp_expr_list(self):
        if self.t.cur_token != '(':
            raise CompilerError('(', self.t.cur_token)

        num_param = 0

        self.t.advance()
        if self.t.cur_token == ')':
            pass
        else:
            while self.t.cur_token_type in (Token.identifier, Token.int_const, Token.string_const) or \
                    self.t.cur_token in ('(', ',', 'true', 'false', 'null', 'this', '-', '~'):
                if self.t.cur_token == ',':
                    self.t.advance()
                else:
                    self.comp_expression()
                    num_param += 1

        if self.t.cur_token != ')':
            raise CompilerError(')', self.t.cur_token)
        self.t.advance()
        return num_param


if __name__ == '__main__':
    c = Compiler('Pong/PongGame.jack', verbose=True)
