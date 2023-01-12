"""
Shopping Cart
"""

from abc import ABC, abstractmethod

class AbstractCart(ABC):
    def add_item(self):
        raise NotImplementedError
    
    def remove_item(self):
        raise NotImplementedError
    
    def get_details(self):
        raise NotImplementedError
    
    def get_item_count(self):
        raise NotImplementedError

class ShoppingCart(AbstractCart):
    def __init__(self) -> None:
        super().__init__()
        self.__data = dict()
        # __data => {item_id_1: int, item_id_2: int, ...}
    
    def __exists(self, item_id: str):
        return item_id in self.__data
    
    def get_item_count(self, item_id: str):
        if not self.__exists(item_id):
            raise LookupError(f'item with id {item_id} does not exist in the cart')
        return self.__data[item_id]

    def add_item(self, item_id: str):
        """
        add item if does not exist else increment item count by 1
        """
        if self.__exists(item_id):
            self.__data[item_id] += 1
        else:
            self.__data[item_id] = 1


