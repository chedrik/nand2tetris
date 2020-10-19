from tokenizer import *


class CompilerError(Exception):
    def __init__(self, expect, found):
        self.expect = expect
        self.found = found

    def __str__(self):
        return ('Expected token of type {} and found {} of type {}'.format(self.expect, self.found,
                                                                           Tokenizer.get_token_type(self.found)))


class Parser:

    def __init__(self, file, verbose=False):
        self.indent_lvl = 0
        self.t = Tokenizer(file)
        self.out_fp = file.split('.')[0] + '.xml'
        self.out_str = []
        self.comp_class()
        if verbose:
            for l in self.out_str:
                print(l)

    @property
    def indent(self):
        return ' ' * self.indent_lvl

    def write(self):
        with open(self.out_fp, "w") as file:
            for line in self.out_str:
                file.write(line + '\n')
        return

    def comp_class(self):
        self.t.advance()
        if self.t.cur_token != 'class':
            raise CompilerError('class', self.t.cur_token)
        self.out_str.append('<class>')
        self.indent_lvl += 2
        self.out_str.append(self.indent + '<keyword> class </keyword>')
        self.t.advance()
        if self.t.cur_token_type != Token.identifier:
            raise CompilerError('identifier', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()
        if self.t.cur_token != '{':
            raise CompilerError('{', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()
        while self.t.cur_token not in ('constructor', 'function', 'method', '}'):
            if self.t.cur_token in ('static', 'field'):
                self.comp_class_var_dec()
            else:
                self.t.advance()

        # TODO: Iterate
        while self.t.cur_token in ('constructor', 'function', 'method'):
            self.comp_sub_dec()
            self.t.advance()

        # self.t.advance()
        if self.t.cur_token != '}':
            raise CompilerError('}', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.out_str.append('</class>')

    def comp_class_var_dec(self):
        self.out_str.append(self.indent + '<classVarDec>')
        self.indent_lvl += 2
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()  # Variable type (static/field)
        if self.t.cur_token_type not in (Token.identifier, Token.keyword):
            raise CompilerError('identifier or keyword', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()  # Variable type
        if self.t.cur_token_type not in (Token.identifier, Token.keyword):
            raise CompilerError('identifier', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()  # Variable name, more types
        while self.t.cur_token != ';':
            if self.t.cur_token == ',':
                self.out_str.append(self.indent + self.t.write_token())
            elif self.t.cur_token_type == Token.identifier:
                self.out_str.append(self.indent + self.t.write_token())
            else:
                raise CompilerError('identifier, ","', self.t.cur_token)
            self.t.advance()
        self.out_str.append(self.indent + self.t.write_token())

        self.indent_lvl -= 2
        self.out_str.append(self.indent + '</classVarDec>')

    def comp_sub_dec(self):
        if self.t.cur_token == '}':  # Handle no-body case
            return
        self.out_str.append(self.indent + '<subroutineDec>')
        self.indent_lvl += 2
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()  # Return type
        if self.t.cur_token_type not in (Token.identifier, Token.keyword):
            raise CompilerError('identifier or keyword', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()  # Subroutine name
        if self.t.cur_token_type != Token.identifier:
            raise CompilerError('identifier', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()  # Parameter list
        if self.t.cur_token != '(':
            raise CompilerError('(', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())
        self.comp_param_list()

        if self.t.cur_token != ')':
            raise CompilerError(')', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.comp_sub_body()

        self.indent_lvl -= 2
        self.out_str.append(self.indent + '</subroutineDec>')

    def comp_param_list(self):
        self.out_str.append(self.indent + '<parameterList>')
        self.indent_lvl += 2

        self.t.advance()  # Var type
        while self.t.cur_token != ')':
            if self.t.cur_token_type not in (Token.identifier, Token.keyword):
                raise CompilerError('identifier or keyword', self.t.cur_token)
            self.out_str.append(self.indent + self.t.write_token())

            self.t.advance()  # Var name
            if self.t.cur_token_type != Token.identifier:
                raise CompilerError('identifier', self.t.cur_token)
            self.out_str.append(self.indent + self.t.write_token())

            self.t.advance()
            if self.t.cur_token == ',':
                self.out_str.append(self.indent + self.t.write_token())
                self.t.advance()

        self.indent_lvl -= 2
        self.out_str.append(self.indent + '</parameterList>')

    def comp_sub_body(self):
        self.out_str.append(self.indent + '<subroutineBody>')
        self.indent_lvl += 2
        self.t.advance()
        if self.t.cur_token != '{':
            raise CompilerError('{', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()  # Var Dec
        while self.t.cur_token not in ('let', 'if', 'while', 'do', 'return'):
            self.comp_var_dec()

        self.comp_statements()

        if self.t.cur_token != '}':
            raise CompilerError('}', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.indent_lvl -= 2
        self.out_str.append(self.indent + '</subroutineBody>')

    def comp_var_dec(self):
        self.out_str.append(self.indent + '<varDec>')
        self.indent_lvl += 2

        if self.t.cur_token != 'var':
            raise CompilerError('var', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()  # Variable type
        if self.t.cur_token_type not in (Token.identifier, Token.keyword):
            raise CompilerError('identifier', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()  # Variable name, more types
        while self.t.cur_token != ';':
            if self.t.cur_token == ',':
                self.out_str.append(self.indent + self.t.write_token())
            elif self.t.cur_token_type == Token.identifier:
                self.out_str.append(self.indent + self.t.write_token())
            else:
                raise CompilerError('identifier, ","', self.t.cur_token)
            self.t.advance()
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()

        self.indent_lvl -= 2
        self.out_str.append(self.indent + '</varDec>')

    def comp_statements(self):
        self.out_str.append(self.indent + '<statements>')
        self.indent_lvl += 2

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
                self.comp_return()
                self.t.advance()
            else:
                raise CompilerError('let,if,while,do,return', self.t.cur_token)
            # self.t.advance()

        self.indent_lvl -= 2
        self.out_str.append(self.indent + '</statements>')

    def comp_let(self):
        self.out_str.append(self.indent + '<letStatement>')
        self.indent_lvl += 2

        if self.t.cur_token != 'let':
            raise CompilerError('let', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()  # varName
        if self.t.cur_token_type != Token.identifier:
            raise CompilerError('identifier', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()  # [Expression] = expression, or = expression
        if self.t.cur_token == '=':
            self.out_str.append(self.indent + self.t.write_token())
            self.t.advance()
            self.comp_expression()
        elif self.t.cur_token == '[':
            self.out_str.append(self.indent + self.t.write_token())
            self.t.advance()
            self.comp_expression()
            if self.t.cur_token != ']':
                raise CompilerError(']', self.t.cur_token)
            self.out_str.append(self.indent + self.t.write_token())
            self.t.advance()
            if self.t.cur_token != '=':
                raise CompilerError('=', self.t.cur_token)
            self.out_str.append(self.indent + self.t.write_token())
            self.t.advance()
            self.comp_expression()
        else:
            raise CompilerError('=, [', self.t.cur_token)

        if self.t.cur_token != ';':
            raise CompilerError(';', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.indent_lvl -= 2
        self.out_str.append(self.indent + '</letStatement>')

    def comp_if(self):
        self.out_str.append(self.indent + '<ifStatement>')
        self.indent_lvl += 2

        if self.t.cur_token != 'if':
            raise CompilerError('if', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()
        if self.t.cur_token != '(':
            raise CompilerError('(', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()
        self.comp_expression()

        if self.t.cur_token != ')':
            raise CompilerError(')', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()
        if self.t.cur_token != '{':
            raise CompilerError('{', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()
        self.comp_statements()

        if self.t.cur_token != '}':
            raise CompilerError('}', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()
        if self.t.cur_token == 'else':
            self.out_str.append(self.indent + self.t.write_token())
            self.t.advance()
            if self.t.cur_token != '{':
                raise CompilerError('{', self.t.cur_token)
            self.out_str.append(self.indent + self.t.write_token())

            self.t.advance()
            self.comp_statements()

            if self.t.cur_token != '}':
                raise CompilerError('}', self.t.cur_token)
            self.out_str.append(self.indent + self.t.write_token())
            self.t.advance()

        self.indent_lvl -= 2
        self.out_str.append(self.indent + '</ifStatement>')

    def comp_while(self):
        self.out_str.append(self.indent + '<whileStatement>')
        self.indent_lvl += 2

        if self.t.cur_token != 'while':
            raise CompilerError('while', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()
        if self.t.cur_token != '(':
            raise CompilerError('(', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()
        self.comp_expression()
        if self.t.cur_token != ')':
            raise CompilerError(')', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()
        if self.t.cur_token != '{':
            raise CompilerError('{', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()
        self.comp_statements()

        if self.t.cur_token != '}':
            raise CompilerError('}', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.indent_lvl -= 2
        self.out_str.append(self.indent + '</whileStatement>')

    def comp_do(self):
        self.out_str.append(self.indent + '<doStatement>')
        self.indent_lvl += 2

        if self.t.cur_token != 'do':
            raise CompilerError('do', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()
        if self.t.cur_token_type != Token.identifier:
            raise CompilerError('identifier', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()
        if self.t.cur_token == '.':
            self.out_str.append(self.indent + self.t.write_token())

            self.t.advance()
            if self.t.cur_token_type != Token.identifier:
                raise CompilerError('identifier', self.t.cur_token)
            self.out_str.append(self.indent + self.t.write_token())

            self.t.advance()
            self.comp_expr_list()

        elif self.t.cur_token == '(':
            self.comp_expr_list()
        else:
            self.out_str.append(self.indent + '<identifier> {} </identifier>'.format(cur_token))

        if self.t.cur_token != ';':
            raise CompilerError(';', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.indent_lvl -= 2
        self.out_str.append(self.indent + '</doStatement>')

    def comp_return(self):
        self.out_str.append(self.indent + '<returnStatement>')
        self.indent_lvl += 2

        if self.t.cur_token != 'return':
            raise CompilerError('return', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.t.advance()

        if self.t.cur_token != ';':
            self.comp_expression()

        if self.t.cur_token != ';':
            raise CompilerError(';', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.indent_lvl -= 2
        self.out_str.append(self.indent + '</returnStatement>')

    def comp_expression(self):
        self.out_str.append(self.indent + '<expression>')
        self.indent_lvl += 2

        self.comp_term()  # term
        while self.t.cur_token in ('+', '-', '*', '/', '&', '|', '>', '<', '='):  # (op term)*
            self.out_str.append(self.indent + self.t.write_token())
            self.t.advance()
            self.comp_term()

        self.indent_lvl -= 2
        self.out_str.append(self.indent + '</expression>')

    def comp_term(self):
        self.out_str.append(self.indent + '<term>')
        self.indent_lvl += 2

        if self.t.cur_token_type in (Token.int_const, Token.string_const) or \
                self.t.cur_token in ('true', 'false', 'null', 'this'):
            self.out_str.append(self.indent + self.t.write_token())
            self.t.advance()
        elif self.t.cur_token == '(':
            self.out_str.append(self.indent + self.t.write_token())

            self.t.advance()
            self.comp_expression()

            if self.t.cur_token != ')':
                raise CompilerError(')', self.t.cur_token)
            self.out_str.append(self.indent + self.t.write_token())

            self.t.advance()
        elif self.t.cur_token in ('-', '~'):
            self.out_str.append(self.indent + self.t.write_token())
            self.t.advance()
            self.comp_term()
        else:
            cur_token = self.t.cur_token
            self.t.advance()
            if self.t.cur_token == '[':  # [expression]
                self.out_str.append(self.indent + '<identifier> {} </identifier>'.format(cur_token))
                self.out_str.append(self.indent + self.t.write_token())

                self.t.advance()
                self.comp_expression()

                if self.t.cur_token != ']':
                    raise CompilerError(']', self.t.cur_token)
                self.out_str.append(self.indent + self.t.write_token())
                self.t.advance()

            elif self.t.cur_token == '.':
                self.out_str.append(self.indent + '<identifier> {} </identifier>'.format(cur_token))
                self.out_str.append(self.indent + self.t.write_token())

                self.t.advance()
                if self.t.cur_token_type != Token.identifier:
                    raise CompilerError('identifier', self.t.cur_token)
                self.out_str.append(self.indent + self.t.write_token())

                self.t.advance()
                self.comp_expr_list()

            elif self.t.cur_token == '(':
                self.comp_expr_list()
            else:
                self.out_str.append(self.indent + '<identifier> {} </identifier>'.format(cur_token))

        self.indent_lvl -= 2
        self.out_str.append(self.indent + '</term>')

    def comp_expr_list(self):
        if self.t.cur_token != '(':
            raise CompilerError('(', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())

        self.out_str.append(self.indent + '<expressionList>')
        self.indent_lvl += 2

        self.t.advance()
        if self.t.cur_token == ')':
            pass
        else:
            while self.t.cur_token_type in (Token.identifier, Token.int_const, Token.string_const) or \
                    self.t.cur_token in ('(',',', 'true', 'false', 'null', 'this'):
                if self.t.cur_token == ',':
                    self.out_str.append(self.indent + self.t.write_token())
                    self.t.advance()
                else:
                    self.comp_expression()

        self.indent_lvl -= 2
        self.out_str.append(self.indent + '</expressionList>')
        if self.t.cur_token != ')':
            raise CompilerError(')', self.t.cur_token)
        self.out_str.append(self.indent + self.t.write_token())
        self.t.advance()


if __name__ == '__main__':
    p = Parser('Square/Main.jack')

    # p = Parser('ArrayTest/Main.jack')

    # while t.has_more_tokens:
    #     t.advance()
