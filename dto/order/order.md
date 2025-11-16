# Order - Computed Fields and Aggregation

## Exercise: Order System with Nested Models and Calculations

Create `OrderItem` and `Order` classes using Pydantic's `BaseModel` with computed fields and aggregations.

**Task:**

1. Create an `OrderItem` class using `BaseModel` with the following fields:
    - `product: Product` - Product from the Product exercise
    - `quantity: int` - Quantity ordered (must be >= 1)
2. Add a `subtotal` property that calculates `product.price * quantity`
3. Create an `Order` class using `BaseModel` with the following fields:
    - `id: UUID` - Order ID (UUID v4)
    - `customer: User` - Customer from the User exercise
    - `items: list[OrderItem]` - List of order items (must have at least 1 item)
    - `status` - Order status, must be one of: "pending", "processing", "shipped", "delivered" (default: "pending")
4. Add a `total` property that sums all item subtotals
5. Add an `item_count` property that returns total number of items

**Example:**

```python
from pydantic import BaseModel
from typing import Literal
from uuid import UUID, uuid4

# From previous exercises
class Category(BaseModel):
    id: int
    name: str

class Product(BaseModel):
    id: UUID
    name: str
    price: float
    quantity: int
    categories: list[Category]

class User(BaseModel):
    id: UUID
    username: str
    email: str
    age: int
    is_active: bool = True

# Create products
laptop = Product(
    id=uuid4(),
    name="Laptop",
    price=999.99,
    quantity=10,
    categories=[Category(id=1, name="Electronics")]
)

mouse = Product(
    id=uuid4(),
    name="Mouse",
    price=29.99,
    quantity=50,
    categories=[Category(id=1, name="Electronics")]
)

# Create order items
item1 = OrderItem(product=laptop, quantity=2)
item2 = OrderItem(product=mouse, quantity=3)

print(item1.subtotal)  # 1999.98
print(item2.subtotal)  # 89.97

# Create customer
customer = User(
    id=uuid4(),
    username="john_doe",
    email="john@example.com",
    age=25
)

# Create order
order = Order(
    id=uuid4(),
    customer=customer,
    items=[item1, item2]
)

print(order.total)  # 2089.95
print(order.item_count)  # 5
print(order.status)  # pending

# Empty items list raises ValidationError
Order(id=uuid4(), customer=customer, items=[])  # ValidationError

# Invalid quantity raises ValidationError
OrderItem(product=laptop, quantity=0)  # ValidationError
```
