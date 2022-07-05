"""
Generators, an extension on iterators
When a function that has a yield statement is called, it returns a generator.
This generator is not callable but it can be iterated over just like an iterable.
On top of it, it implements send and throw methods that allow two-way communication, it somewhat maintains a state
We cannot send a value to a just started generator but when atleast one time called, we can send values as well as exceptions
Similar to iterators, it also stops with a StopIteration error, and also can be explicitly closed by x.close()
"""

from loguru import logger as lg

def func():
    return True

def f1():
    try:
        x = yield 1
        lg.info(f'received {x}')
        x = yield x+10
        lg.info(f'received {x}')
        x = yield x+20
        lg.info(f'received {x}')
    except ValueError as e:
        lg.error(e)
        x = yield -1
    except Exception as e:
        lg.error(e)
        x = yield 4
    finally:
        yield False

x = f1()
x.send(None)
x.send(True)    # or any value
x.throw(Exception, 'intentionally raised exception')
