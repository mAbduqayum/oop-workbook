# Map/Transform Function

## Exercise: Generic Map/Transform Function

Implement a generic `map_transform` function that applies a transformation function to each element of a list, returning a new list. The function should work with `Callable` and handle type transformations (input type may differ from output type).

**Why This Matters:**
Map/transform is one of the most fundamental functional programming patterns. A generic implementation enables type-safe transformations between any two types, making it versatile and reusable across many scenarios.

**Example Usage:**
```python
from typing import Callable

# Transform integers to strings
numbers = [1, 2, 3, 4, 5]
strings = map_transform(numbers, str)
print(strings)  # ["1", "2", "3", "4", "5"]

# Transform strings to their lengths
words = ["hello", "world", "python"]
lengths = map_transform(words, len)
print(lengths)  # [5, 5, 6]

# Transform with custom function
def square(x: int) -> int:
    return x * x

squared = map_transform([1, 2, 3, 4], square)
print(squared)  # [1, 4, 9, 16]

# Transform with lambda
upper = map_transform(["a", "b", "c"], lambda s: s.upper())
print(upper)  # ["A", "B", "C"]

# Chain transformations
numbers = [1, 2, 3]
strings = map_transform(numbers, str)          # [int] -> [str]
lengths = map_transform(strings, len)          # [str] -> [int]
doubled = map_transform(lengths, lambda x: x * 2)  # [int] -> [int]
print(doubled)  # [2, 2, 2]

# Empty list
empty: list[int] = []
result = map_transform(empty, str)
print(result)  # []

# Type safety is preserved
ints: list[int] = [1, 2, 3]
strs: list[str] = map_transform(ints, str)  # Type checker knows result is list[str]
```

**Advanced Example with Custom Types:**
```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

@dataclass
class PersonSummary:
    info: str

people = [
    Person("Alice", 30),
    Person("Bob", 25),
]

def summarize(p: Person) -> PersonSummary:
    return PersonSummary(f"{p.name} ({p.age})")

summaries = map_transform(people, summarize)
# Type: list[PersonSummary]
```

**Testing Requirements:**
Your implementation should pass tests that verify:
- Transforms integers to strings correctly
- Transforms strings to integers correctly
- Transforms with custom functions
- Transforms with lambda functions
- Handles empty lists
- Preserves order of elements
- Type hints are correctly specified with multiple type parameters
- Works with complex transformations between custom types
