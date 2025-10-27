# Reduce/Fold Function

## Exercise: Generic Reduce/Fold Function

Implement a generic `reduce` function that combines all elements of a list into a single accumulated value using a reducer function and an initial value. Use `Callable` for the reducer function.

**How Reduce Works:**
```
reduce([a, b, c], func, init) executes:
  step 1: result = func(init, a)
  step 2: result = func(result, b)
  step 3: result = func(result, c)
  return result
```

**Why This Matters:**
Reduce is one of the most powerful functional programming patterns. It can implement sum, product, concatenation, finding min/max, grouping, and countless other aggregations. A generic implementation works with any data types and any combining operation.

**Example Usage:**
```python
from typing import Callable

# Sum numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(numbers, lambda acc, x: acc + x, 0)
print(total)  # 15

# Product of numbers
product = reduce(numbers, lambda acc, x: acc * x, 1)
print(product)  # 120

# Concatenate strings
words = ["Hello", " ", "World", "!"]
sentence = reduce(words, lambda acc, word: acc + word, "")
print(sentence)  # "Hello World!"

# Count elements
count = reduce([1, 2, 3, 4, 5], lambda acc, _: acc + 1, 0)
print(count)  # 5

# Find maximum
numbers = [3, 7, 2, 9, 1, 5]
maximum = reduce(numbers, lambda acc, x: max(acc, x), float('-inf'))
print(maximum)  # 9

# Build a list in reverse (type transformation)
numbers = [1, 2, 3, 4]
reversed_list = reduce(numbers, lambda acc, x: [x] + acc, [])
print(reversed_list)  # [4, 3, 2, 1]

# Empty list returns initial value
result = reduce([], lambda acc, x: acc + x, 100)
print(result)  # 100

# Count word lengths (different input/output types)
words = ["cat", "elephant", "dog"]
total_length = reduce(words, lambda acc, word: acc + len(word), 0)
print(total_length)  # 11
```

**Advanced Example with Custom Types:**
```python
from dataclasses import dataclass

@dataclass
class Order:
    item: str
    price: float
    quantity: int

orders = [
    Order("Laptop", 999.99, 2),
    Order("Mouse", 25.50, 5),
    Order("Keyboard", 75.00, 3),
]

# Calculate total revenue
total_revenue = reduce(
    orders,
    lambda acc, order: acc + (order.price * order.quantity),
    0.0
)
print(f"Total: ${total_revenue:.2f}")  # Total: $2352.48

# Group orders by price range (transform to dictionary)
def group_by_price(acc: dict[str, list[Order]], order: Order) -> dict[str, list[Order]]:
    category = "expensive" if order.price > 100 else "affordable"
    if category not in acc:
        acc[category] = []
    acc[category].append(order)
    return acc

grouped = reduce(orders, group_by_price, {})
print(f"Expensive: {len(grouped['expensive'])}")  # Expensive: 1
print(f"Affordable: {len(grouped['affordable'])}")  # Affordable: 2

# Build summary string
summary = reduce(
    orders,
    lambda acc, order: acc + f"{order.quantity}x {order.item}, ",
    "Order: "
)
print(summary)  # Order: 2x Laptop, 5x Mouse, 3x Keyboard,
```

**More Practical Examples:**
```python
# Convert list of tuples to dictionary
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_result = reduce(
    pairs,
    lambda acc, pair: {**acc, pair[0]: pair[1]},
    {}
)
print(dict_result)  # {"a": 1, "b": 2, "c": 3}

# Flatten nested lists
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(nested, lambda acc, lst: acc + lst, [])
print(flat)  # [1, 2, 3, 4, 5, 6]

# Count occurrences
items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = reduce(
    items,
    lambda acc, item: {**acc, item: acc.get(item, 0) + 1},
    {}
)
print(counts)  # {"apple": 3, "banana": 2, "cherry": 1}
```

**Testing Requirements:**
Your implementation should pass tests that verify:
- Sums numbers correctly
- Calculates product correctly
- Concatenates strings correctly
- Returns initial value for empty lists
- Works with different input/output types (T ≠ U)
- Works with same input/output types (T = U)
- Handles custom objects
- Processes elements in correct order (left to right)
- Type hints correctly specify both type parameters
- Builds complex data structures (lists, dicts) as accumulators
- Handles transformation operations
