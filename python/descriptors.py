class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # ---- property getter and setter w/ decorators ----
    # @property def x: ...
    # @x.setter def x: ...
    # @x.deleter def x: ...

    # @property
    # def user_name(self) -> str:
    #     return self.name
    
    # # @user_name.setter
    # # def user_name(self, value) -> None:
    # #     self.name = value
    
    # @user_name.setter
    # def user_name(self, value) -> None:
    #     raise AttributeError('cannot update value')


    # ---- property getter and setter w/o decorators ----    
    # property(fget, fset, fdel)
    
    def user_name_getter(self) -> str:
        return self.name
    
    # def user_name_setter(self, value: str) -> None:
    #     self.name = value
    
    def user_name_setter(self, value: str) -> None:
        raise AttributeError('Cannot update value')
    
    user_name = property(user_name_getter, user_name_setter)


user = User('Tushar', 26)
print(user)
print(vars(user))

print('Accessing user_name')
print(user.user_name)

print('Setting user_name')
user.user_name = user.user_name.lower()

print('Accessing user_name')
print(user.user_name)

