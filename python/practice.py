from typing import Any
from loguru import logger
log = logger.info

# getattribute, getattr, get

# class A:
#   def __setattr__(self, name: str, value: Any) -> None:
#     log(('__setattr__', name, value))
#     return super().__setattr__(name, value)

#   def __getattribute__(self, name: str) -> Any:
#     log(('__getattribute__', name))
#     return super().__getattribute__(name)

#   def __getattr__(self, name: str):
#     # name is not a direct attribute of current object
#     log(('__getattr__', name))
#     dc = {'y': 121}
#     return dc[name] if name in dc else None

# a = A()
# a.x = 10
# log(a.x)
# log(a.y)
# log(a.z)

# # Descriptors

# class Descriptor:
#   def __init__(self, name: str) -> None:
#     self.name = name

#   def __get__(self, instance, owner: type):
#     log(('__get__', instance, owner))
#     return instance.__dict__[self.name]

#   def __set__(self, instance, value):
#     log(('__set__', instance, value))
#     instance.__dict__[self.name] = value


# class User:
#   email = Descriptor('email')
#   def __init__(self, name: str, age:int, email: str) -> None:
#     self._name = name
#     self._age = age
#     self.email = email

#   @property
#   def name(self):
#     log(('name', 'pre-get ops'))
#     return self._name

#   @name.setter
#   def name(self, value):
#     log(('namesetter', 'pre-set ops', value))
#     self._name = value

#   @name.deleter
#   def name(self):
#     log(('namedeleter'))
#     del self._name

#   def age_setter(self, value):
#     log(('age', 'pre-set ops'))
#     self._age = value
  
#   def age_getter(self):
#     log(('age', 'pre-get ops'))
#     return self._age
  
#   age = property(age_getter, age_setter)

# usr = User("Tushar", 10, "hello@tusharsrivastava.com")
# usr2 = User("Sonali", 11, "hello2@tusharsrivastava.com")
# log(usr.name)
# usr.name = "TS"
# log(usr.name)
# log(usr.email)

# log(usr2.name)
# usr2.name = "SS"
# log(usr2.name)
# log(usr2.email)
# usr2.email = "email2@email.com"
# log(usr2.email)

# # usr.name = "Sonali"
# # log(usr.name)

# log(usr.age)
# usr.age=100
# log(usr.age)

# log(usr2.age)
# usr2.age=101
# log(usr2.age)

# del usr.name
# log(usr.name)


# OOPS

# static, instance and class methods

# class User:
#   species = 'Human'                         # class variable
#   def __init__(self, name: str) -> None:    # instance method
#     self.name = name                        # instance variable

#   @classmethod                              # class method
#   def detect_species(cls):
#     log(f'This is a class method - {cls.species}')

#   @staticmethod                             # static method
#   def belonging_function():
#     log('static method')

# u1 = User("Tushar")
# u2 = User("Sonali")
# u3 = User("Tanu")
# log((u1.species, u2.species))

# u2.species = "Neanderthals"

# log((u1.species, u2.species))

# # u1.detect_species()
# User.detect_species()
# User.belonging_function()

# new vs init

# class Store:
#   __instance = None
#   def __init__(self) -> None:
#     log('init pre-op')
#     log('init post-op')

#   def __new__(cls) -> 'Store':
#     log(f'new pre-op')
#     if cls.__instance is None:
#       cls.__instance = super().__new__(cls)
#     log('new post-op')
#     return cls.__instance

# s1 = Store()


# User = type('User', (object,), {
#   'a': 10
# })

# u1 = User()
# u2 = User()

# class SingletonMetaCls(type):
#   _instance = None

#   def __call__(cls, *args, **kwds):
#     if cls._instance is None:
#       cls._instance = super().__call__(*args, **kwds)
#     return cls._instance

# class Store(metaclass=SingletonMetaCls):
#   ...

# s1 = Store()
# s1.key = "142351"
# s2 = Store()

# class RegistryMetaCls(type):
#   registry = set()
#   def __call__(cls, *args, **kwargs):
#     log((cls, args, kwargs))
#     if cls not in RegistryMetaCls.registry:
#       RegistryMetaCls.registry.add(cls)
#     return super().__call__(*args, **kwargs)

# # class SQLSource(metaclass=RegistryMetaCls):
# #   ...

# # class NoSQLSource(metaclass=RegistryMetaCls):
# #   ...

# SQLSource = RegistryMetaCls('SQLSource', (object,), {})
# NoSQLSource = RegistryMetaCls('NoSQLSource', (object,), {})

# SQLSource()
# NoSQLSource()


# class User:
#   def __init__(self, name: str) -> None:
#     self.name = name
#     self.is_employed = False
  
#   def info(self):
#     log((self.name, self.is_employed))

#   def __enter__(self, *args, **kwargs):
#     log(('__enter__', args, kwargs))
#     self.is_employed = True
#     return self

#   def __exit__(self, exc_type, exc_value, exc_traceback):
#     log(('__exit__', exc_type, exc_value, exc_traceback))
#     self.is_employed = False

# usr = User("Tushar")
# usr.info()
# with usr as u:
#   u.info()
#   raise Exception('Manual error')
# usr.info()


# from contextlib import contextmanager

# @contextmanager
# def employ_user(name):
#   usr = User(name)
#   usr.info()
#   try:
#     usr.is_employed = True
#     yield usr
#   finally:
#     usr.is_employed = False

# with employ_user('Tushar') as u:
#   u.info()
# u.info()

class A:
  def __init__(self, val) -> None:
    log(f'A.__init__')
    self.val = val

  def show(self) -> None:
    log(f'A.show {self.val}')

class B(A):
  def __init__(self, val) -> None:
    log(f'B.__init__')
    super().__init__(val)
  
  def show(self) -> None:
    log(f'B.show')
    super().show()

class C(A):
  def __init__(self, val) -> None:
    log(f'C.__init__')
    super().__init__(val)
  
  def show(self) -> None:
    log(f'C.show')
    super().show()

class D(B, C):
  def __init__(self, val) -> None:
    log(f'D.__init__')
    super().__init__(val)
  
  def show(self) -> None:
    log(f'D.show')
    super().show()


log('No inheritance')
ob = A(11)
ob.show()

log('Simple inheritance')
ob = B(12)
ob.show()

log('Simple inheritance')
ob = C(13)
ob.show()

log('Multiple and multi-level inheritance')
ob = D(14)
ob.show()
log(D.__mro__)