# PaginatedResponse - Generic Types with Modern Syntax

## Exercise: Generic Paginated Response Model

Create a generic `PaginatedResponse` class using Pydantic's `BaseModel` with modern generic syntax (PEP 695) to handle
paginated API responses.

**Task:**

1. Create a generic `PaginatedResponse[T]` class using modern generic syntax with the following fields:
    - `items: list[T]` - List of items for the current page
    - `total: int` - Total number of items across all pages (must be >= 0)
    - `page: int` - Current page number (must be >= 1)
    - `page_size: int` - Number of items per page (must be >= 1)
2. Implement a `total_pages` property that calculates the total number of pages
3. Implement a `has_next` property that indicates if there's a next page

**Example:**

```python
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float


products = [
    Product(id=1, name="Laptop", price=999.99),
    Product(id=2, name="Mouse", price=29.99),
]

response = PaginatedResponse[Product](
    items=products,
    total=10,
    page=1,
    page_size=2
)

print(response.total_pages)  # 5
print(response.has_next)  # True
```
