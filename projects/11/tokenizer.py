from enum import Enum

keyword = {'class', 'constructor', 'function', 'method', 'field',
           'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false',
           'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return'}
symbol = {'{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '>', '<', '=', '~'}


class Token(Enum):
    keyword = 0
    symbol = 1
    identifier = 2
    int_const = 3
    string_const = 4


class Comment(Enum):
    line = 0
    partial = 1
    newline = 2
    space = 3


def is_int(s):
    """ Wrapper for checking whether a string is an integer"""
    try:
        int(s)
        return True
    except ValueError:
        return False


def read_file(file_path):
    """ Reads a plaintext file and returns the data"""
    try:
        with open(file_path) as file:
            data = file.read()
    except FileNotFoundError:
        print("Can't find the file! Returning empty data")
        data = ''
    return data


class Tokenizer:

    def __init__(self, file_path, verbose=False):
        self.data = read_file(file_path)
        self.char_idx = 0
        self.cur_token = None
        self.verbose = verbose

    @property
    def has_more_tokens(self):
        return self.char_idx < len(self.data) - 1

    @property
    def cur_token_type(self):
        return self.get_token_type(self.cur_token)

    @staticmethod
    def get_token_type(token):
        """ Gets the token type of the current token """
        if token in keyword:
            return Token.keyword
        elif token in symbol:
            return Token.symbol
        elif token[0] == '"':
            return Token.string_const
        elif is_int(token):
            return Token.int_const
        else:
            return Token.identifier

    def write_token(self):
        """ Write the XML for the token if a basic lexical element"""
        if self.cur_token_type == Token.keyword:
            return '<keyword> {} </keyword>'.format(self.cur_token)
        elif self.cur_token_type == Token.symbol:
            if self.cur_token == '>':
                return '<symbol> &gt; </symbol>'
            elif self.cur_token == '<':
                return '<symbol> &lt; </symbol>'
            elif self.cur_token == '"':
                return '<symbol> &quot; </symbol>'
            elif self.cur_token == '&':
                return '<symbol> &amp; </symbol>'
            else:
                return '<symbol> {} </symbol>'.format(self.cur_token)
        elif self.cur_token_type == Token.identifier:
            return '<identifier> {} </identifier>'.format(self.cur_token)
        elif self.cur_token_type == Token.string_const:
            return '<stringConstant> {} </stringConstant>'.format(self.cur_token[1:-1])
        elif self.cur_token_type == Token.int_const:
            return '<integerConstant> {} </integerConstant>'.format(self.cur_token)

    def advance(self):
        while self._is_comment():
            cmt = self._is_comment()
            self._advance_through_comment(cmt)
        if self.has_more_tokens:
            self.cur_token = self._eat()
            self.char_idx += 1
        else:
            self.cur_token = None
        if self.verbose:
            print(self.cur_token)

    def _eat(self):
        """ Eat char until a token, or the EOF"""
        if self.data[self.char_idx] in symbol:
            return self.data[self.char_idx]
        if self.data[self.char_idx] == '"':
            temp_idx = self.char_idx
            while temp_idx < len(self.data) - 1:
                temp_idx += 1
                if self.data[temp_idx] == '"':
                    token = self.data[self.char_idx:temp_idx+1]
                    self.char_idx = temp_idx
                    return token

        temp_idx = self.char_idx
        while temp_idx < len(self.data) - 1:
            temp_idx += 1
            if self.data[temp_idx] in (' ', '\n'):
                token = self.data[self.char_idx:temp_idx]
                self.char_idx = temp_idx
                return token
            elif self.data[temp_idx] in symbol:
                token = self.data[self.char_idx:temp_idx]
                self.char_idx = temp_idx-1
                return token

    def _is_comment(self):
        """ Checks whether the current place in text is a comment, and whether a full line or partial"""
        if self.char_idx <= len(self.data) - 2 and self.data[self.char_idx:self.char_idx+2] == '//':
            return Comment.line
        elif self.char_idx <= len(self.data) - 3 and self.data[self.char_idx:self.char_idx+3] == '/**':
            return Comment.partial
        elif self.data[self.char_idx] == '\n':
            return Comment.newline
        elif self.data[self.char_idx] == ' ' or self.data[self.char_idx] == '\t':
            return Comment.space
        else:
            return False

    def _advance_through_comment(self, cmt):
        """ Increment char_idx until end of line, or until comment is done"""
        if cmt == Comment.line:
            while self.has_more_tokens and self.data[self.char_idx] != '\n':
                self.char_idx += 1
            self.char_idx += 1
        elif cmt == Comment.partial:
            while self.has_more_tokens and self.data[self.char_idx:self.char_idx+2] != '*/':
                self.char_idx += 1
            self.char_idx += 2
        elif cmt == Comment.newline or cmt == Comment.space:
            self.char_idx += 1
        else:
            raise ValueError('Comment erroneously identified!')


if __name__ == '__main__':
    t = Tokenizer('ArrayTest/Main.jack', verbose=True)
    while t.has_more_tokens:
        t.advance()
