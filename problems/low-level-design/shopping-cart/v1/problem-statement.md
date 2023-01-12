# Low Level Design - Shopping Cart

## Problem Statement
Design Shopping cart and write unit tests -
- A shopping cart where it stores the items with their count. If the same item is added to the cart again, the count should be increased. End to end code is expected including valid exceptions and negative test scenarios as well.
- Create a class and write following methods for adding item to the cart, remove item from cart, get number of items from cart and __repr__ for representing the cart data. Use dictionary to store the items with their count.
- Write the testcases including the negative scenarios where it should raise ItemNotFoundException when user tries to remove the item which is not in the cart.
- We are expected to run this code with all the testcases passed.

---

## Solution Building

### Shopping Cart Functionalities
- Stores items with count
- Add item
    - Increment count if already exists
- Remove item
    - Raise exception if does not exist
- Get cart data
    - Items with count
- Get item count
    - Count of that item

### Test cases
- Add item to cart
- Add non-existing item to cart
- Remove existing item from cart
- Remove non-existing item from cart
- Get cart data
- Get item count