"""
decorator -> a function `d` that takes another function `f` as an argument and returns a wrapper `w`(a function)
on `f`
This wrapper can extend the behaviour of `f`, including pre-processing and post-processing
"""

from typing import Any
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


# class based decorators

class Decorator:
    def __init__(self, func, *args) -> None:
        lg.info('initializing decorator')
        lg.info(f'func: {func}')
        lg.info(f'args: {args}')
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        # __call__ acts as a wrapper for the decorated function
        lg.info('extended features through __call__ wrapper')
        rsp = self.func(*args, **kwds)
        return rsp

class DecoratorGenerator:
    def __new__(cls, *args, **kwargs):
        return cls.__call__(*args, **kwargs)
    
    @classmethod
    def __call__(cls, *dargs: Any, **dkwds: Any) -> Any:
        # Decorator behaviour can be based on these arguments
        # args and kwds
        lg.info(f'{dargs}, {dkwds}')

        class Decorator:
            def __init__(self, func, *args) -> None:
                lg.info('initializing decorator')
                lg.info(f'func: {func}')
                lg.info(f'args: {args}')
                self.func = func

            def __call__(self, *args: Any, **kwds: Any) -> Any:
                # decorator behaviour params
                lg.info(f'dargs {dargs}')
                lg.info(f'dkwds {dkwds}')

                # __call__ acts as a wrapper for the decorated function
                lg.info('extended features through __call__ wrapper')
                rsp = self.func(*args, **kwds)
                return rsp
        return Decorator

def class_function_f1(*args):
    lg.info(f'primary call with args {args}')

@Decorator
def class_function_f2(*args):
    lg.info(f'primary call with args {args}')

@DecoratorGenerator(flag=True, foo='bar')
def class_function_f3(*args):
    lg.info(f'primary call with args {args}')

# execution ground
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


    # +------------------------+
    # | Class based decorators |
    # +------------------------+

    # class based decorator w/ instantiation
    lg.info('class based decorator w/ instantiation')
    class_decorated_function_f = Decorator(class_function_f1, True)
    args = ('argument',)
    class_decorated_function_f(*args)
    lg.info('-'*50)

    # callable POC
    lg.info('callable POC')
    class_function_f1('standard')
    class_function_f1.__call__('via __call__')
    lg.info(callable(class_function_f1))    # True, implicitly implements __call__
    lg.info(callable(Decorator))            # True, we explicitly implemented __call__
    class A: pass
    lg.info(callable(A))                    # True, implicitly implemented __call__ is used while instantiation
    lg.info(callable(A()))                  # False, instance does not have __call__
    lg.info('-'*50)

    # class based decorator w/o instantiation
    lg.info('class based decorator w/o instantiation')
    args = ('argument',)
    class_function_f2(*args)
    lg.info('-'*50)

    # decoration via class based decorator generator
    lg.info('decoration via class based decorator generator')
    args = ('argument',)
    class_function_f3(*args)
    lg.info('-'*50)


main()


from functools import partial


# pow x, n
pow
sq = partial(pow, exp=2)

