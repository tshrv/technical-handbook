"""
Observing functioning of `__getattr__`, `__getattribute__` and `__get__`

Assume object 'a' of class A
Trying to access any attribute 'x' of a => a.x
This will trigger a.__getattribute__('x')
    __getattribute__ will check whether x is an attribute or not
    if not, it'll raise an Attribute error
        __getattr__ if implemented, will be triggered in this case
        this has to return a COMPUTED value as we are here since x is not an attribute of the instance
    if yes, it'll check if it is a descriptor (contains __get__ attribute)
        if yes, return x.__get__()
        if not, returns x
"""

from typing import Any
from loguru import logger as lg


class A:
    def __init__(self, val: int = None) -> None:
        self.val = val

    def __getattribute__(self, __name: str) -> Any:
        lg.info(f'__getattribute__, {__name}')
        return super().__getattribute__(__name)
    
    def __getattr__(self, __name: str) -> Any:
        lg.info(f'__getattr__ {__name}')
        lg.info(f'trying to access {__name} which does not exist')
        return 'default-value-for-non-existing-attributes'


def main():
    # Accessing attributes
    a = A(11)
    
    # access object itself
    lg.info('access object itself')
    lg.info(a)
    lg.info('-'*50)

    # access existing attribute via dot operator
    lg.info('access existing attribute via dot operator')
    lg.info(a.val)
    lg.info('-'*50)

    # access existing attribute via __dict__ subscript
    lg.info('access existing attribute via __dict__ subscript')
    lg.info(a.__dict__['val'])
    lg.info('-'*50)
    
    # access non-existing attribute
    lg.info('access non-existing attribute')
    lg.info(a.x)
    lg.info('-'*50)
    

main()