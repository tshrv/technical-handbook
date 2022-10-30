"""
add(a: int, b: int)
add(a: int, b: int, c: int)
Not possible to achieve this way

Either modify code and go with *args and **kwargs to identify input params and execute accordingly
Or, use dispatch decorator from mutipledispatch package
"""
from loguru import logger

from multipledispatch import dispatch

@dispatch(int, int)
def add(a: int, b: int):
    return a + b

@dispatch(int, int, int)
def add(a: int, b: int, c: int):
    return a + b + c

logger.debug(add(1, 2))
logger.debug(add(1, 2, 3))
# logger.debug(add(1.1, 2.2, 3.1))    # error since method with such signature not implemented
