"""
In Python, "generic" often refers to the use of generics in typing to allow for more flexible and reusable code. Generics enable you to write functions, classes, or methods that can work with any data type while still maintaining type safety.

For example, you can use the TypeVar and Generic classes from the typing module to create generic types. Here’s a basic example:
"""

from typing import Generic, TypeVar

T = TypeVar('T', str, int, list[int])

class Box(Generic[T]):
  def __init__(self, value: T):
    self.value = value
  
  def get_value(self) -> T:
    return self.value
  

int_box = Box(12)
int_box.get_value()

ls_int_box = Box([1, 2, 3])
ls_int_box.get_value()