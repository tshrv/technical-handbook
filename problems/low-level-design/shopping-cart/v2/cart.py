"""
Shopping Cart
"""

from abc import ABC, abstractmethod

class ItemNotFoundException(Exception):
    """
    Signifies that the required item does not exist 
    """
    pass

class AbstractShoppingCart(ABC):
    
    @abstractmethod
    def add_item(self, item_id) -> int:
        ...
    
    @abstractmethod
    def remove_item(self, item_id) -> int:
        ...
    
    @abstractmethod
    def get_item_count(self, item_id) -> int:
        ...

class ShoppingCart(AbstractShoppingCart):
    def __init__(self, cart_data: dict) -> None:
        super().__init__()
        self.data = cart_data

    def __exists(self, item_id: str) -> bool:
        """
        check whether or not item_id exists in the cart
        """
        return item_id in self.data

    def __item_qty(self, item_id: str) -> int:
        if not self.__exists(item_id):
            raise ItemNotFoundException
        return self.data[item_id]

    def add_item(self, item_id: str, item_quantity: int=1) -> int:
        item_quantity = item_quantity or 1
        try:
            current_qty = self.__item_qty(item_id)
        except ItemNotFoundException:
            current_qty = 0

        self.data[item_id] = current_qty + item_quantity
        return self.__item_qty(item_id)
 
    def remove_item(self, item_id: str) -> int:
        if not self.__exists(item_id):
            raise ItemNotFoundException
        self.data.pop(item_id)
    
    def get_item_count(self, item_id: str) -> int:
        return self.__item_qty(item_id)

    def __repr__(self) -> str:
        rep = ''
        for ind, (item_id, item_count) in enumerate(self.data.items()):
            rep += f'#{ind} | ITEM_ID {item_id} | QTY {item_count}'
            rep += '\n'
        return rep
    
# cart_data = {101: 2, 100:3, 102:1}
# sc = ShoppingCart(cart_data)
# print(sc)