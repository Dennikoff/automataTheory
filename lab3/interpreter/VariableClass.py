import sys

from interpreter import convertor

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



class ArrVariable:
    def __init__(self, sizes, type, values=None, name=''):
        if not values:
            self.type = type
            self.name = name
            self.values = []
            for index, size in enumerate(sizes):
                if index == 0:
                    value = Variable(0, 'int')
                else:
                    value = self.values.copy()
                    self.values = []
                for i in range(size):
                    if not isinstance(value, Variable):
                        new_value = []
                        for child in value:
                            if isinstance(child, Variable):
                               new_value.append(Variable(child.value, child.type))

                        value = new_value
                    else:
                        value = convertor.convert_type(Variable(0, 'int'), type)
                    self.values.append(value)
        else:
            self.type = type
            self.name = name
            self.values = []
            counter = 0
            for index, size in enumerate(sizes):
                if index == 0:
                    value = Variable(0, 'int')
                else:
                    value = self.values.copy()
                    self.values = []
                for i in range(size):
                    if not isinstance(value, Variable):
                        new_value = []
                        for child in value:
                            if isinstance(child, Variable):
                               new_value.append(Variable(child.value, child.type))

                        value = new_value
                    else:
                        value = convertor.convert_type(Variable(values[counter], 'int'), type)
                        counter += 1
                    self.values.append(value)



