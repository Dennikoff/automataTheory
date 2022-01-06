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


class ErrorHandler:
    def __init__(self):
        self.node = ''

    def set_node(self, node):
        self.node = node

    def raise_err(self, code=0, data=None):
        if data is None:
            data = ['placeholder']
        errors_list = {
            0: f"[ERROR] Unexpected Error\n",
            1: f"[ERROR] Missing Work function\n",
            2: f"[ERROR] Some syntax error\n",
            3: f"[ERROR] Key {data[0]} does not exist\n"
        }
        print_err(errors_list[code])

class UnexpectedError(Exception):
    pass

class MissingWorkError(Exception):
    pass

class SyntaxError(Exception):
    pass

class MyKeyError(Exception):
    pass