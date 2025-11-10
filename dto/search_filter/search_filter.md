# SearchFilter - Query Parameters with Optional Fields

## Exercise: SearchFilter Model for API Queries

Create a `SearchFilter` class using Pydantic's `BaseModel` with all optional fields for flexible search queries.

**Task:**

1. Create a `SearchFilter` class using `BaseModel` with the following optional fields:
    - `query: str | None` - Search query text (default: None)
    - `min_price: float | None` - Minimum price filter (must be > 0, multiple of 0.01, default: None)
    - `max_price: float | None` - Maximum price filter (must be > 0, multiple of 0.01, default: None)
    - `categories: list[str] | None` - Category filters (default: None)
    - `in_stock: bool | None` - Filter by stock availability (default: None)
    - `sort_by: Literal["price", "name", "date"] | None` - Sort field (default: None)
    - `sort_order: Literal["asc", "desc"] | None` - Sort direction (default: None)
2. Add a model validator to ensure `min_price` <= `max_price` when both are provided
3. Add a `has_filters` property that returns True if any filter is set
4. Add a `to_query_params()` method that returns a dict of non-None values

**Example:**

```python
from typing import Literal

# Empty filter (no filters applied)
filter1 = SearchFilter()
print(filter1.has_filters)  # False
print(filter1.to_query_params())  # {}

# Price range filter
filter2 = SearchFilter(min_price=10.0, max_price=100.0)
print(filter2.has_filters)  # True
print(filter2.to_query_params())  # {'min_price': 10.0, 'max_price': 100.0}

# Complex filter
filter3 = SearchFilter(
    query="laptop",
    min_price=500.0,
    max_price=2000.0,
    categories=["Electronics", "Computers"],
    in_stock=True,
    sort_by="price",
    sort_order="asc"
)
print(filter3.has_filters)  # True
print(filter3.query)  # laptop
print(len(filter3.categories))  # 2

params = filter3.to_query_params()
print(params['query'])  # laptop
print(params['sort_by'])  # price

# Invalid price range raises ValidationError
SearchFilter(min_price=100.0, max_price=50.0)  # ValidationError

# Zero or negative price raises ValidationError
SearchFilter(min_price=0.0)  # ValidationError
SearchFilter(min_price=-10.0)  # ValidationError
```
