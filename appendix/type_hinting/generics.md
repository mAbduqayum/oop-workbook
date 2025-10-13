# Python Generics: Complete Tutorial

## Table of Contents
1. [Introduction to Generics](#introduction-to-generics)
2. [TypeVar Basics](#typevar-basics)
3. [Generic Functions](#generic-functions)
4. [Generic Classes](#generic-classes)
5. [Multiple Type Variables](#multiple-type-variables)
6. [Bounded Type Variables](#bounded-type-variables)
7. [Constrained Type Variables](#constrained-type-variables)
8. [Variance](#variance)
9. [Generic Protocols](#generic-protocols)
10. [ParamSpec for Callables](#paramspec-for-callables)
11. [Advanced Patterns](#advanced-patterns)
12. [Best Practices](#best-practices)

## Introduction to Generics

Generics allow you to write flexible, reusable code that works with multiple types while maintaining type safety. Instead of writing separate functions for each type, you can write one generic function that adapts to the types you use.

**Why use generics?**
- Write code once, use with many types
- Maintain type safety and IDE support
- Avoid code duplication
- Make relationships between types explicit

**Python Version:** This guide uses **Python 3.12+** syntax exclusively for cleaner, more modern code.

<details>
<summary>Legacy Syntax (Python 3.9-3.11)</summary>

If you're using Python 3.9-3.11, you'll need to use `TypeVar` and `Generic`:

```python
from typing import TypeVar, Generic

T = TypeVar('T')

def identity(value: T) -> T:
    return value

class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
```

The concepts are identical - only the syntax differs.
</details>

## TypeVar Basics

Python 3.12 introduced **built-in generic syntax** - no imports or explicit TypeVar needed!

```python
# Generic function - just use [T] syntax
def identity[T](value: T) -> T:
    """Returns the same value passed in."""
    return value

# Type checker infers the type
x = identity(42)        # x is int
y = identity("hello")   # y is str
z = identity([1, 2])    # z is list[int]

# Generic class - same simple syntax
class Box[T]:
    def __init__(self, value: T) -> None:
        self._value = value
    
    def get(self) -> T:
        return self._value

# Usage
int_box = Box(42)         # Box[int]
str_box = Box("hello")    # Box[str]
```

**Key benefits:**
- No imports needed
- Cleaner, more readable
- Type parameter scope is automatic
- This is the recommended modern approach

The key insight: **the return type matches the input type**.

## Generic Functions

### Simple Generic Function

```python
from collections.abc import Sequence

def first_element[T](items: Sequence[T]) -> T:
    """Get the first element from a sequence."""
    return items[0]

# Works with different types
num = first_element([1, 2, 3])      # int
text = first_element(["a", "b"])    # str
char = first_element("hello")       # str
```

### Multiple Parameters with Same Type

```python
def are_equal[T](a: T, b: T) -> bool:
    """Check if two values are equal."""
    return a == b

# Both parameters must be the same type
are_equal(1, 2)           # OK: both int
are_equal("a", "b")       # OK: both str
# are_equal(1, "a")       # Error: mixed types
```

### Returning Collections of Generic Type

```python
def repeat[T](item: T, times: int) -> list[T]:
    """Repeat an item multiple times."""
    return [item] * times

numbers = repeat(5, 3)        # list[int]
words = repeat("hi", 2)       # list[str]

def wrap_in_list[T](item: T) -> list[T]:
    """Wrap a single item in a list."""
    return [item]
```

### Generic Function with Multiple Operations

```python
def process_list[T](items: list[T], default: T) -> T:
    """Return first item or default if list is empty."""
    return items[0] if items else default

# Type checker ensures default matches list type
result1 = process_list([1, 2, 3], 0)           # OK: int
result2 = process_list(["a", "b"], "none")     # OK: str
# result3 = process_list([1, 2], "none")       # Error: mixed types
```

## Generic Classes

### Basic Generic Class

```python
class Box[T]:
    """A simple container for a single value."""
    
    def __init__(self, value: T) -> None:
        self._value = value
    
    def get(self) -> T:
        return self._value
    
    def set(self, value: T) -> None:
        self._value = value

# Create boxes with different types
int_box = Box(42)           # Box[int]
str_box = Box("hello")      # Box[str]

# Type checker enforces consistency
num = int_box.get()      # int
int_box.set(100)         # OK
# int_box.set("text")    # Error: expected int
```

### Stack Implementation

```python
class Stack[T]:
    """A generic stack (LIFO) data structure."""
    
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        """Add item to top of stack."""
        self._items.append(item)
    
    def pop(self) -> T:
        """Remove and return top item."""
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items.pop()
    
    def peek(self) -> T | None:
        """View top item without removing."""
        return self._items[-1] if self._items else None
    
    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Get number of items in stack."""
        return len(self._items)

# Usage
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
value = int_stack.pop()  # int

str_stack = Stack[str]()
str_stack.push("hello")
# str_stack.push(42)     # Error: expected str
```

### Queue Implementation

```python
class Queue[T]:
    """A generic queue (FIFO) data structure."""
    
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def enqueue(self, item: T) -> None:
        """Add item to end of queue."""
        self._items.append(item)
    
    def dequeue(self) -> T:
        """Remove and return front item."""
        if not self._items:
            raise IndexError("Queue is empty")
        return self._items.pop(0)
    
    def front(self) -> T | None:
        """View front item without removing."""
        return self._items[0] if self._items else None
    
    def is_empty(self) -> bool:
        return len(self._items) == 0

# Usage
task_queue = Queue[str]()
task_queue.enqueue("task1")
task_queue.enqueue("task2")
next_task = task_queue.dequeue()  # str
```

## Multiple Type Variables

### Pair/Tuple Class

```python
class Pair[K, V]:
    """A container holding two values of potentially different types."""
    
    def __init__(self, first: K, second: V) -> None:
        self.first = first
        self.second = second
    
    def get_first(self) -> K:
        return self.first
    
    def get_second(self) -> V:
        return self.second
    
    def swap(self) -> 'Pair[V, K]':
        """Return new pair with values swapped."""
        return Pair(self.second, self.first)

# Usage
pair1 = Pair("age", 25)        # Pair[str, int]
pair2 = Pair(1, "first")       # Pair[int, str]

# Access with type safety
name = pair1.get_first()   # str
age = pair1.get_second()   # int

# Swapping creates correct new type
swapped = pair1.swap()     # Pair[int, str]
```

### Generic Cache/Map

```python
class Cache[K, V]:
    """A simple key-value cache."""
    
    def __init__(self) -> None:
        self._data: dict[K, V] = {}
    
    def set(self, key: K, value: V) -> None:
        """Store a value with a key."""
        self._data[key] = value
    
    def get(self, key: K) -> V | None:
        """Retrieve a value by key."""
        return self._data.get(key)
    
    def has(self, key: K) -> bool:
        """Check if key exists."""
        return key in self._data
    
    def delete(self, key: K) -> bool:
        """Remove a key-value pair."""
        if key in self._data:
            del self._data[key]
            return True
        return False
    
    def items(self) -> list[tuple[K, V]]:
        """Get all key-value pairs."""
        return list(self._data.items())
    
    def keys(self) -> list[K]:
        """Get all keys."""
        return list(self._data.keys())
    
    def values(self) -> list[V]:
        """Get all values."""
        return list(self._data.values())

# Usage examples
user_cache = Cache[int, str]()
user_cache.set(1, "Alice")
user_cache.set(2, "Bob")
name = user_cache.get(1)  # str | None

config_cache = Cache[str, int | str]()
config_cache.set("timeout", 30)
config_cache.set("name", "app")
```

### Generic Result Type

```python
class Result[T, E]:
    """Represents either a success (Ok) or failure (Err)."""
    
    def __init__(self, value: T | None = None, error: E | None = None) -> None:
        if value is not None and error is not None:
            raise ValueError("Cannot have both value and error")
        if value is None and error is None:
            raise ValueError("Must have either value or error")
        self._value = value
        self._error = error
    
    def is_ok(self) -> bool:
        return self._value is not None
    
    def is_err(self) -> bool:
        return self._error is not None
    
    def unwrap(self) -> T:
        """Get value or raise if error."""
        if self._value is not None:
            return self._value
        raise ValueError(f"Called unwrap on error: {self._error}")
    
    def unwrap_or(self, default: T) -> T:
        """Get value or return default."""
        return self._value if self._value is not None else default
    
    def error(self) -> E | None:
        """Get error if present."""
        return self._error

# Usage
def divide(a: int, b: int) -> Result[float, str]:
    if b == 0:
        return Result(error="Division by zero")
    return Result(value=a / b)

result = divide(10, 2)
if result.is_ok():
    print(result.unwrap())  # 5.0
else:
    print(result.error())
```

## Bounded Type Variables

Bounded type variables restrict the types that can be used with a generic.

### Upper Bound

```python
from collections.abc import Sized

def get_length[T: Sized](item: T) -> int:
    """Get length of any sized object."""
    return len(item)

# Works with any Sized type
get_length("hello")        # str has __len__
get_length([1, 2, 3])      # list has __len__
get_length({1, 2})         # set has __len__
# get_length(42)           # Error: int is not Sized
```

### Numeric Bound

```python
from typing import Protocol

class SupportsAdd(Protocol):
    def __add__(self, other) -> 'SupportsAdd': ...

def add_all[T: SupportsAdd](items: list[T]) -> T:
    """Sum all items that support addition."""
    if not items:
        raise ValueError("Empty list")
    result = items[0]
    for item in items[1:]:
        result = result + item
    return result

# Works with numbers
add_all([1, 2, 3])           # int
add_all([1.5, 2.5, 3.0])     # float

# Also works with strings
add_all(["hello", " ", "world"])  # str
```

### Comparable Bound

```python
from typing import Protocol, Any

class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...

def find_min[T: Comparable](items: list[T]) -> T:
    """Find minimum value in list."""
    if not items:
        raise ValueError("Empty list")
    return min(items)

def find_max[T: Comparable](items: list[T]) -> T:
    """Find maximum value in list."""
    if not items:
        raise ValueError("Empty list")
    return max(items)

def sort_items[T: Comparable](items: list[T]) -> list[T]:
    """Sort items in ascending order."""
    return sorted(items)

# Usage
find_min([3, 1, 4, 1, 5])        # int
find_max(["zebra", "apple"])     # str
```

**Python 3.9-3.11:**
```python
from typing import TypeVar, Protocol, Any

class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...

T = TypeVar('T', bound=Comparable)

def find_min(items: list[T]) -> T:
    """Find minimum value in list."""
    if not items:
        raise ValueError("Empty list")
    return min(items)
```

## Constrained Type Variables

Constrained type variables limit the possible types to a specific set.

**Note:** Python 3.12+ doesn't have simpler syntax for constraints - you still need `TypeVar` for this feature.

### Basic Constraints

```python
from typing import TypeVar

# T can only be int or float (both syntaxes the same)
Numeric = TypeVar('Numeric', int, float)

def average(values: list[Numeric]) -> float:
    """Calculate average of numeric values."""
    return sum(values) / len(values)

# Works with int or float
average([1, 2, 3])           # OK: list[int]
average([1.5, 2.5, 3.0])     # OK: list[float]
# average(["1", "2"])        # Error: str not allowed

def multiply(a: Numeric, b: Numeric) -> Numeric:
    """Multiply two numbers."""
    return a * b

# Return type matches input type
result1 = multiply(5, 3)         # int
result2 = multiply(2.5, 4.0)     # float
```

### String or Bytes Constraint

```python
from typing import TypeVar

AnyStr = TypeVar('AnyStr', str, bytes)

def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    """Concatenate two strings or two bytes."""
    return a + b

# Works with consistent types
concat("hello", "world")        # str
concat(b"hello", b"world")      # bytes
# concat("hello", b"world")     # Error: mixed types

def join_items(separator: AnyStr, items: list[AnyStr]) -> AnyStr:
    """Join items with separator."""
    return separator.join(items)

# Type is preserved
text = join_items(" ", ["a", "b"])          # str
data = join_items(b"-", [b"x", b"y"])       # bytes
```

## Variance

Variance describes how subtyping relationships between complex types relate to subtyping relationships of their components.

### Covariance (Producer)

Covariant type variables are read-only (producers).

```python
from typing import TypeVar, Generic

T_co = TypeVar('T_co', covariant=True)

class Producer(Generic[T_co]):
    """A producer can only produce/return values of type T."""
    
    def __init__(self, value: T_co) -> None:
        self._value = value
    
    def produce(self) -> T_co:
        """Get the value (producer)."""
        return self._value
    
    # Cannot have methods that accept T_co as input
    # def consume(self, value: T_co) -> None:  # Would break covariance!
    #     pass

# Covariance allows subtype substitution for return values
class Animal: pass
class Dog(Animal): pass

dog_producer: Producer[Dog] = Producer(Dog())
# Can assign to more general type
animal_producer: Producer[Animal] = dog_producer  # OK with covariance
```

### Contravariance (Consumer)

Contravariant type variables are write-only (consumers).

```python
from typing import TypeVar, Generic

T_contra = TypeVar('T_contra', contravariant=True)

class Consumer(Generic[T_contra]):
    """A consumer can only consume/accept values of type T."""
    
    def consume(self, value: T_contra) -> None:
        """Accept a value (consumer)."""
        print(f"Consuming: {value}")
    
    # Cannot have methods that return T_contra
    # def produce(self) -> T_contra:  # Would break contravariance!
    #     pass

# Contravariance allows supertype substitution for parameters
class Animal: pass
class Dog(Animal): pass

animal_consumer: Consumer[Animal] = Consumer()
# Can assign to more specific type
dog_consumer: Consumer[Dog] = animal_consumer  # OK with contravariance
```

### Invariance (Default)

Invariant type variables (default) can both read and write.

```python
from typing import TypeVar, Generic

T = TypeVar('T')  # Invariant by default

class Container(Generic[T]):
    """A container that can both store and retrieve values."""
    
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def add(self, item: T) -> None:
        """Add item (consumer)."""
        self._items.append(item)
    
    def get(self, index: int) -> T:
        """Get item (producer)."""
        return self._items[index]

# Invariance: no subtype substitution allowed
class Animal: pass
class Dog(Animal): pass

dog_container: Container[Dog] = Container()
# animal_container: Container[Animal] = dog_container  # Error: invariant!
```

## Generic Protocols

Protocols can be generic, allowing structural subtyping with type parameters.

### Generic Comparable Protocol

```python
from typing import Protocol, TypeVar, Any

T = TypeVar('T')

class Comparable(Protocol[T]):
    """Protocol for comparable types."""
    
    def __lt__(self, other: T) -> bool: ...
    def __le__(self, other: T) -> bool: ...
    def __gt__(self, other: T) -> bool: ...
    def __ge__(self, other: T) -> bool: ...

def sort_items(items: list[Comparable[T]]) -> list[Comparable[T]]:
    """Sort items implementing Comparable."""
    return sorted(items)
```

### Generic Container Protocol

```python
from typing import Protocol, TypeVar
from collections.abc import Iterator

T = TypeVar('T')

class Container(Protocol[T]):
    """Protocol for container types."""
    
    def __contains__(self, item: T) -> bool: ...
    def __iter__(self) -> Iterator[T]: ...
    def __len__(self) -> int: ...

def has_duplicates(container: Container[T]) -> bool:
    """Check if container has duplicate items."""
    seen: set[T] = set()
    for item in container:
        if item in seen:
            return True
        seen.add(item)
    return False
```

## ParamSpec for Callables

`ParamSpec` preserves function signatures in decorators and wrappers.

### Basic ParamSpec

```python
from typing import TypeVar, ParamSpec, Callable
from functools import wraps

P = ParamSpec('P')
R = TypeVar('R')

def log_calls(func: Callable[P, R]) -> Callable[P, R]:
    """Decorator that logs function calls."""
    
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    
    return wrapper

@log_calls
def add(x: int, y: int) -> int:
    return x + y

# Type checker knows signature is preserved
result = add(5, 3)  # (int, int) -> int
```

### Async ParamSpec

```python
from typing import TypeVar, ParamSpec, Callable
from collections.abc import Awaitable
from functools import wraps
import time

P = ParamSpec('P')
R = TypeVar('R')

def async_timer(func: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[R]]:
    """Time async function execution."""
    
    @wraps(func)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.time()
        result = await func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.2f}s")
        return result
    
    return wrapper

@async_timer
async def fetch_data(url: str, timeout: int = 30) -> dict:
    # async logic here
    return {"data": "value"}
```

## Advanced Patterns

### Generic Builder

```python
from typing import Generic, TypeVar, Self

T = TypeVar('T')

class Builder(Generic[T]):
    """Generic builder pattern."""
    
    def __init__(self, factory: type[T]) -> None:
        self._factory = factory
        self._kwargs: dict[str, Any] = {}
    
    def set(self, key: str, value: Any) -> Self:
        """Set a property."""
        self._kwargs[key] = value
        return self
    
    def build(self) -> T:
        """Build the object."""
        return self._factory(**self._kwargs)

# Usage
class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

user = (Builder(User)
        .set("name", "Alice")
        .set("age", 30)
        .build())  # Returns User
```

### Generic Repository Pattern

```python
from typing import Generic, TypeVar, Protocol

class Entity(Protocol):
    """Protocol for entities with an ID."""
    id: int

T = TypeVar('T', bound=Entity)

class Repository(Generic[T]):
    """Generic repository for data access."""
    
    def __init__(self) -> None:
        self._storage: dict[int, T] = {}
        self._next_id = 1
    
    def add(self, entity: T) -> T:
        """Add entity and assign ID."""
        entity.id = self._next_id
        self._storage[self._next_id] = entity
        self._next_id += 1
        return entity
    
    def get(self, entity_id: int) -> T | None:
        """Get entity by ID."""
        return self._storage.get(entity_id)
    
    def get_all(self) -> list[T]:
        """Get all entities."""
        return list(self._storage.values())
    
    def delete(self, entity_id: int) -> bool:
        """Delete entity by ID."""
        if entity_id in self._storage:
            del self._storage[entity_id]
            return True
        return False

# Usage
class User:
    def __init__(self, name: str) -> None:
        self.id: int = 0
        self.name = name

user_repo: Repository[User] = Repository()
user = user_repo.add(User("Alice"))
found = user_repo.get(user.id)  # User | None
```

## Best Practices

### 1. Use Descriptive TypeVar Names

```python
# Bad: Single letters everywhere
T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')

# Good: Descriptive names for complex code
Key = TypeVar('Key')
Value = TypeVar('Value')
Element = TypeVar('Element')
Result = TypeVar('Result')
```

### 2. Prefer Bounds Over Constraints

```python
# Less flexible: only int or float
Numeric = TypeVar('Numeric', int, float)

# More flexible: any numeric type
from typing import Protocol

class SupportsAdd(Protocol):
    def __add__(self, other: Any) -> Any: ...

Numeric = TypeVar('Numeric', bound=SupportsAdd)
```

### 3. Use Generic Protocols for Flexibility

```python
from typing import Protocol, TypeVar

T = TypeVar('T')

class Drawable(Protocol):
    def draw(self) -> None: ...

def render_all(items: list[Drawable]) -> None:
    """Works with any class that has draw method."""
    for item in items:
        item.draw()
```

### 4. Don't Over-Generalize

```python
# Bad: Too generic, loses meaning
def process(data: T) -> T:
    return data

# Good: Specific enough to be useful
def uppercase_strings(items: list[str]) -> list[str]:
    return [s.upper() for s in items]
```

### 5. Document Generic Constraints

```python
from typing import TypeVar
from collections.abc import Sized

T = TypeVar('T', bound=Sized)

def longest(items: list[T]) -> T:
    """
    Find the longest item in a list.
    
    Args:
        items: List of sized objects (strings, lists, etc.)
    
    Returns:
        The item with the greatest length
    
    Note:
        All items must implement __len__ method
    """
    return max(items, key=len)
```

## Summary

**Key Concepts:**
- **Python 3.12+**: Use `class Box[T]:` and `def func[T](x: T):` - no imports needed!
- **Python 3.9-3.11**: Requires `TypeVar` and `Generic` imports
- **Generic classes**: Reusable containers and data structures
- **Bounds**: Restrict types to those with certain capabilities (`T: Sized`)
- **Constraints**: Limit to specific set of types (still needs `TypeVar`)
- **Variance**: Control subtype relationships (covariant/contravariant)
- **ParamSpec**: Preserve function signatures in decorators

**When to Use Generics:**
- Building reusable containers (Stack, Queue, Cache)
- Creating type-safe wrappers and decorators
- Implementing patterns (Repository, Builder, Result)
- Functions that work with multiple types identically

**Syntax Comparison:**
```python
# Python 3.12+ (recommended)
def identity[T](x: T) -> T:
    return x

class Box[T]:
    def __init__(self, value: T) -> None:
        self.value = value

# Python 3.9-3.11 (legacy)
from typing import TypeVar, Generic

T = TypeVar('T')

def identity(x: T) -> T:
    return x

class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
```

**Remember:**
- Prefer Python 3.12+ syntax when possible
- Use bounds for flexibility over constraints
- Document constraints clearly
- Generics are compile-time only
