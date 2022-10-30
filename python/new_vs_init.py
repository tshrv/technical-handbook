from loguru import logger as lg

class User:
    def __new__(cls, *args, **kwargs) -> 'User':
        return super().__new__(*args, **kwargs)
    
    def __init__(self, name) -> None:
        self.name = name


u = User('Tushar')
print(u.__dict__)
