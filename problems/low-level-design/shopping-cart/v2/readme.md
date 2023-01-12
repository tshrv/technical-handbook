# Low Level Design - Shopping Cart
Design Shopping cart and write unit tests -
1. A shopping cart where it stores the items with their count. If the same item is added to the cart again, the count should be increased. End to end code is expected including valid exceptions and negative test scenarios as well.
2. Create a class and write following methods for adding item to the cart, remove item from cart, get number of items from cart and __repr__ for representing the cart data. Use dictionary to store the items with their count.
3. Write the testcases including the negative scenarios where it should raise ItemNotFoundException when user tries to remove the item which is not in the cart.
4. We are expected to run this code with all the testcases passed.

## Requirments
1. Add items to cart
   1. If item does not exist in cart, set item count 1.
   2. If item already exists in cart, increment item count by 1.
2. Remove items from cart
   1. If 1 or more units of the item is present in cart, remove all.
   2. If item not present in cart, raise ItemNotFoundException
3. Get cart data
   1. All items with their quantities
4. Get cart item count
   1. Return quantity count if item exists in cart
   2. Otherwise raise ItemNotFoundException

## Test Cases
- Add item
  1. Add existing item to cart
  2. Add non-existing item to cart
- Remove item
  1. Remove item from cart with item count greater than 1
  2. Remove item from cart with item count equal to 1
  3. Remove non-existing item from cart
- Cart item count
  1. Get count of existing item from cart
  2. Get count of non-existing item from cart
- Cart data