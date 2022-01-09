import sys
from enum import Enum
from Parser.Node import Node


def print_err(msg):
    sys.stderr.write(msg)


class ErrType(Enum):
    UnexpectedError = 0
    MissingWorkError = 1
    SyntaxError = 2
    KeyError = 3
    TypeError = 4
    RuntimeError = 5
    RepeatingParam = 6
    KeyErrorFunc = 7
    SizeOfError = 8
    FunctionVarlistError = 9
    WrongArrayDeclaration = 10


class ErrorHandler:
    def __init__(self):
        self.node = ''

    def set_node(self, node):
        self.node = node

    def raise_err(self, code=0, data=None):
        if data is None:
            data = ['placeholder']
        if code == 0:
            print_err(f"[ERROR] Unexpected Error on line {data[0].lineno}\n")
        elif code == 1:
            print_err(f"[ERROR] Missing Work function\n")
        elif code == 2:
            print_err(f"[ERROR] Some syntax error\n")
        elif code == 3:
            print_err(f"[ERROR] Variable {data[0].data} does not exist on line {data[0].lineno}\n")
        elif code == 4:
            print_err(f"[ERROR] Type of '{data[0].value}' and '{data[1].value}' are not the same on line {data[2].lineno}\n")
        elif code == 5:
            print_err(f"[ERROR] Runtime Error\n")
        elif code == 6:
            print_err(f"[ERROR] Variable '{data[0]}' already declared in function on line {data[1].lineno}\n")
        elif code == 7:
            print_err(f"[ERROR] Function named {data[0]} does not exist on line {data[1].lineno}\n")
        elif code == 8:
            print_err(f"[ERROR] Size of Error, invalid argument {data[0]} on line {data[1].lineno}\n")
        elif code == 9:
            print_err(f"[ERROR] Invalid number of parametern in calling function {data[0]} on line {data[1].lineno}\n")
        elif code == 10:
            print_err(f"[ERROR] Wrong array declaration on line {data[0].lineno}\n")

class MyRuntimeError(Exception):
    pass

class TypeError(Exception):
    pass

class UnexpectedError(Exception):
    pass

class MissingWorkError(Exception):
    pass

class SyntaxError(Exception):
    pass

class MyKeyError(Exception):
    pass

class RepeatingParam(Exception):
    pass

class KeyErrorFunc(Exception):
    pass

class SizeOfError(Exception):
    pass

class FunctionVarlistError(Exception):
    pass

class WrongArrayDeclaration(Exception):
    pass
