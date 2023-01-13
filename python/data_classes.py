"""
Classes
1. Data container
2. Behaviour container

Data containing classes
Order, compare, other data point oriented tasks
"""

from loguru import logger
from dataclasses import dataclass, field

# without dataclasses
class Person:
    name: str
    job: str
    age: int

    def __init__(self, name: str, job: str, age: int) -> None:
        self.name = name
        self.job = job
        self.age = age

person_1 = Person('Ethan Kenway', 'Assassin', 28)
person_2 = Person('Charles Darwin', 'Author', 72)
person_3 = Person('Charles Darwin', 'Author', 72)

logger.debug(id(person_2))  # id2
logger.debug(id(person_3))  # id3
logger.debug(person_1)      # <__main__.Person object at 0x7f1a3675f700>
logger.debug(person_2 == person_3)  # False, even though both have same data


@dataclass(order=True, frozen=True)
class Person:
    name: str
    job: str
    age: int
    strength: int = 100                                     # default value
    sort_index: int = field(init=False, repr=False)

    def __post_init__(self) -> None:
        # self.sort_index = self.age                        # fails for frozen dataclass
        # setattr(self, 'sort_index', self.age)             # fails for frozen dataclass
        object.__setattr__(
            self, 
            'sort_index',
            self.strength
        )   # way around for frozen dataclass
    
    def __str__(self) -> str:
        return f'{self.name}, {self.job}({self.age}) - [{self.strength}]'
    
person_1 = Person('Ethan Kenway', 'Assassin', 28)
person_2 = Person('Charles Darwin', 'Author', 72, 98)
person_3 = Person('Charles Darwin', 'Author', 72, strength=98)

# person_1.age = 72     # fails for frozen set

logger.debug(id(person_2))  # id2
logger.debug(id(person_3))  # id3
logger.debug(person_1)      # Person(name='Ethan Kenway', job='Assassin', age=28)
logger.debug(person_2 == person_3)  # True, as both have same data
logger.debug(person_2 > person_1)   # works when ordering is enabled