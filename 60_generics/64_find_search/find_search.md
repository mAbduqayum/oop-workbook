# Find/Search with Predicate

## Exercise: Generic Find Function with Predicate

Implement a generic `find` function that searches a list and returns the first element matching a predicate, or `None` if no match is found. Use `Callable` for the predicate function.

**Why This Matters:**
Finding elements by condition is a fundamental operation in programming. A generic implementation works with any data type and any condition, making it extremely reusable for searching collections.

**Example Usage:**
```python
from typing import Callable

# Find first even number
numbers = [1, 3, 5, 6, 8, 9]
first_even = find(numbers, lambda x: x % 2 == 0)
print(first_even)  # 6

# Find first string longer than 5 characters
words = ["cat", "dog", "elephant", "tiger", "mouse"]
long_word = find(words, lambda w: len(w) > 5)
print(long_word)  # "elephant"

# Find with custom predicate function
def is_positive(n: int) -> bool:
    return n > 0

result = find([-5, -2, 0, 3, 7], is_positive)
print(result)  # 3

# No match found
result = find([1, 3, 5, 7], lambda x: x % 2 == 0)
print(result)  # None

# Empty list
result = find([], lambda x: True)
print(result)  # None

# Find first string starting with 'p'
words = ["apple", "banana", "pear", "plum"]
p_word = find(words, lambda w: w.startswith('p'))
print(p_word)  # "pear"

# Type safety is maintained
numbers = [1, 2, 3, 4, 5]
found: int | None = find(numbers, lambda x: x > 3)
if found is not None:
    print(f"Found: {found}")  # Found: 4
```

**Advanced Example with Custom Types:**
```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    active: bool

users = [
    User("Alice", 30, False),
    User("Bob", 25, True),
    User("Charlie", 35, True),
]

# Find first active user
active_user = find(users, lambda u: u.active)
print(active_user)  # User(name='Bob', age=25, active=True)

# Find user by name
bob = find(users, lambda u: u.name == "Bob")
print(bob)  # User(name='Bob', age=25, active=True)

# Find user over 30
senior = find(users, lambda u: u.age > 30)
print(senior)  # User(name='Charlie', age=35, active=True)

# No match
young = find(users, lambda u: u.age < 20)
print(young)  # None
```

**Testing Requirements:**
Your implementation should pass tests that verify:
- Finds first element matching predicate
- Returns `None` when no match found
- Returns `None` for empty lists
- Works with integer predicates
- Works with string predicates
- Works with custom object predicates
- Stops at first match (doesn't continue searching)
- Type hints are correctly specified with optional return type
- Handles predicates that are always true
- Handles predicates that are always false
