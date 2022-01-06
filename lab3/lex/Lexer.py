import ply.lex as lexer
import re


class LexerClass:
    def __init__(self):
        self.lexer = lexer.lex(module=self)

    reserved = {
        'true': 'TRUE',
        'false': 'FALSE',
        'bool': 'BOOL',
        'undefined': 'UNDEFINED',
        'int': 'INT',
        'short': 'SHORT',
        'set': 'SET',
        'sizeof': 'SIZEOF',
        'first': 'FIRST',
        'second': 'SECOND',
        'add': 'ADD',
        'sub': 'SUB',
        'smaller': 'SMALLER',
        'larger': 'LARGER',
        'or': 'OR',
        'not': 'NOT',
        'and': 'AND',
        'begin': 'BEGIN',
        'end': 'END',
        'do': 'DO',
        'while': 'WHILE', #(a second smaller b) b < a
        'if': 'IF',
        'then': 'THEN',
        'else': 'ELSE',
        'move': 'MOVE',
        'right': 'RIGHT',
        'left': 'LEFT',
        'function': 'FUNCTION',
        'return': 'RETURN',
        'lms': 'LMS'
    }

    types = [
        'INTTYP', 'SHORTTYP', 'VARIABLE',
        'OPBR', 'CLBR', 'SQOPBR', 'SQCLBR', 'CUOPBR', 'CUCLBR',
        'ENDSTR', 'EQUAL',
        'NEWLINE', 'COMMA', 'VECTOROF'
    ]

    tokens = types + list(reserved.values())

    t_ignore = ' \t'

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def t_INTTYP(self, t):
        r'\-?[0-9]+'
        t.value = int(t.value)
        return t

    def t_SHORTTYP(self, t):
        r's\-?[0-9]+'
        t.value = int(t.value[1:])
        return t

    def t_VECTOROF(self, t):
        r'vector[ ]+of'
        return t

    def t_VARIABLE(self, t):
        r'[a-zA-Z][a-zA-Z0-9]*'
        t.type = self.reserved.get(t.value, 'VARIABLE')
        return t

    def t_OPBR(self, t):
        r'\('
        return t

    def t_CLBR(self, t):
        r'\)'
        return t

    def t_SQOPBR(self, t):
        r'\['
        return t

    def t_SQCLBR(self, t):
        r'\]'
        return t

    def t_CUOPBR(self, t):
        r'\{'
        return t

    def t_CUCLBR(self, t):
        r'\}'
        return t

    def t_COMMA(self, t):
        r'\,'
        return t

    def t_ENDSTR(self, t):
        r'\;'
        return t

    def t_EQUAL(self, t):
        r'\=\='
        return t

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count('\n')

    def t_error(self, t):
        print(f"Invalid character {t.value[0]}")
        t.lexer.skip(1)
        t.value = t.value[0]
        return t


if __name__ == '__main__':
    f = open('check.txt', 'r')
    lex = LexerClass()
    data = f.read()
    lex.input(data)
    while True:
        tok = lex.token()
        if not tok:
            break
        print(tok)
