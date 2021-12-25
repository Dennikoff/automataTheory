from lex.Lexer import LexerClass
import ply.yacc as yacc
import sys




class ParserClass:
    tokens = LexerClass().tokens

    def __init__(self):
        self.lexer = LexerClass()
        self.parser = yacc.yacc(module=self)
        self.functions = dict()
        self.hasError = False

    def parse(self, data):
        res = self.parser.parse(data)
        return res, self.functions, self.hasError

    def p_program(self, p):
        """program : statement_list"""

    def p_statement_list(self, p):
        """statement_list : statement_list single_statement
                          | single_statement
                          | NEWLINE"""

    def p_single_statement(self, p):
        """single_statement : declaration ENDSTR NEWLINE
                    | setting ENDSTR NEWLINE
                    | if
                    | dowhile
                    | function
                    | callfunc ENDSTR NEWLINE
                    | cmd ENDSTR NEWLINE
                    | ENDSTR NEWLINE"""

    def p_declaration(self, p):
        """declaration : type var"""

    def p_type(self, p):
        """type : INT
                | BOOL
                | SHORT INT
                | SHORT"""

    def p_var(self, p):
        """var : variable
               | setting
               | var COMMA var"""

    def p_setting(self, p):
        """setting : variable SET expr"""

    def p_expr(self, p):
        """expr : variable
                | const
                | math_expr
                | callfunc
                | cmd
                | OPBR expr CLBR"""

    def p_setting_arr(self, p):
        """setting : variable SET setarr"""

    def p_type_arr(self, p):
        """type : vectorof"""

    def p_vectorof(self, p):
        """vectorof : VECTOROF type"""

    def p_setarr(self, p):
        """setarr : CUOPBR setarr CUCLBR
                  | setarr COMMA setarr
                  | CUOPBR exprarr CUCLBR"""

    def p_exprarr(self, p):
        """exprarr : exprarr COMMA exprarr
                   | expr"""

    def p_const(self, p):
        """const : digit
                 | bool
                 | sizeof"""

    def p_variable(self, p):
        """variable : VARIABLE
                    | VARIABLE index"""

    def p_index(self, p):
        """index : SQOPBR expr SQCLBR
                 | index index"""

    def p_sizeof(self, p):
        """sizeof : SIZEOF OPBR type CLBR
                  | SIZEOF OPBR variable CLBR"""

    def p_bool(self, p):
        """bool : TRUE
                | FALSE
                | UNDEFINED"""

    def p_digit(self, p):
        """digit : INTTYP
                 | SHORTTYP"""

    def p_math_expr(self, p):
        """math_expr : expr SUB expr
                     | expr ADD expr
                     | expr VERTBAR expr LARGER
                     | expr VERTBAR expr SMALLER
                     | expr AND expr
                     | expr OR expr
                     | expr NOT AND expr
                     | expr NOT OR expr"""

    def p_callfunc(self, p):
        """callfunc : VARIABLE OPBR varlist CLBR"""

    def p_varlist(self, p):
        """varlist : variable
                   | const
                   | varlist COMMA varlist"""

    def p_if(self, p):
        """if : IF expr THEN NEWLINE statement_gr ELSE NEWLINE statement_gr
              | IF expr THEN NEWLINE statement_gr ELSE ENDSTR NEWLINE"""

    def p_iferr(self, p):
        """if : IF expr THEN NEWLINE statement_gr error
              | IF expr error"""

    def p_statement_gr(self, p):
        """statement_gr : BEGIN NEWLINE statement_list END NEWLINE
                        | single_statement"""

    def p_dowhile(self, p):
        """dowhile : DO NEWLINE statement_gr WHILE expr ENDSTR NEWLINE"""

    def p_dowhileerr(self, p):
        """dowhile : DO NEWLINE error"""

    def p_function(self, p):
        """function : FUNCTION VARIABLE OPBR arrtype CLBR NEWLINE statement_gr RETURN expr ENDSTR NEWLINE"""

    def p_arrtype(self, p):
        """arrtype : type VARIABLE
                   | arrtype COMMA arrtype"""

    def p_cmd(self, p):
        """cmd : MOVE
               | MOVE dir
               | dir
               | LMS"""

    def p_dir(self, p):
        """dir : RIGHT
               | LEFT"""

    def p_error(self, p):
        try:
            sys.stderr.write(f"Unknown Error on {p.lineno} line\n")
        except Exception:
            sys.stderr.write("Unknown ERROR")
        self.hasError = True

if __name__ == '__main__':
    f = open('check.txt', 'r')
    data = f.read()
    parser = ParserClass()
    res, functions, flag = parser.parse(data)
