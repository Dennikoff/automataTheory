class Variable:
    def __init__(self, value, type, name=''):
        if type == 'short int':
            type = 'short'
        if type == 'short':
            if isinstance(value, str):
                if value[0] == 's':
                    value = int(value[1:])
        elif type == 'int':
            value = int(value)
        self.value = value
        self.type = type
        self.name = name

    def set_value(self, value):
        self.value = value

    def __repr__(self):
        return f"Name: {self.name}; Type: {self.type}; Value: {self.value};"

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
         return Variable('False', type)
     if value.value == 0:
         return Variable('Undefined', type)
     if value.value > 0:
         return Variable('True', type)


def bool_to_int(value, type):
    if value.value == 'True':
        return Variable(1, type)
    if value.value == 'False':
        return Variable(-1, type)
    if value.value == 'Undefined':
        return Variable(0, type)



if __name__ == '__main__':
    a = Variable(0, 'int')
    print(type(5) == int)
    print(convert_type(a, 'bool'))
    print(convert_type(Variable('False', 'bool'), 'int'))
    print(Variable('s-100', 'short'))
