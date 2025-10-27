# Generic Filter

## Exercise: Generic Filter Function

Implement a generic `filter_items` function that returns a new list containing only elements matching a predicate. Use `Callable` for the predicate function.

**Why This Matters:**
Filtering is one of the core operations in functional programming and data processing. A generic implementation enables filtering any collection type with any condition, making code more reusable and maintainable.

**Example Usage:**
```python
from typing import Callable

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter_items(numbers, lambda x: x % 2 == 0)
print(evens)  # [2, 4, 6, 8, 10]

# Filter odd numbers
odds = filter_items(numbers, lambda x: x % 2 != 0)
print(odds)  # [1, 3, 5, 7, 9]

# Filter strings by length
words = ["cat", "elephant", "dog", "tiger", "ant"]
long_words = filter_items(words, lambda w: len(w) > 3)
print(long_words)  # ["elephant", "tiger"]

# Filter with custom function
def is_positive(n: int) -> bool:
    return n > 0

positives = filter_items([-5, -2, 0, 3, 7, -1], is_positive)
print(positives)  # [3, 7]

# No matches
result = filter_items([1, 3, 5, 7], lambda x: x % 2 == 0)
print(result)  # []

# All match
result = filter_items([2, 4, 6], lambda x: x % 2 == 0)
print(result)  # [2, 4, 6]

# Empty input
result = filter_items([], lambda x: True)
print(result)  # []

# Filter strings starting with specific letter
words = ["apple", "banana", "apricot", "cherry", "avocado"]
a_words = filter_items(words, lambda w: w.startswith('a'))
print(a_words)  # ["apple", "apricot", "avocado"]

# Type safety is preserved
numbers: list[int] = [1, 2, 3, 4, 5]
filtered: list[int] = filter_items(numbers, lambda x: x > 2)
# Type checker knows filtered is list[int]
```

**Advanced Example with Custom Types:**
```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool

products = [
    Product("Laptop", 999.99, True),
    Product("Mouse", 25.50, False),
    Product("Keyboard", 75.00, True),
    Product("Monitor", 299.99, True),
    Product("Webcam", 49.99, False),
]

# Filter in-stock products
available = filter_items(products, lambda p: p.in_stock)
print(len(available))  # 3

# Filter expensive products
expensive = filter_items(products, lambda p: p.price > 100)
print([p.name for p in expensive])  # ["Laptop", "Monitor"]

# Filter affordable in-stock items
affordable_available = filter_items(
    products,
    lambda p: p.in_stock and p.price < 100
)
print([p.name for p in affordable_available])  # ["Keyboard"]

# Chain with map (filter then transform)
in_stock_names = [p.name for p in filter_items(products, lambda p: p.in_stock)]
print(in_stock_names)  # ["Laptop", "Keyboard", "Monitor"]
```

**Testing Requirements:**
Your implementation should pass tests that verify:
- Filters elements correctly based on predicate
- Returns empty list when no matches found
- Returns all elements when all match
- Returns empty list for empty input
- Works with integer predicates
- Works with string predicates
- Works with custom object predicates
- Preserves order of filtered elements
- Type hints are correctly specified
- Does not modify the original list
- Handles complex predicates with multiple conditions
