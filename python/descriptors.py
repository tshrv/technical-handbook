from loguru import logger as lg


class EmailDescriptor:
    def __init__(self, value=None) -> None:
        self._value = value
    
    def __get__(self, obj, objtype):
        lg.debug('pre-get operations')
        return self._value
    
    def __set__(self, obj, email):
        lg.debug('pre-set operations')
        self._value = email
    
    
class User:
    # class based descriptor
    email = EmailDescriptor()

    def __init__(self, name: str, age: int, email: str) -> None:
        self._name = name
        self._age = age

        # class based descriptor
        self.email = email
        # self.email = EmailDescriptor(value=email) # does not work this way

    # ---- property getter and setter w/ decorators ----
    # @property def age: ...
    # @age.setter def age: ...
    # @age.deleter def age: ...

    @property
    def age(self) -> int:
        lg.debug('pre-get checks')
        return self._age
    
    @age.setter
    def age(self, value) -> None:
        lg.debug('pre-set checks')
        if not isinstance(value, int):
            raise ValueError(f'age should be of type {int} not {type(value)}')
        self._age = value

    # ---- property getter and setter w/o decorators ----    
    # property(fget, fset, fdel)
    
    def name_getter(self) -> str:
        lg.debug('pre-get checks')
        return self._name
    
    def name_setter(self, value: str) -> None:
        lg.debug('pre-set checks')
        self._name = value
        
    name = property(name_getter, name_setter)


user = User('Tushar', 26, 'foo@bar.com')
lg.debug(user)
lg.debug(vars(user))

lg.debug('Access')
lg.debug((user.name, user.age, user.email))

lg.debug('Update')
user.name = user.name.lower()
user.age = user.age + 1
user.email = 'foo+1@bar.com'

lg.debug('Access')
lg.debug((user.name, user.age, user.email))
