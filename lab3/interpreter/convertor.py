from interpreter.VariableClass import Variable


class arr_variable:
    def __init__(self, values, type, sizes, name =''):
        if type == 'short int':
            type = 'short'
        self.type = type
        self.array = []
        for number in values:
            pass



def convert_type(value, type):
    if value.type == type:
        return value
    if value.type == 'int' and type == 'bool':
        return int_to_bool(value, type)
    if value.type == 'bool' and type == 'int':
        return bool_to_int(value, type)


def int_to_bool(value, type):
     if value.value < 0:
         return Variable('false', type)
     if value.value == 0:
         return Variable('undefined', type)
     if value.value > 0:
         return Variable('true', type)


def bool_to_int(value, type):
    if value.value == 'true':
        return Variable(1, type)
    if value.value == 'false':
        return Variable(-1, type)
    if value.value == 'undefined':
        return Variable(0, type)



if __name__ == '__main__':
    a = Variable(0, 'int')
    print(type(5) == int)
    print(convert_type(a, 'bool'))
    print(convert_type(Variable('False', 'bool'), 'int'))
    print(Variable('s-100', 'short'))
