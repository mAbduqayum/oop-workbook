# Identity Function

## Exercise: Generic Identity Function

Implement a generic `identity` function that accepts any value and returns it unchanged while preserving type information.

**Type Safety Examples:**
```python
# These should all preserve type information
num: int = identity(42)           # Type checker knows this is int
text: str = identity("hello")     # Type checker knows this is str
items: list[int] = identity([1, 2, 3])  # Type checker knows this is list[int]
```

**Why This Matters:**
The identity function is the simplest generic function, but it demonstrates the fundamental concept: a single implementation that works with any type while maintaining type safety. This pattern is the foundation for more complex generic utilities.

**Example Usage:**
```python
# Works with any type
print(identity(42))              # 42
print(identity("hello"))          # hello
print(identity([1, 2, 3]))       # [1, 2, 3]
print(identity({"key": "value"})) # {"key": "value"}

# Type checkers understand the return type
x: int = identity(10)        # Valid: returns int
y: str = identity("text")    # Valid: returns str
# z: str = identity(10)      # Type error: can't assign int to str
```

**Testing Requirements:**
Your implementation should pass tests that verify:
- Returns the exact same value for integers
- Returns the exact same value for strings
- Returns the exact same value for lists
- Returns the exact same value for dictionaries
- Returns the exact same value for custom objects
- Type hints are correctly specified for type checkers
