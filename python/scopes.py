"""
LEGB
local
enclosed
global
builtin
nonlocal
"""
from loguru import logger
# scope resolution

x = 0

def f1():
    global x
    logger.info('')

    x = 1

    def f2():
        logger.info('f2')
        nonlocal x  # write, not for read
        logger.info(x)
        x = 2
        logger.info(x)

    logger.info(x)
    f2()
    logger.info(x)

f1()

# read from global
x = 0
def func():
    logger.debug(x) # picks x from global
func()
logger.debug(x)

# read and write in presence of global
x = 0
def func():
    # logger.debug(x) # supposed to pick x from global but fails as x in next line makes it local
    # x = 1
    # logger.debug(x) # picks x from global

    # solution
    global x
    logger.debug(x)     # picks x from global
    x = 1               # updates global x
    logger.debug(x)     # picks x from global


func()
logger.debug(x)

# enclosed scope (non local)
x = 1
y = 10
def func():
    x = 2
    y = 20
    def outer_func():
        x = 3
        y = 30
        def enclosed_func():
            nonlocal x
            global y
            logger.debug(x)
            logger.debug(y)
            x = 4
            y = 40
            logger.debug(x)
            logger.debug(y)
        enclosed_func()
        logger.debug(x)
        logger.debug(y)
    outer_func()
    logger.debug(x)
    logger.debug(y)

func()
logger.debug(x)
logger.debug(y)
