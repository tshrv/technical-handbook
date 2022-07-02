"""
decorator -> a function `d` that takes another function `f` as an argument and returns a wrapper `w`(a function)
on `f`
This wrapper can extend the behaviour of `f`, including pre-processing and post-processing
"""

from django.db import OperationalError
from loguru import logger as lg

def function_based_decorator_d(func, flag=True):
    if not flag:
        raise OperationalError('cannot decorate function')
    lg.info('decorating function')
    def wrapper_w(*args, **kwargs):
        lg.info('extended features through wrapper')
        rsp = func(*args, **kwargs)
        return rsp
    return wrapper_w

def decorator_generator(flag):
    if not flag:
        raise OperationalError('cannot build the decorator')
    else:
        lg.info('generating decorator')

    # same as above
    def function_based_decorator_d(func):
        if not flag:
            raise OperationalError('cannot decorate function')
        lg.info('decorating function')
        def wrapper_w(*args, **kwargs):
            lg.info('extended features through wrapper')
            rsp = func(*args, **kwargs)
            return rsp
        return wrapper_w

    return function_based_decorator_d

def function_f(*args):
    lg.info(f'primary call with args {args}')

@function_based_decorator_d
def decorated_function_f(*args):
    lg.info(f'primary call with args {args}')

@decorator_generator(True)
# @decorator_generator(False)
def function_f1(*args):
    lg.info(f'primary call with args {args}')

def function_f2(*args):
    lg.info(f'primary call with args {args}')

def main():
    # without decorator
    lg.info('without decorator')
    function_f('argument')
    lg.info('-'*50)

    # function based decorator
    lg.info('function based decorator')
    args = ('argument',)
    decorated_f = function_based_decorator_d(function_f, flag=True)
    decorated_f(*args)
    lg.info('-'*50)
    
    # decorated function
    lg.info('decorated function')
    args = ('argument',)
    decorated_function_f(*args)
    lg.info('-'*50)

    # decorated function though decorator generator with args
    lg.info('decorated function though decorator generator with args')
    args = ('argument',)
    function_f1(*args)
    lg.info('-'*50)

    # decorated function though decorator generator with args using function call
    lg.info('decorated function though decorator generator with args using function call')
    args = ('argument',)
    decorated_function_f2 = decorator_generator(True)(function_f2)
    # decorated_function_f2 = decorator_generator(False)(function_f2)
    decorated_function_f2()
    lg.info('-'*50)

main()
