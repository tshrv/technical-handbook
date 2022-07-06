from loguru import logger as lg

class User:
    def __new__(cls, *args, **kwargs) -> 'User':
        return super().__new__(*args, **kwargs)
    
    def __init__(self, name) -> None:
        self.name = name


u = User('Tushar')
print(u.__dict__)


x = 0


# scope resolution
def f1():
    global x
    lg.info('')

    x = 1
    
    def f2():
        lg.info('f2')
        nonlocal x  # write, not for read
        lg.info(x)
        x = 2
        lg.info(x)
    
    lg.info(x)
    f2()
    lg.info(x)

f1()