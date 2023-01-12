import pytest
from main import ShoppingCart

class TestShoppingCart:
    def test_add_item(self):
        cart = ShoppingCart()
        item_id = 'usha-heater'
        cart.add_item(item_id)
        item_count = cart.get_item_count(item_id)
        assert item_count == 1

        cart.add_item(item_id)
        item_count = cart.get_item_count(item_id)
        assert item_count == 2
    