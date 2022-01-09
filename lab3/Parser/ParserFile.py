from lex.Lexer import LexerClass
import ply.yacc as yacc
import sys
from Parser.NodeBuilder import NodeBuilder



class ParserClass:
    tokens = LexerClass().tokens

    def __init__(self):
        self.lexer = LexerClass()
        self.parser = yacc.yacc(module=self)
        self.functions = dict()
        self.has_Syntax_Error = False
        self.node_build = NodeBuilder()

    def parse(self, data):
        res = self.parser.parse(data)
        return res, self.functions, self.has_Syntax_Error

    def p_program(self, p):
        """program : statement_list"""
        self.node_build.program(p)

    def p_statement_list(self, p):
        """statement_list : statement_list single_statement
                          | single_statement"""
        self.node_build.statement_list(p)


    def p_single_statement(self, p): # игнорировать newLine
        """single_statement : declaration ENDSTR
                            | setting ENDSTR
                            | if
                            | dowhile
                            | function
                            | callfunc ENDSTR
                            | cmd ENDSTR
                            | ENDSTR"""
        self.node_build.single_statement(p)

    def p_declaration(self, p):
        """declaration : type var"""
        self.node_build.declaration(p)

    def p_type(self, p):
        """type : INT
                | BOOL
                | SHORT INT
                | SHORT"""
        self.node_build.type(p)

    def p_var(self, p):
        """var : variable
               | setting
               | var COMMA var"""
        self.node_build.var(p)


    def p_setting(self, p):
        """setting : variable SET expr"""
        self.node_build.setting(p)

    def p_expr(self, p):
        """expr : variable
                | const
                | math_expr
                | callfunc
                | cmd
                | OPBR expr CLBR"""
        self.node_build.expr(p)

    def p_setting_arr(self, p):
        """setting : variable SET setarr"""
        self.node_build.setting_arr(p)

    def p_type_arr(self, p):
        """type : vectorof"""
        self.node_build.type_arr(p)

    def p_vectorof(self, p):
        """vectorof : VECTOROF type"""
        self.node_build.vectorof(p)

    def p_setarr(self, p):
        """setarr : CUOPBR setarr CUCLBR
                  | setarr COMMA setarr
                  | CUOPBR exprarr CUCLBR"""
        self.node_build.setarr(p)

    def p_exprarr(self, p):
        """exprarr : exprarr COMMA exprarr
                   | expr"""
        self.node_build.exprarr(p)

    def p_const(self, p):
        """const : digit
                 | bool
                 | sizeof"""
        self.node_build.const(p)

    def p_variable(self, p):
        """variable : VARIABLE
                    | VARIABLE index"""
        self.node_build.variable(p)

    def p_index(self, p):
        """index : SQOPBR expr SQCLBR
                 | index index"""
        self.node_build.index(p)

    def p_sizeof(self, p):
        """sizeof : SIZEOF OPBR type CLBR
                  | SIZEOF OPBR variable CLBR"""
        self.node_build.sizeof(p)

    def p_bool(self, p):
        """bool : TRUE
                | FALSE
                | UNDEFINED"""
        self.node_build.bool(p)

    def p_digit(self, p):
        """digit : INTTYP
                 | SHORTTYP"""
        self.node_build.digit(p)

    def p_math_expr(self, p): # !!!!
        """math_expr : expr EQUAL expr
                     | expr SUB expr
                     | expr ADD expr
                     | expr SECOND LARGER expr
                     | expr SECOND SMALLER expr
                     | expr FIRST LARGER expr
                     | expr FIRST SMALLER expr
                     | expr AND expr
                     | expr OR expr
                     | expr NOT AND expr
                     | expr NOT OR expr"""
        self.node_build.math_expr(p)

    def p_callfunc(self, p):
        """callfunc : VARIABLE OPBR varlist CLBR"""
        self.node_build.callfunc(p)

    def p_varlist(self, p):
        """varlist : variable
                   | const
                   | varlist COMMA varlist"""
        self.node_build.varlist(p)

    def p_if(self, p): # !!!!! второе убрать
        """if : IF expr THEN statement_gr ELSE statement_gr"""
        self.node_build.if_b(p)

    def p_iferr(self, p):
        """if : IF expr THEN statement_gr error
              | IF expr error"""
        self.node_build.iferr_b(p)

    def p_statement_gr(self, p):
        """statement_gr : BEGIN statement_list END
                        | single_statement"""
        self.node_build.statement_gr(p)

    def p_dowhile(self, p):
        """dowhile : DO statement_gr WHILE expr ENDSTR"""
        self.node_build.dowhile(p)

    def p_dowhileerr(self, p):
        """dowhile : DO error"""
        self.node_build.dowhileerr(p)


    def p_function(self, p):
        """function : FUNCTION VARIABLE OPBR arrtype CLBR statement_gr RETURN expr ENDSTR"""
        flag = self.node_build.function(p, self.functions)
        if flag:
            sys.stderr.write("Error in function declaration:\nName of the function already in use")

    def p_arrtype(self, p):
        """arrtype : type VARIABLE
                   | arrtype COMMA arrtype"""
        self.node_build.arrtype(p)

    def p_cmd(self, p):
        """cmd : MOVE
               | MOVE dir
               | RIGHT
               | LEFT
               | LMS"""
        self.node_build.cmd(p)

    def p_dir(self, p):
        """dir : RIGHT
               | LEFT"""
        self.node_build.dir(p)

    def p_error(self, p):
        try:
            sys.stderr.write(f"Unknown Error on {p.lineno} line Token: {p}\n")
        except Exception:
            sys.stderr.write(f"Unknown ERROR {p}")
        self.has_Syntax_Error = True

if __name__ == '__main__':
    f = open('check.txt', 'r')
    data = f.read()
    parser = ParserClass()
    res, functions, flag = parser.parse(data)
    print(res)
