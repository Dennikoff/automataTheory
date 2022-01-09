import copy
import sys

from Parser.ParserFile import ParserClass
from interpreter import convertor
from interpreter.errors import ErrorHandler
from Parser.Node import Node
from interpreter.errors import ErrType
from interpreter import errors
from interpreter.VariableClass import Variable
from interpreter.VariableClass import ArrVariable


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
                return_value = self.expression(self.functions['work'].children[2]).value
                print('Return:', return_value)
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
                    print(f"Something wrong in Assign")
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
                try:
                    self.callfunc(node)
                except Exception as err:

                    self.returnEnv()
                    print('Something wrong in Call function')
                    raise err
            elif node_type == 'do while':
                try:
                    self.dowhile_statement(node)
                except Exception as err:
                    self.returnEnv()
                    print('Something wrong in DO WHILE statement')
                    raise err
            else:
                print('Error in node building or not all cases checked')
        except errors.MyKeyError as err:
            self.errorHandler.raise_err(self.err_type.KeyError.value, [err.args[0]])
        except errors.UnexpectedError as err:
            self.errorHandler.raise_err(self.err_type.UnexpectedError.value, [err.args[0]])
        except errors.TypeError as err:
            self.errorHandler.raise_err(self.err_type.TypeError.value, [err.args[0], err.args[1], err.args[2]])
        except errors.KeyErrorFunc as err:
            self.errorHandler.raise_err(self.err_type.KeyErrorFunc.value, [err.args[0], err.args[1]])
        except errors.RepeatingParam as err:
            self.errorHandler.raise_err(self.err_type.RepeatingParam.value, [err.args[0], err.args[1]])
        except errors.MyRuntimeError as err:
            self.errorHandler.raise_err((self.err_type.RuntimeError.value))
            sys.exit(self.err_type.RuntimeError.value)
        except errors.SizeOfError as err:
            self.errorHandler.raise_err(self.err_type.SizeOfError.value, [err.args[0], err.args[1]])
        except errors.FunctionVarlistError as err:
            self.errorHandler.raise_err(self.err_type.FunctionVarlistError.value, [err.args[0], err.args[1]])
        except errors.WrongArrayDeclaration as err:
            self.errorHandler.raise_err(self.err_type.WrongArrayDeclaration.value, [err.args[0]])

    def get_indexes_arr(self, node, sizelist):
        for child in node.children:
            if child.type == 'double index':
                self.get_indexes_arr(child, sizelist)
            elif child.type == 'squared bracket':
                value = self.expression(child.children[0])
                value = convertor.convert_type(value, 'int').value
                sizelist.append(value)


    def get_values(self, node, values):
        if node.type == 'expr comma':
            for child in node.children:
                if child.type != 'expr comma':
                    values.append(self.expression(child).value)
                elif child.type == 'expr comma':
                    self.get_values(child, values)
        else:
            errors.UnexpectedError(node)


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
            scope_count, arr_type = self.arr_count(type, 0)
            if var.type == 'array variable':
                name = var.data
                sizelist = []
                self.get_indexes_arr(var, sizelist)
                if len(sizelist) != scope_count:
                    raise errors.WrongArrayDeclaration(var)
                variable = ArrVariable(sizelist, arr_type, name=name)
                self.variables.variables[name] = variable
            elif var.type == 'assign array':
                name = var.children[0].data
                values = []
                self.get_values(var.children[1].children[0], values)
                variable = ArrVariable([len(values)], arr_type, values, name=name)
                self.variables.variables[name] = variable
            elif var.type == 'assign':
                name = var.children[0].data
                if var.children[1].type == 'call function':
                    variable = self.callfunc(var.children[1])
                    if isinstance(variable, ArrVariable):
                        variable.name = name
                        self.variables.variables[name] = variable
                    else:
                        raise errors.WrongArrayDeclaration(var)






    def expression(self, node):
        if node.type == 'variable':
            return self.get_variable(node)
        elif node.type == 'array variable':
            return self.get_Variable_arr(self.get_variable(node), node)
        elif node.type == 'math expression':
            return self.math_expression(node)
        elif node.type == 'digit':
            return Variable(node.data, 'int')
        elif node.type == 'bool':
            return Variable(node.data, 'bool')
        elif node.type == 'call function':
            return self.callfunc(node)
        elif node.type == 'size of':
            return Variable(self.sizeof(node.children[0]), 'int')
        elif node.type == 'brackets expression':
            return self.expression(node.children[0])
        else:
            raise errors.UnexpectedError(node)



    def arr_count(self, node, count):
        if node.type == 'type':
            return count, node.data
        else:
            count += 1
            return self.arr_count(node.children[0], count)


    def sizeof(self, node):
        if node.type == 'variable':
            data = self.get_variable(node).type
        else:
            data = node.data
        if data == 'int':
            return 4
        elif data == 'bool':
            return 1
        elif data == 'short':
            return 2
        else:
            raise errors.SizeOfError(data, node)


    def createNewEnv(self):
        current = VariableList()
        current.pre = self.variables
        self.variables.next = current
        self.variables = self.variables.next


    def returnEnv(self):
        self.variables = self.variables.pre


    def varlist(self, node, varlist):
        variable_1 = node.children[0]
        if variable_1.type == 'variable':
            variable_1 = self.get_variable(variable_1)
            if isinstance(variable_1, Variable):
                variable_1 = variable_1.value
            elif isinstance(variable_1, ArrVariable):
                arr = []
                for value in variable_1.values:
                    arr.append(value.value)
                variable_1 = arr
        elif variable_1.type == 'size of':
            variable_1 = self.sizeof(variable_1)
        else:
            variable_1 = variable_1.data
        varlist.append(variable_1)
        if len(node.children) > 1:
            variable_2 = node.children[1]
            if variable_2.type == 'double varlist':
                self.varlist(variable_2, varlist)
                return
            elif variable_2.type == 'variable':
                variable_2 = self.get_variable(variable_2.data).value
            elif variable_2.type == 'size of':
                variable_2 = self.sizeof(variable_2)
            else:
                variable_2 = variable_2.data
            varlist.append(variable_2)





    def callfunc(self, node):
        func_name = node.data
        try:
            func = self.functions[func_name]
        except KeyError as err:
            self.createNewEnv()
            raise errors.KeyErrorFunc(err, node)
        varlist = []
        if node.children[0].type == 'double varlist':
            self.varlist(node.children[0], varlist)
        else:
            self.varlist(node, varlist)
        self.createNewEnv()
        self.comma_variables(func.children[0], varlist, node)
        self.nodeHandle(func.children[1])
        return_value = func.children[2]
        value = self.expression(return_value)
        self.returnEnv()
        return value


    def if_statement(self, expression, then_statement, else_statement):
        self.createNewEnv()
        condition = self.expression(expression)
        condition = convertor.convert_type(condition, 'bool').value
        if condition == 'true':
            self.nodeHandle(then_statement)
        elif condition == 'false':
            self.nodeHandle(else_statement)
        self.returnEnv()


    def dowhile_statement(self, node):
        body = node.children[0]
        expression = node.children[1]
        self.createNewEnv()
        counter = 0
        condition = 'true'
        while condition == 'true':
            counter += 1
            self.nodeHandle(body)
            condition = self.expression(expression)
            condition = convertor.convert_type(condition, 'bool').value
            if counter > 100000:
                raise errors.MyRuntimeError()
        self.returnEnv()


    def get_variable(self, node):
        name = node.data
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
            raise errors.MyKeyError(node)
        return variable


    def get_Variable_arr(self, variable, node):
        indexes = []
        self.get_indexes_arr(node, indexes)
        if len(indexes) == 1:
            return variable.values[indexes[0]]
        if len(indexes) == 2:
            return variable.values[indexes[0]][indexes[1]]


    def assign(self, name, value):
        # self.errorHandler.set_node(name)
        # raise errors.MyKeyError
        variable = self.get_variable(name)
        if isinstance(variable, Variable):
            cur_value = self.expression(value)
            cur_value = convertor.convert_type(cur_value, variable.type).value
            variable.set_value(cur_value)
        elif isinstance(variable, ArrVariable):
            cur_value = self.expression(value)
            if not isinstance(cur_value, ArrVariable):
                cur_value = convertor.convert_type(cur_value, variable.type).value
            var = self.get_Variable_arr(variable, name)
            var.set_value(cur_value)



    def math_expression(self, value):
        flag = False
        if value.data == '==' or value.data == 'first larger' or value.data == 'first smaller' or value.data == 'second larger' or value.data == 'second smaller':
            value_1 = self.expression(value.children[0])
            value_2 = self.expression(value.children[1])
            if value_1.type != value_2.type:
                raise errors.TypeError(value_1, value_2, value)
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
                value_1 = self.expression(value.children[1].children[0])
                value_1 = convertor.convert_type(value_1, 'int').value
                flag = True
                # value_1 = self.math_expression(value.children[1])
            elif value.children[1].type == 'variable':
                variable = self.get_variable(value.children[1])
                value_1 = variable.value
                if variable.type == 'bool':
                    value_1 = convertor.convert_type(Variable(value_1, 'bool'), 'int').value
            elif value.children[1].type == 'array variable':
                return self.get_Variable_arr(self.get_variable(value.children[1]), value.children[1].children[0])
            elif value.children[1].type == 'brackets expression':
                value_1 = self.expression(value.children[1])
                value_1 = convertor.convert_type(value_1, 'int').value
            else:
                value_1 = value.children[1].data
                if value.children[1].type == 'bool':
                    value_1 = convertor.convert_type(Variable(value_1, 'bool'), 'int').value
                    # convert_type returns tuple (value, type) so we take convert_type[0]
            value_2 = self.expression(value.children[0])
            value_2 = convertor.convert_type(value_2, 'int').value
            if value.data == 'add':
                result = value_2 + value_1
            elif value.data == 'sub':
                result = value_2 - value_1
            else:
                raise errors.UnexpectedError(value)
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
                value_1 = self.expression(value.children[1].children[0])
                value_1 = convertor.convert_type(value_1, 'bool').value
                flag = True
                # value_1 = self.math_expression(value.children[1])
            elif value.children[1].type == 'variable':
                variable = self.get_variable(value.children[1])
                value_1 = convertor.convert_type(variable, 'bool').value
            elif value.children[1].type == 'array variable':
                value_1 = self.get_Variable_arr(self.get_variable(value.children[1]), value.children[1].children[0])
                value_1 = convertor.convert_type(value_1, 'bool').value
            elif value.children[1].type == 'brackets expression':
                value_1 = self.expression(value.children[1])
                value_1 = convertor.convert_type(value_1, 'bool').value
            else:
                value_1 = value.children[1].data
                if value.children[1].type == 'digit':
                    value_1 = convertor.convert_type(Variable(value_1, 'int'), 'bool').value
                    # convert_type returns tuple (value, type) so we take convert_type[0]
            value_2 = self.expression(value.children[0])
            value_2 = convertor.convert_type(value_2, 'bool').value
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
                raise errors.UnexpectedError(value)
            if flag:
                new_node = Node('math expression',
                                data=value.children[1].data,
                                children=[Node('bool', data=result, lineno=value.children[1].lineno),
                                          value.children[1].children[1]],
                                lineno=value.children[1].lineno)
                result = self.math_expression(new_node).value
            return Variable(result, 'bool')


    def comma_variables(self, node, varlist, name):
        for child in node.children:
            if child.type == 'variable':
                try:
                    self.variables.variables[child.data]
                    raise errors.RepeatingParam(child.data, child)
                except KeyError:
                    if len(varlist) != 0:
                        value = varlist.pop(0)
                    else:
                        raise errors.FunctionVarlistError(name.data, name)
                    if child.children[0].type == 'Vector of':
                        name = child.data
                        size = len(value)
                        sizelist = []
                        scope_count, arr_type = self.arr_count(child.children[0], 0)
                        variable = ArrVariable([size], arr_type, value, name=name)
                    else:
                        variable = Variable(value, child.children[0].data, child.data)
                    self.variables.variables[child.data] = variable
            elif child.type == 'comma variables':
                self.comma_variables(child, varlist, name)
            else:
                raise errors.UnexpectedError(node)
        if len(varlist) != 0:
            raise errors.FunctionVarlistError(name.data, name)


if __name__ == '__main__':
    f = open('check2.txt', 'r')      #errors_check.txt не забыть показать отсутствие функции work
    data = f.read()
    my_interpreter = InterpreterClass(data)
    my_interpreter.interprete()
