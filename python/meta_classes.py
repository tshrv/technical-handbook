"""
Classes that `generate` other classes are meta classes
`type` is the default meta class in python, which can be updated while writing class
So that python knows which meta class to use to generate current class
"""

from typing import Dict, Tuple
from loguru import logger as lg

# standard ways of creating a class - all equivalent
# class User:
# class User():
class User(metaclass=type):
    def __init__(self, name: str) -> None:
        self.name = name

    def show_name(self) -> None:
        lg.debug(self.name.upper())

# under the hood working of generating a class, uses type
# type(class_name: str, bases: Tuple, attrs: Dict)
def __init__1(self, name: str) -> None:
    self.name = name

def show_name_1(self) -> None:
    lg.debug(self.name.upper())

# bases = (object,)
# or,
# bases = ()
# works the same way as it by default subclasses from object
User1 = type('User1', (object,), {
    '__init__': __init__1,
    'show_name': show_name_1,
})

# generating class using a custom meta class
class MetaCls(type):
    def __new__(cls: type, cls_name:str, bases: Tuple, attributes: Dict) -> type:
        lg.debug((cls_name, bases, attributes))
        return super().__new__(cls, cls_name, bases, attributes)

class User2(metaclass=MetaCls):
    def __init__(self, name: str) -> None:
        self.name = name

    def show_name(self) -> None:
        lg.debug(self.name.upper())

# generating class using a custom meta class though function call
User3 = MetaCls('User3', (), {
    '__init__': __init__1,
    'show_name': show_name_1,
})

def main():
    # standard
    lg.debug(type(User))
    user = User('Tushar')
    user.show_name()
    lg.debug(dir(user))
    lg.debug('-'*10)

    # using type
    lg.debug(type(User1))
    user_1 = User1('Ayush')
    user_1.show_name()
    lg.debug(dir(user_1))
    lg.debug('-'*10)

    # using custom meta class via class definiton
    lg.debug(type(User2))
    user_2 = User2('Shishir')
    user_2.show_name()
    lg.debug(dir(user_2))
    lg.debug('-'*10)

    # using custom meta class via function call
    lg.debug(type(User3))
    user_3 = User3('Simran')
    user_3.show_name()
    lg.debug(dir(user_3))
    lg.debug('-'*10)

main()