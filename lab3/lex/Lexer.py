import ply.lex as lexer


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
        'add': 'ADD',
        'sub': 'SUB',
        'first': 'FIRST',
        'second': 'SECOND',
        'smaller': 'SMALLER',
        'larger': 'LARGER',
        'or': 'OR',
        'not': 'NOT',
        'and': 'AND',
        'begin': 'BEGIN',
        'end': 'END',
        'do': 'DO',
        'while': 'WHILE',
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
        'INTTYP', 'SHORTTYP', 'STRTYP',
        'OPBR', 'CLBR', 'SQOPBR', 'SQCLBR', 'CUOPBR', 'CUCLBR',
        'ENDSTR',
        'NEWLINE', 'COMMA', 'VECTOROF'
    ]

    tokens = types + list(reserved.values())

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


    def t_STRTYP(self, t):
        r'[a-zA-Z][a-zA-Z0-9]*'
        t.type = self.reserved.get(t.value, 'STRTYP')
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

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count('\n')
        return t

    def t_error(self, t):
        print(f"Invalid character {t.value[0]}")
        t.lexer.skip(1)
        return t

    if __name__ == '__main__':
        f = open('check.txt')
        data = f.read().lower()

