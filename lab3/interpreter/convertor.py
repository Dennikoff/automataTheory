class variable:
    def __init__(self, value, type, name=''):
        if type == 'short':
            if isinstance(value, str):
                if value[0] == 's':
                    value = int(value[1:])
        self.value = value
        self.type = type
        self.name = name


    def __repr__(self):
        return f"Name: {self.name}; Type: {self.type}; Value: {self.value};"


def convert_type(value, type):
    if value.type == type:
        return value
    if value.type == 'int' and type == 'bool':
        return int_to_bool(value, type)
    if value.type == 'bool' and type == 'int':
        return bool_to_int(value, type)


def int_to_bool(value, type):
     if value.value < 0:
         return variable('False', type)
     if value.value == 0:
         return variable('Undefined', type)
     if value.value > 0:
         return variable('True', type)


def bool_to_int(value, type):
    if value.value == 'True':
        return variable(1, type)
    if value.value == 'False':
        return variable(-1, type)
    if value.value == 'Undefined':
        return variable(0, type)



if __name__ == '__main__':
    a = variable(0, 'int')
    print(type(5) == int)
    print(convert_type(a, 'bool'))
    print(convert_type(variable('False', 'bool'), 'int'))
    print(variable('s-100', 'short'))
