import sys
from enum import Enum
from parser.Node import Node


def print_error(msg):
    sys.stderr.write(msg)


class ErrType(Enum):
    UnexpectedError = 0


class ErrorHandler:
    def __init__(self, node):
        self.node = node


    def raise_err(self, code=0):
        errors_list = {
            0: f"Unexpected Error"
        }
        print_error(errors_list[code])




