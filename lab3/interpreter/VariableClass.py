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