from Node import Node


class NodeBuilder:
    def program(self, p):
        p[0] = Node('program', children=[p[1]], lineno=p.lineno(1))

    def statement_list(self, p):
        if len(p) == 3:
            p[0] = Node('statement list', children=[p[1], p[2]], lineno=p.lineno(1))
        else:
            p[0] = p[1]

    def single_statement(self, p):
        if p[1] != ';':
            p[0] = p[1]
        else:
            p[0] = Node('End of program', lineno=p.lineno(1))

    def declaration(self, p):
        p[0] = Node('declaration', children=[p[1], p[2]], lineno=p.lineno(1))

    def type(self, p):
        p[0] = Node('type', data=p[1], lineno=p.lineno(1))

    def var(self, p):
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = Node('var', children=[p[1], p[3]], lineno=p.lineno(1))

    def setting(self, p):
        p[0] = Node('assign', data=p[2], children=[p[1], p[3]], lineno=p.lineno(1))

    def expr(self, p):
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = Node('expression', children=[p[1], p[2], p[3]], lineno=p.lineno(1))

    def setting_arr(self, p):
        p[0] = Node('assign array', data=p[2], children=[p[1], p[3]], lineno=p.lineno(1))

    def type_arr(self, p):
        p[0] = p[1]

    def vectorof(self, p):
        p[0] = Node('Vector of', data=p[1], children=[p[2]], lineno=p.lineno(1))

    def setarr(self, p):
        if p[2] == ',':
            p[0] = Node('arr comma', children=[p[1], p[3]], lineno=p.lineno(1))
        else:
            p[0] = Node('arr count', children=[p[2]], lineno=p.lineno(1))

    def exprarr(self, p):
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = Node('expr comma', children=[p[1], p[3]], lineno=p.lineno(1))

    def const(self, p):
        p[0] = p[1]

    def variable(self, p):
        if len(p)== 2:
            p[0] = Node('variable', data=p[1], lineno=p.lineno(1))
        else:
            p[0] = Node('array variable', data= p[1], children=[p[2]], lineno=p.lineno(1))

    def index(self, p):
        if len(p) == 3:
            p[0] = Node('double index', children=[p[1], p[2]], lineno=p.lineno(1))
        else:
            p[0] = Node('squared bracket', data=p[2], lineno=p.lineno(1))

    def sizeof(self, p):
        p[0] = Node('size of ', data=p[1], children=[p[3]], lineno=p.lineno(1))

    def bool(self, p):
        p[0] = Node('bool', data=p[1], lineno=p.lineno(1))

    def digit(self, p):
        p[0] = Node('digit', data=p[1], lineno=p.lineno(1))

    def math_expr(self, p):
        if len(p) == 4:
            p[0] = Node('math expression', data=p[2], children=[p[1], p[3]], lineno=p.lineno(1))
        else:
            if p[2] != 'not':
                p[0] = Node('compare', data=f"{p[2]} {p[3]}", children=[p[1], p[4]], lineno=p.lineno(1))
            else:
                p[0] = Node('logic operator', data=f"{p[2]} {p[3]}", children=[p[1], p[4]], lineno=p.lineno(1))

    def callfunc(self, p):
        p[0] = Node('call function', data=p[1], children=[p[3]], lineno=p.lineno(1))

    def varlist(self, p):
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = Node('double varlist', children=[p[1], p[3]], lineno=p.lineno(1))

    def if_b(self, p):
        p[0] = Node('if then else', children=[p[2], p[4], p[6]], lineno=p.lineno(2))

    def iferr_b(self, p):
        if len(p) == 6:
            p[0] = Node('if error 1', data='You should have ELSE statement', lineno=p.lineno(1))
        else:
            p[0] = Node('if error 2', data='You should have THEN statement', lineno=p.lineno(1))

    def statement_gr(self, p):
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[1] = Node('Begin', data=p[1], lineno=p.lineno(1))
            p[3] = Node('End', data=p[3], lineno=p.lineno(1))
            p[0] = Node('statement group', children=[p[1], p[2], p[3]], lineno=p.lineno(1))

    def dowhile(self, p):
        p[0] = Node('do while', children=[p[2], p[4]], lineno=p.lineno(1))

    def dowhileerr(self, p):
        p[0] = Node('do while error', data='You should have statement', lineno=p.lineno(1))

    def function(self, p, functions):
        if p[2] in functions.keys():
            p[0] = Node('function error 1', data='function already declared', lineno=p.lineno(1))
            return True
        else:
            p[0] = Node('function', data=p[2], children=[p[4], p[6], p[8]], lineno=p.lineno)
            functions[p[2]] = 'function'
        return False

    def arrtype(self, p):
        if len(p) == 3:
            p[0] = Node('variable', data=p[2], children=[p[1]], lineno=p.lineno(1))
        else:
            p[0] = Node('comma variables', children=[p[1], p[3]], lineno=p.lineno(1))

    def cmd(self, p):
        if len(p) == 2:
            p[0] = Node('Robot command', data=p[1], lineno=p.lineno(1))
        else:
            p[0] = Node('Robot command', data=p[1], children=[p[2]], lineno=p.lineno(1))

    def dir(self, p):
        p[0] = Node('direction', data=p[1], lineno=p.lineno(1))
