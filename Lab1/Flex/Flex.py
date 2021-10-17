import ply.lex as lex
from ply.lex import Lexer

def InTheList(strList, arg):
    for i in strList:
        if i == arg:
            return True
    return False

class LexAnalyser:
    tokens = [
        'AIMNAME',
        'COLON',
        'SPACE'
    ]
    token_list = []
    dict = {}
    set = set()
    def t_COLON(self, t):
        r":"
        return t

    def t_AIMNAME(self, t):
        r"[A-Za-z][A-Za-z0-9\._]*"
        return t

    def t_error(self, t):
        print("Illegal Token")
        return False

    def __init__(self):
        self.lexer: Lexer = lex.lex(module=self)

    def t_SPACE(self, t):
        r"[ \t]+"

    def gen_tokens(self, inp):
        self.lexer.input(inp)
        while True:
            try:
                tok = self.lexer.token()
            except lex.LexError:
                self.clear()
                return False
            if not tok:
                break
            self.token_list.append(tok)
        return self.token_list

    def clear(self):
        self.token_list.clear()

    def checkString(self):
        if len(self.token_list) < 2:
            return False
        token1 = self.token_list.pop(0)
        token2 = self.token_list.pop(0)
        if token1.type != 'AIMNAME' or token2.type != 'COLON':
            return False
        self.set.add(token1.value)
        list1 = []
        local_dict = {}
        list1.append(token1.value)
        for token in self.token_list:
            if token.type != 'AIMNAME':
                return False
            if InTheList(list1, token.value):
                return False
            list1.append(token.value)
            if local_dict.get(token.value) == None:
                local_dict[token.value] = 1
            else:
                local_dict[token.value] += 1
        for k in local_dict:
            if self.dict.get(k) == None:
                self.dict[k] = 1
            else:
                self.dict[k] += 1
        self.set.add(token1.value)
        return True

    def analyse(self, str):
        self.gen_tokens(str)
        res = self.checkString()
        self.clear()
        return res
