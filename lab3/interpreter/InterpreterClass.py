from Parser.ParserFile import ParserClass
from interpreter import convertor
from interpreter.errors import ErrorHandler
from Parser.Node import Node
from interpreter.errors import ErrType
from interpreter import errors
from interpreter.VariableClass import Variable


class VariableList:
    def __init__(self):
        self.pre = None
        self.variables = {}
        self.next = None


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
        self.variables = VariableList()



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
                except Exception as err:
                    print("Something wrong in declaration")
                    raise err
            elif node_type == 'statement group':
                self.nodeHandle(node.children[0])
            elif node_type == 'assign':
                variable1 = node.children[0]
                variable2 = node.children[1]
                try:
                    self.assign(variable1, variable2)
                except Exception as err:
                    print(f"Something wrong in Assign {err}")
                    raise err
            elif node_type == 'expression':
                self.nodeHandle(node.children[1])
            elif node_type == 'expr comma':
                pass
            elif node_type == 'if then else':
                try:
                    self.if_statement(node.children[0], node.children[1], node.children[2])
                except Exception as err:
                    self.returnEnv()
                    print('Something wrong in IF statement')
                    raise err
            elif node_type == 'call function':
                pass
            elif node_type == 'do while':
                try:
                    self.dowhile_statement(node.children[0], node.children[1])
                except Exception as err:
                    print('Something wrong in DO WHILE statement')
                    raise err
            else:
                print('Error in node building or not all cases checked')
        except errors.MyKeyError as err:
            self.errorHandler.raise_err(self.err_type.KeyError.value, [err])
        except errors.UnexpectedError:
            self.errorHandler.raise_err(self.err_type.UnexpectedError.value)
        except errors.TypeError as err:
            self.errorHandler.raise_err(self.err_type.TypeError.value, [err.args[0], err.args[1]])

    def declaration(self, type, var, flag_arr):
        if not flag_arr:
            if var.type == 'variable':
                variable = Variable(0, type.data, var.data)  # (value, type, name)
                self.variables.variables[var.data] = variable
            elif var.type == 'assign':
                variable = Variable(0, type.data, var.children[0].data)  # (value, type, name)
                self.variables.variables[var.children[0].data] = variable
                self.assign(var.children[0], var.children[1])
        else:
            print("[TODO]Vector declaration!!")
            #     variable = var.children[0]
            #     value = var.children[1]
            #     if value.type != 'math expression':
            #         variable = Variable(value.data, )


    def createNewEnv(self):
        current = VariableList()
        current.pre = self.variables
        self.variables.next = current
        self.variables = self.variables.next


    def returnEnv(self):
        self.variables = self.variables.pre


    def if_statement(self, expression, then_statement, else_statement):
        self.createNewEnv()
        if expression.type == 'bool':
            condition = expression.data
        elif expression.type == 'digit':
            condition = expression.data
            condition = convertor.convert_type(Variable(condition, 'int'), 'bool').value
        elif expression.type == 'variable':
            variable = self.get_variable(expression.data)
            condition = convertor.convert_type(variable, 'bool').value
        elif expression.type == 'math expression':
            condition = self.math_expression(expression)
            condition = convertor.convert_type(condition, 'bool').value
        else:
            print("Something wrong in if")
            condition = 'undefined'
        if condition == 'true':
            self.nodeHandle(then_statement)
        elif condition == 'false':
            self.nodeHandle(else_statement)
        self.returnEnv()


    def dowhile_statement(self, body, expression):
        self.createNewEnv()
        counter = 0
        condition = 'true'
        while condition == 'true':
            counter += 1
            self.nodeHandle(body)
            if expression.type == 'brackets expression':
                expression = expression.children[0]
            if expression.type == 'math expression':
                variable = self.math_expression(expression)
                condition = convertor.convert_type(variable, 'bool').value
            elif expression.type == 'variable':
                condition = self.get_variable(expression.data)
            elif expression.type == 'bool':
                condition = expression.data
            elif expression.type == 'digit':
                variable = Variable(expression.data, 'int')
                condition = convertor.convert_type(variable, 'bool')
            else:
                raise errors.UnexpectedError
            if counter > 10000:
                raise errors.MyRuntimeError()
        self.returnEnv()


    def get_variable(self, name):
        current = self.variables
        variable = None
        while True:
            try:
                variable = current.variables[name]
                break
            except KeyError:
                current = current.pre
                if current == None:
                    break
        if not(variable):
            raise KeyError(name)
        return variable

    def assign(self, name, value):
        # self.errorHandler.set_node(name)
        # raise errors.MyKeyError
        variable = self.get_variable(name.data)
        if value.type == 'math expression':
            cur_value = self.math_expression(value).value
            variable.set_value(cur_value)
        elif value.type == 'digit':
            cur_value = value.data
            cur_value = convertor.convert_type(Variable(cur_value, 'int'), variable.type).value
            variable.set_value(cur_value)
        elif value.type == 'bool':
            cur_value = value.data
            cur_value = convertor.convert_type(Variable(cur_value, 'bool'), variable.type).value
            variable.set_value(cur_value)
        elif value.type == 'variable':
            variable_second = self.get_variable(value.data)
            variable.set_value(variable_second.value)

    def math_expression(self, value):
        flag = False
        if value.data == '==' or value.data == 'first larger' or value.data == 'first smaller' or value.data == 'second larger' or value.data == 'second smaller':
            val1 = value.children[0]
            val2 = value.children[1]
            if val1.type == 'brackets expression':
                val1 = val1.children[0]
            if val1.type == 'math expression':
                value_1 = self.math_expression(val1)
            elif val1.type == 'variable':
                value_1 = self.get_variable(val1.data)
            elif val1.type == 'bool':
                value_1 = Variable(val1.data, 'bool')
            elif val1.type == 'digit':
                value_1 = Variable(val1.data, 'int')
            else:
                raise errors.UnexpectedError
            if val2.type == 'brackets expression':
                val2 = val2.children[0]
            if val2.type == 'math expression':
                value_2 = self.math_expression(val2)
            elif val2.type == 'variable':
                value_2 = self.get_variable(val2.data)
            elif val2.type == 'bool':
                value_2 = Variable(val2.data, 'bool')
            elif val2.type == 'digit':
                value_2 = Variable(val2.data, 'int')
            else:
                raise errors.UnexpectedError
            if value_1.type != value_2.type:
                raise errors.TypeError(value_1, value_2)
            if value.data == '==':
                if value_1.value == value_2.value:
                    return Variable('true', 'bool')
                else:
                    return Variable('false', 'bool')
            elif value.data == 'first larger' or value.data == 'second smaller':
                if value_1.value > value_2.value:
                    return Variable('true', 'bool')
                else:
                    return Variable('false', 'bool')
            elif value.data == 'first smaller' or value.data == 'second larger':
                if value_1.value < value_2.value:
                    return Variable('true', 'bool')
                else:
                    return Variable('false', 'bool')
        if value.data == 'add' or value.data == 'sub':
            if value.children[1].type == 'math expression':
                # if second child is math expression we create new math expression
                # where first element is sum of value.children[0].data and value.children[1].children[0].data
                # and second is value.children[1].children[1].data
                value_1 = 0
                if value.children[1].children[0].type == 'brackets expression':
                    saved_val = value
                    value = value.children[1].children[0]
                    if value.children[0].type == 'math expression':
                        value_1 = self.math_expression(value.children[0]).value
                    elif value.children[0].type == 'variable':
                        variable = self.get_variable(value.children[1].data)
                        value_1 = variable.value
                        if variable.type == 'bool':
                            value_1 = convertor.convert_type(Variable(value_1, 'bool'), 'int').value
                    else:
                        value_1 = value.children[0].data
                        if value.children[0].type == 'bool':
                            value_1 = convertor.convert_type(Variable(value_1, 'bool'), 'int').value
                    value = saved_val
                elif value.children[1].children[0].type == 'variable':
                    variable = self.get_variable(value.children[1].children[0].data)
                    value_1 = variable.value
                    if variable.type == 'bool':
                        value_1 = convertor.convert_type(Variable(value_1, 'bool'), 'int').value
                else:
                    value_1 = value.children[1].children[0].data
                    if value.children[1].children[0].type == 'bool':
                        value_1 = convertor.convert_type(Variable(value_1, 'bool'), 'int').value
                flag = True
                # value_1 = self.math_expression(value.children[1])
            elif value.children[1].type == 'variable':
                variable = self.get_variable(value.children[1].data)
                value_1 = variable.value
                if variable.type == 'bool':
                    value_1 = convertor.convert_type(Variable(value_1, 'bool'), 'int').value
            elif value.children[1].type == 'brackets expression':
                #value = value.children[1]
                if value.children[1].children[0].type == 'math expression':
                    value_1 = self.math_expression(value.children[1].children[0]).value
                elif value.children[1].children[0].type == 'variable':
                    variable = self.get_variable(value.children[1].children[1].data)
                    value_1 = variable.value
                    if variable.type == 'bool':
                        value_1 = convertor.convert_type(Variable(value_1, 'bool'), 'int').value
                else:
                    value_1 = value.children[1].children[0].data
                    if value.children[1].type == 'bool':
                        value_1 = convertor.convert_type(Variable(value_1, 'bool'), 'int').value
            else:
                value_1 = value.children[1].data
                if value.children[1].type == 'bool':
                    value_1 = convertor.convert_type(Variable(value_1, 'bool'), 'int').value
                    # convert_type returns tuple (value, type) so we take convert_type[0]
            if value.children[0].type == 'variable':
                variable = self.get_variable(value.children[0].data)
                value_2 = variable.value
                if variable.type == 'bool':
                    value_2 = convertor.convert_type(Variable(value_2, 'bool'), 'int').value
            elif value.children[0].type == 'brackets expression':
                value = value.children[0]
                if value.children[0] == 'math expression':
                    value_2 = self.math_expression(value.children[0]).value
                elif value.children[0] == 'variable':
                    variable = self.get_variable(value.children[0].data)
                    value_2 = variable.value
                    if variable.type == 'bool':
                        value_2 = convertor.convert_type(Variable(value_2, 'bool'), 'int').value
                else:
                    value_2 = value.children[0].data
                    if value.children[0].type == 'bool':
                        value_2 = convertor.convert_type(Variable(value_2, 'bool'), 'int').value
            else:
                value_2 = value.children[0].data
                if value.children[0].type == 'bool':
                    value_2 = convertor.convert_type(Variable(value_2, 'bool'), 'int').value
            if value.data == 'add':
                result = value_2 + value_1
            elif value.data == 'sub':
                result = value_2 - value_1
            else:
                raise errors.UnexpectedError
            if flag:
                new_node = Node('math expression',
                     data=value.children[1].data,
                     children=[Node('digit', data=result, lineno=value.children[1].lineno),
                               value.children[1].children[1]],
                     lineno=value.children[1].lineno)
                result = self.math_expression(new_node).value
            return Variable(result, 'int')
        elif value.data == 'and' or value.data == 'or' or value.data == 'not and' or value.data == 'not or':
            if value.children[1].type == 'math expression':
                # if second child is math expression we create new math expression
                # where first element is sum of value.children[0].data and value.children[1].children[0].data
                # and second is value.children[1].children[1].data
                value_1 = 0
                if value.children[1].children[0].type == 'brackets expression':
                    saved_val = value
                    value = value.children[1].children[0]
                    if value.children[0].type == 'math expression':
                        value_1 = self.math_expression(value.children[0]).value
                    elif value.children[0].type == 'variable':
                        variable = self.get_variable(value.children[1].data)
                        value_1 = variable.value
                        if variable.type == 'int':
                            value_1 = convertor.convert_type(Variable(value_1, 'int'), 'bool').value
                    else:
                        value_1 = value.children[0].data
                        if value.children[0].type == 'digit':
                            value_1 = convertor.convert_type(Variable(value_1, 'int'), 'bool').value
                    value = saved_val
                elif value.children[1].children[0].type == 'variable':
                    variable = self.get_variable(value.children[1].children[0].data)
                    value_1 = variable.value
                    if variable.type == 'int':
                        value_1 = convertor.convert_type(Variable(value_1, 'int'), 'bool').value
                else:
                    value_1 = value.children[1].children[0].data
                    if value.children[1].children[0].type == 'digit':
                        value_1 = convertor.convert_type(Variable(value_1, 'int'), 'bool').value
                flag = True
                # value_1 = self.math_expression(value.children[1])
            elif value.children[1].type == 'variable':
                variable = self.get_variable(value.children[1].data)
                value_1 = variable.value
                if variable.type == 'int':
                    value_1 = convertor.convert_type(Variable(value_1, 'int'), 'bool').value
            elif value.children[1].type == 'brackets expression':
                # value = value.children[1]
                if value.children[1].children[0].type == 'math expression':
                    value_1 = self.math_expression(value.children[1].children[0]).value
                elif value.children[1].children[0].type == 'variable':
                    variable = self.get_variable(value.children[1].children[1].data)
                    value_1 = variable.value
                    if variable.type == 'int':
                        value_1 = convertor.convert_type(Variable(value_1, 'int'), 'bool').value
                else:
                    value_1 = value.children[1].children[0].data
                    if value.children[1].type == 'digit':
                        value_1 = convertor.convert_type(Variable(value_1, 'int'), 'bool').value
            else:
                value_1 = value.children[1].data
                if value.children[1].type == 'digit':
                    value_1 = convertor.convert_type(Variable(value_1, 'int'), 'bool').value
                    # convert_type returns tuple (value, type) so we take convert_type[0]
            if value.children[0].type == 'variable':
                variable = self.get_variable(value.children[0].data)
                value_2 = variable.value
                if variable.type == 'int':
                    value_2 = convertor.convert_type(Variable(value_2, 'int'), 'bool').value
            elif value.children[0].type == 'brackets expression':
                value = value.children[0]
                if value.children[0] == 'math expression':
                    value_2 = self.math_expression(value.children[0]).value
                elif value.children[0] == 'variable':
                    variable = self.get_variable(value.children[0].data)
                    value_2 = variable.value
                    if variable.type == 'int':
                        value_2 = convertor.convert_type(Variable(value_2, 'int'), 'bool').value
                else:
                    value_2 = value.children[0].data
                    if value.children[0].type == 'digit':
                        value_2 = convertor.convert_type(Variable(value_2, 'int'), 'bool').value
            else:
                value_2 = value.children[0].data
                if value.children[0].type == 'digit':
                    value_2 = convertor.convert_type(Variable(value_2, 'int'), 'bool').value
            if value.data == 'and':
                if value_1 == 'false' or value_2 == 'false':
                    result = 'false'
                elif value_1 == 'undefined' or value_2 == 'undefined':
                    result = 'undefined'
                else:
                    result = 'true'
            elif value.data == 'or':
                if value_1 == 'true' or value_2 == 'true':
                    result = 'true'
                elif value_1 == 'undefined' or value_2 == 'undefined':
                    result = 'undefined'
                else:
                    result = 'false'
            elif value.data == 'not and':
                if value_1 == 'false' or value_2 == 'false':
                    result = 'true'
                elif value_1 == 'undefined' or value_2 == 'undefined':
                    result = 'undefined'
                else:
                    result = 'false'
            elif value.data == 'not or':
                if value_1 == 'true' or value_2 == 'true':
                    result = 'false'
                elif value_1 == 'undefined' or value_2 == 'undefined':
                    result = 'undefined'
                else:
                    result = 'true'
            else:
                raise errors.UnexpectedError
            if flag:
                new_node = Node('math expression',
                                data=value.children[1].data,
                                children=[Node('bool', data=result, lineno=value.children[1].lineno),
                                          value.children[1].children[1]],
                                lineno=value.children[1].lineno)
                result = self.math_expression(new_node).value
            return Variable(result, 'bool')


if __name__ == '__main__':
    f = open('check.txt', 'r')
    data = f.read()
    my_interpreter = InterpreterClass(data)
    my_interpreter.interprete()
