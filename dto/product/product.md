# Product - Pydantic Field Constraints

## Exercise: Product Model with Advanced Constraints

Create a `Product` class using Pydantic with field constraints and pattern validation.

**Task:**
Create a `Product` class using `BaseModel` with the following fields:

- `id: UUID` - Product ID (UUID v4)
- `name: str` - Product name (1-50 characters)
- `price: float` - Product price (must be > 0, multiple of 0.01)
- `quantity: int` - Stock quantity (must be >= 0)
- `categories: list[Category]` - List of product categories (nested models from Category exercise)

**Example:**

```python
from uuid import uuid4

# Create categories
electronics = Category(id=1, name="Electronics")
computers = Category(id=2, name="Computers")

# Create product with categories
product = Product(
    id=uuid4(),
    name="Laptop",
    price=999.99,
    quantity=10,
    categories=[electronics, computers]
)
print(product.categories[0].name)  # Electronics
print(len(product.categories))  # 2

# Can also pass categories as dicts
product2 = Product(
    id=uuid4(),
    name="Mouse",
    price=29.99,
    quantity=5,
    categories=[{"id": 3, "name": "Accessories"}, {"id": 1, "name": "Electronics"}]
)
print(product2.name)  # Mouse
print(product2.categories[0].id)  # 3

# Serialization includes nested categories
data = product.model_dump()
print(data['categories'][0]['name'])  # Electronics

# Invalid data raises ValidationError
Product(id=uuid4(), name="", price=999.99, quantity=10, categories=[electronics])  # ValidationError (empty name)
Product(id=uuid4(), name="Laptop", price=-10, quantity=10,
        categories=[electronics])  # ValidationError (negative price)
```
