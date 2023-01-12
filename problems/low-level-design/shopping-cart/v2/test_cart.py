"""
Testing Shopping Cart
"""
import pytest
from loguru import logger
from cart import ShoppingCart, ItemNotFoundException
from copy import deepcopy

@pytest.fixture
def cart_data():
    data = {
        # item_id: item_count
        '101': 2,
        '100':3,
        '102':1
    }
    yield data

@pytest.fixture
def shopping_cart(cart_data: dict):
    cart = ShoppingCart(deepcopy(cart_data))
    yield cart


class TestShoppingCart:
    @pytest.mark.parametrize(
        ('item_id', 'item_quantity', 'expected_item_quantity'),
        (('101', 2, 4), ('101', None, 3), ('103', None, 1), ('103', 2, 2)))
    def test_add_item(self, shopping_cart: ShoppingCart,
        item_id: str, item_quantity: int, expected_item_quantity: int) -> None:
        """
        """
        new_item_qty = shopping_cart.add_item(item_id, item_quantity)
        assert new_item_qty == expected_item_quantity
    
    @pytest.mark.parametrize(('item_id',), (('100',), ('102',)))
    def test_remove_item_existing(self, shopping_cart: ShoppingCart, item_id: str) -> None:
        """
        """
        shopping_cart.remove_item(item_id)
        with pytest.raises(ItemNotFoundException):
            shopping_cart.get_item_count(item_id)

    @pytest.mark.parametrize(('item_id',), (('103',),))
    def test_remove_item_non_existing(self, shopping_cart: ShoppingCart, item_id: str) -> None:
        """
        """
        with pytest.raises(ItemNotFoundException):
            shopping_cart.remove_item(item_id)

    @pytest.mark.parametrize(('item_id', 'expected_count'), (('101', 2),))
    def test_item_count_existing(self, shopping_cart: ShoppingCart, 
        item_id: str, expected_count: int) -> None:
        """
        """
        item_count = shopping_cart.get_item_count(item_id)
        assert item_count == expected_count
    
    @pytest.mark.parametrize(('item_id',), (('103',),))
    def test_item_count_non_existing(self, shopping_cart: ShoppingCart, 
        item_id: str) -> None:
        """
        """
        with pytest.raises(ItemNotFoundException):
            item_count = shopping_cart.get_item_count(item_id)
        