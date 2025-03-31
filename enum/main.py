from enum import Enum
from http_status import *

def test_boolean():
    a = True
    b = True
    print(a is b)  # True

def test_boolean2():
    # True = False  # SyntaxError: cannot assign to True
    pass

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    @classmethod
    def printMembers(cls):
        for color in cls:
            print(color.name, color.value)

def test_enum():
    a = Color.RED
    b = Color.RED
    # Color.RED = 4 # AttributeError: can't set attribute
    print(a is b)  # True

if __name__ == '__main__':
    test_boolean()
    test_enum()
    Color.printMembers()
    handle_http(HTTPStatus.OK)
    handle_http(HTTPStatus.NOT_FOUND)