from Parser.ParserFile import ParserClass
from convertor import Variable
import convertor
from errors import ErrorHandler
from Parser.Node import Node
from errors import ErrType
import errors

class InterpreterClass:
    def __init__(self, program):
        self.parser = ParserClass()
        self.program = program
        self.tree = []
        self.functions = None
        self.has_errors = False
        self.errorHandler = ErrorHandler()
        self.err_type = ErrType
        self.curFunc = None
        self.variables = {}


    def interprete(self):
        self.tree, self.functions, self.has_errors = self.parser.parse(self.program)
        if not self.has_errors:
            if 'work' not in self.functions.keys():
                self.errorHandler.raise_err(ErrType.MissingWorkError.value)
            else:
                self.curFunc = 'work'
                self.nodeHandle(self.functions['work'].children[1])
                print('Return:', self.functions['work'].children[2])
        else:
            self.errorHandler.raise_err(self.err_type.SyntaxError.value)

    def nodeHandle(self, node):
        node_type = node.type
        try:
            if node_type == None:
                return
            elif node_type == 'program':
                self.nodeHandle(node.children[0])
            elif node_type == 'statement list':
                self.nodeHandle(node.children[0])
                self.nodeHandle(node.children[1])
            elif node_type == 'End of program':
                return
            elif node_type == 'declaration':
                var_type = node.children[0]
                var_var = node.children[1]
                try:
                    if var_type.data != 'vector of':
                        self.declaration(var_type, var_var, False)
                    else:
                        self.declaration(var_type, var_var, True)
                except Exception:
                    print("Something wrong in declaration")
            elif node_type == 'statement group':
                self.nodeHandle(node.children[0])
            elif node_type == 'assign':
                variable1 = node.children[0]
                variable2 = node.children[1]
                try:
                    self.assign(variable1, variable2)
                except KeyError as err:
                    self.errorHandler.raise_err(self.err_type.KeyError, [err])
                except Exception as err:
                    print(f"Something wrong in Assign {err}")
                    raise err
            elif node_type == 'expression':
                self.nodeHandle(node.children[1])
            elif node_type == 'expr comma':
                pass
            else:
                print('Error in node building or not all cases checked')
        except errors.MyKeyError as err:
            self.errorHandler.raise_err(self.err_type.KeyError.value)



    def declaration(self, type, var, flag_arr):
        if not flag_arr:
            if var.type == 'variable':
                variable = Variable(None, type.data, var.data)  #(value, type, name)
                self.variables[var.data] = variable
            elif var.type == 'assign':
                variable = Variable(0, type.data, var.children[0].data)  # (value, type, name)
                self.variables[var.children[0].data] = variable
                self.assign(var.children[0], var.children[1])
        else:
            print("[TODO]Vector declaration!!")
            #     variable = var.children[0]
            #     value = var.children[1]
            #     if value.type != 'math expression':
            #         variable = Variable(value.data, )


    def assign(self, name, value):
        # self.errorHandler.set_node(name)
        # raise errors.MyKeyError
        variable = self.variables[name.data]
        if value.type == 'math expression':
            cur_value = self.math_expression(value)
            variable.set_value(cur_value)
            print('kek')

    def math_expression(self, value):
        flag = False
        if value.data == 'add':
            if value.children[1].type == 'math expression':
                # if second child is math expression we create new math expression
                # where first element is sum of value.children[0].data and value.children[1].children[0].data
                # and second is value.children[1].children[1].data
                value_1 = value.children[1].children[0].data
                flag = True
                if value.children[1].type == 'bool':
                    value_1 = convertor.convert_type(Variable(value_1, 'bool'), 'int')[0]
                # value_1 = self.math_expression(value.children[1])
            else:
                value_1 = value.children[1].data
                if value.children[1].type == 'bool':
                    value_1 = convertor.convert_type(Variable(value_1, 'bool'), 'int')[0]
                    # convert_type returns tuple (value, type) so we take convert_type[0]
            value_2 = value.children[0].data
            if value.children[0].type == 'bool':
                value_2 = convertor.convert_type(Variable(value_2, 'bool'), 'int')[0]
            result = value_2 + value_1
            if flag:
                new_node = Node('math expression',
                     data=value.children[1].data,
                     children=[Node('digit', data=result, lineno=value.children[1].lineno),
                               value.children[1].children[1]],
                     lineno=value.children[1].lineno)
                result = self.math_expression(new_node)
            return result
        elif value.data == 'sub':
            if value.children[1].type == 'math expression':
                value_1 = value.children[1].children[0].data
                flag = True
                if value.children[1].type == 'bool':
                    value_1 = convertor.convert_type(Variable(value_1, 'bool'), 'int')[0]
                # value_1 = self.math_expression(value.children[1])
            else:
                value_1 = value.children[1].data
                if value.children[1].type == 'bool':
                    value_1 = convertor.convert_type(Variable(value_1, 'bool'), 'int')[0]
                    # convert_type returns tuple (value, type) so we take convert_type[0]
            value_2 = value.children[0].data
            if value.children[0].type == 'bool':
                value_2 = convertor.convert_type(Variable(value_2, 'bool'), 'int')[0]
            result = value_2 - value_1
            if flag:
                new_node = Node('math expression',
                                data=value.children[1].data,
                                children=[Node('digit', data=result, lineno=value.children[1].lineno),
                                          value.children[1].children[1]],
                                lineno=value.children[1].lineno)
                result = self.math_expression(new_node)
            return result


if __name__ == '__main__':
    f = open('check.txt', 'r')
    data = f.read()
    my_interpreter = InterpreterClass(data)
    my_interpreter.interprete()
