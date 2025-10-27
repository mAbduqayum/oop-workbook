# Generic Decorator

## Exercise: Generic Timing Decorator with ParamSpec

Implement a generic `@timer` decorator that measures and prints the execution time of any function while preserving its signature and return type. Use `ParamSpec` and `time.perf_counter()`. Print format: `"Function '{function_name}' took {elapsed:.4f} seconds"`.

**Why This Matters:**
Decorators are powerful but notoriously difficult to type correctly. Using `ParamSpec` and generics, you can create decorators that work with any function while maintaining complete type safety, enabling better IDE support and type checking.

**Example Usage:**
```python
# Decorate a simple function
@timer
def greet(name: str) -> str:
    time.sleep(0.1)
    return f"Hello, {name}!"

result = greet("Alice")
# Output: Function 'greet' took 0.1001 seconds
# result: "Hello, Alice!"

# Type safety is preserved
text: str = greet("Bob")  # Type checker knows return type is str

# Decorate function with multiple parameters
@timer
def add(a: int, b: int, c: int = 0) -> int:
    time.sleep(0.05)
    return a + b + c

total = add(1, 2, c=3)
# Output: Function 'add' took 0.0501 seconds
# total: 6

# Decorate function with no parameters
@timer
def get_random() -> int:
    time.sleep(0.02)
    return 42

value = get_random()
# Output: Function 'get_random' took 0.0201 seconds

# Decorate function returning different types
@timer
def get_items() -> list[str]:
    time.sleep(0.03)
    return ["apple", "banana", "cherry"]

items = get_items()
# Output: Function 'get_items' took 0.0301 seconds
# items is correctly typed as list[str]

# Works with complex return types
@timer
def compute() -> dict[str, int]:
    time.sleep(0.01)
    return {"a": 1, "b": 2}

result = compute()
# Output: Function 'compute' took 0.0101 seconds
```

**Advanced Example with Custom Types:**
```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

@timer
def create_user(name: str, age: int) -> User:
    time.sleep(0.05)
    return User(name, age)

user = create_user("Alice", 30)
# Output: Function 'create_user' took 0.0501 seconds
# user is correctly typed as User

@timer
def process_users(users: list[User], min_age: int = 0) -> list[str]:
    time.sleep(0.1)
    return [u.name for u in users if u.age >= min_age]

names = process_users([user], min_age=25)
# Output: Function 'process_users' took 0.1001 seconds
# names is correctly typed as list[str]

# Type checker catches errors
# error: process_users("not a list")  # Type error!
```

**Testing Different Function Signatures:**
```python
# No parameters, no return value
@timer
def do_nothing() -> None:
    time.sleep(0.01)

do_nothing()
# Output: Function 'do_nothing' took 0.0101 seconds

# Multiple parameters with defaults
@timer
def format_name(first: str, last: str, middle: str = "") -> str:
    time.sleep(0.02)
    if middle:
        return f"{first} {middle} {last}"
    return f"{first} {last}"

full_name = format_name("John", "Doe", middle="Q")
# Output: Function 'format_name' took 0.0201 seconds

# Keyword-only arguments
@timer
def configure(*, host: str, port: int, debug: bool = False) -> dict[str, str | int | bool]:
    time.sleep(0.01)
    return {"host": host, "port": port, "debug": debug}

config = configure(host="localhost", port=8080)
# Output: Function 'configure' took 0.0101 seconds
```

**Testing Requirements:**
Your implementation should pass tests that verify:
- Times function execution correctly (within reasonable margin)
- Prints correctly formatted timing message
- Returns the original function's return value
- Works with functions taking no parameters
- Works with functions taking multiple parameters
- Works with functions using default parameters
- Works with functions using keyword-only parameters
- Preserves function signature for type checkers
- Works with different return types (str, int, list, dict, custom objects, None)
- Function name appears correctly in output message
- Uses `@wraps` to preserve function metadata

**Implementation Hints:**
- Use `time.perf_counter()` for precise timing (call before and after function execution)
- Use `@wraps(func)` from functools to preserve function metadata
- The print format should be: `f"Function '{func.__name__}' took {elapsed:.4f} seconds"`
- Make sure to return the result from the original function call
- The decorator signature must use `ParamSpec` and a type variable for the return type
