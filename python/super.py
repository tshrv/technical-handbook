"""
super()
super(SubClass, sub_class_instance) -> A proxy object representing the superclasses
super(...).attr -> Finds the <attr> from the MRO(C3 Linearization) of the proxy object
"""

from loguru import logger as lg


class A:
    def __init__(self, val, *args, **kwargs) -> None:
        self._val = val
    
    def get_val(self) -> None:
        lg.info(f'A.val {self._val}')


class A1:
    def __init__(self, val, *args, **kwargs) -> None:
        lg.debug(val)
        self._val = val
    
    def get_val(self) -> None:
        lg.info(f'A1.val {self._val}')


class B(A):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_val(self) -> None:
        lg.info(f'B.val {self._val}')
        super().get_val()


class C(A):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_val(self) -> None:
        lg.info(f'C.val {self._val}')
        super().get_val()

class E(A):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_val(self) -> None:
        lg.info(f'E.val {self._val}')
        super().get_val()

# +--------------------------------------------------------------------+
# | C3 Lineralization Algorithm for Method Resolution Order of a Class |
# +--------------------------------------------------------------------+
# 1. Children precede their parents
# 2. If a class inherits from multiple classes, they are kept in the order specified in the tuple of the base class.

# class D(B, C, E, A1):   # mro -> D B C E A A1 object
# class D(A1, B, C, E):   # mro -> D A1 B C E A object

# class D(A1, B, C, A, E):   # mro -> Cannot create a consistent method resolution order (MRO) for bases object, A, E
# reason: Child precedes it's parent but here, A precedes E, thus, inconsistent with C3 Linearization

# class D(B, C, A1, E):   # mro -> D B C A1 E A object
# reason: A is in last because even after C, E is there which is a subclass of A

class D(B, C, A1):   # mro -> D B C A A1 object

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_val(self) -> None:
        lg.info(f'D.val {self._val}')
        super().get_val()

def main():
    # simple class - no inheritance
    lg.info('Single Class - A')
    a = A(10)
    a.get_val()
    lg.info('-'*50)

    # -----------------------------------------------
    # simple inheritance
    lg.info('Simple inheritance - B')
    b = B(10)
    b.get_val()
    lg.info('-'*50)

    # -----------------------------------------------
    # multilevel inheritance
    lg.info('Multilevel inheritance - C')
    c = C(10)
    c.get_val()
    lg.info('-'*50)

    # -----------------------------------------------
    # multiple + multilevel inheritance
    lg.info('Multiple + Multilevel inheritance - D')
    d = D(10)
    d.get_val()
    lg.info('-'*50)
    lg.info(D.__mro__)

main()
