# Python Generics: Type Parameters and Generic Programming

## What Are Generics?

**Generics** allow you to write code that works with multiple types while maintaining type safety. Instead of writing the same code multiple times for different types (one for integers, one for strings, one for custom objects), you write it once with a type parameter that acts as a placeholder.

Think of generics as creating a **blueprint** that works with any type, rather than a specific blueprint for each type.

## Real-World Analogies

### The Container Analogy

Imagine a storage container at a warehouse:
- **Non-generic approach:** You need separate containers labeled "Books Only", "Electronics Only", "Clothes Only" -- one specialized container type for each item category
- **Generic approach:** You have a universal container that can hold ANY type of item, but once you put books in it, it's treated as a "Container of Books"

The generic container knows what type of items it holds, so you can't accidentally put electronics in a book container.

### The Recipe Analogy

A recipe for making a sauce:
- **Non-generic:** Separate recipes for "Tomato Sauce", "Cheese Sauce", "Chocolate Sauce" -- even though the process (heat, stir, thicken) is identical
- **Generic:** One "Sauce[Ingredient]" recipe where Ingredient is a placeholder. Use `Sauce[Tomato]`, `Sauce[Cheese]`, or `Sauce[Chocolate]`

The process stays the same, but the type of ingredient changes.

## Why Use Generics?

### Problem: Without Generics

```python
class IntStack:
    def __init__(self):
        self._items: list[int] = []

    def push(self, item: int) -> None:
        self._items.append(item)

    def pop(self) -> int:
        return self._items.pop()

class StringStack:
    def __init__(self):
        self._items: list[str] = []

    def push(self, item: str) -> None:
        self._items.append(item)

    def pop(self) -> str:
        return self._items.pop()
```

This approach has serious problems:
- **Code duplication:** Same logic repeated for every type
- **Maintenance nightmare:** Fix a bug? Update it in every version
- **Limited types:** Need a stack for floats? Write another class
- **No type safety with Any:** Using `Any` gives up type checking entirely

### Solution: With Generics

```python
class Stack[T]:
    def __init__(self):
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

int_stack = Stack[int]()
int_stack.push(42)

str_stack = Stack[str]()
str_stack.push("hello")
```

**Benefits:**
- **Write once, use everywhere:** One implementation for all types
- **Type safety:** Type checkers verify you're using the right types
- **Maintainability:** Fix bugs in one place
- **Flexibility:** Works with any type without losing type information

## Generic Syntax

Python provides a clean, intuitive syntax for generics that makes them simple to use.

### Generic Classes

Define type parameters directly in square brackets after the class name:

```python
class Cache[T]:
    def __init__(self):
        self._data: dict[str, T] = {}

    def get(self, key: str) -> T | None:
        return self._data.get(key)

    def set(self, key: str, value: T) -> None:
        self._data[key] = value

user_cache = Cache[User]()
user_cache.set("user_1", User("Alice"))

config_cache = Cache[dict]()
config_cache.set("settings", {"theme": "dark"})
```

**Key features:**
- Type parameters defined directly in class declaration `[T]`
- No need to import `TypeVar` or `Generic`
- Clean, readable syntax

### Generic Functions

Functions can also have type parameters:

```python
def first[T](items: list[T]) -> T:
    return items[0]

def last[T](items: list[T]) -> T:
    return items[-1]

def swap[T](a: T, b: T) -> tuple[T, T]:
    return (b, a)

result1 = first[int]([1, 2, 3])
result2 = last[str](["a", "b", "c"])
x, y = swap[float](3.14, 2.71)
```

### Type Aliases

Use the `type` statement to create generic type aliases:

```python
type Point2D = tuple[float, float]
type Point3D = tuple[float, float, float]

type ListOrSet[T] = list[T] | set[T]
type Nested[T] = list[list[T]]

type JSON = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None
```

**Key advantage:** The `type` statement enables self-referential type aliases without quotes (forward references).

## Working with Type Parameters

### Multiple Type Parameters

Classes and functions can use multiple type parameters:

```python
class KeyValueStore[K, V]:
    def __init__(self):
        self._store: dict[K, V] = {}

    def put(self, key: K, value: V) -> None:
        self._store[key] = value

    def get(self, key: K) -> V | None:
        return self._store.get(key)

store = KeyValueStore[str, int]()
store.put("age", 25)
store.put("score", 100)

def pair[T, U](first: T, second: U) -> tuple[T, U]:
    return (first, second)

result = pair[str, int]("answer", 42)
```

### Bounded Type Parameters

Restrict a type parameter to subclasses of a specific type using `:` (colon):

```python
class ConnectionPool[T: DatabaseConnection]:
    def __init__(self, max_connections: int):
        self._connections: list[T] = []
        self._max_connections = max_connections

    def add_connection(self, conn: T) -> None:
        if len(self._connections) < self._max_connections:
            self._connections.append(conn)

    def close_all(self) -> None:
        for conn in self._connections:
            conn.close()

class DatabaseConnection:
    def close(self):
        print("Closing connection...")

class PostgresConnection(DatabaseConnection):
    def execute_query(self, sql: str):
        print(f"Executing: {sql}")

pg_pool = ConnectionPool[PostgresConnection](max_connections=10)
pg_pool.add_connection(PostgresConnection())
```

**Why use bounds?**
- Ensures type parameter has specific methods/attributes
- Type checker knows `T` supports methods from the bound class
- Provides compile-time safety

### Constrained Type Parameters

Limit a type parameter to a specific set of types:

```python
class Adder[T: (int, float)]:
    def add(self, a: T, b: T) -> T:
        return a + b

int_adder = Adder[int]()
print(int_adder.add(5, 10))

float_adder = Adder[float]()
print(float_adder.add(3.14, 2.71))
```

**Difference from bounds:**
- **Bounds:** Allow any subclass (flexible)
- **Constraints:** Only exact types listed (restrictive)

### Variadic Type Parameters

For types that need an arbitrary number of type parameters, use `*`:

```python
class Array[*Shape]:
    def __init__(self, data):
        self.data = data

class Tensor[DType, *Shape]:
    pass

tensor1 = Tensor[float, 10, 20, 30]()
```

**Use cases:**
- Tensor/array dimensions (NumPy, PyTorch)
- Tuple types with unknown length
- Function signatures with variable arguments

### ParamSpec for Callables

Preserve function parameter signatures in decorators using `**P`:

```python
from collections.abc import Callable

def log_call[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age}"
```

## Type Defaults

Python supports default values for type parameters, similar to default function arguments.

### Basic Type Defaults

```python
class Response[T = dict]:
    def __init__(self, data: T, status_code: int):
        self.data = data
        self.status_code = status_code

response1 = Response({"message": "OK"}, 200)
response2 = Response[str]("Success", 200)
```

**Without type argument:** `Response({...}, 200)` -> `Response[dict]` (uses default)
**With type argument:** `Response[str]("Success", 200)` -> `Response[str]` (overrides default)

### Default Rules

**Ordering Rule:** Non-default type parameters cannot follow defaults:

```python
class Good[T, U = int]:
    pass

class Bad[T = int, U]:
    pass
```

**Type Parameter as Default:**
```python
class Range[StartT = int, StopT = StartT]:
    pass

r1 = Range()
r2 = Range[float]()
```

**Bound Compatibility:** Default must be a subtype of the bound:

```python
class Serializer[T: BaseModel = User]:
    pass
```

### Real-World Use Cases

**Generator with sensible defaults:**
```python
class Generator[YieldT, SendT = None, ReturnT = None]:
    pass

def simple_gen() -> Generator[int]:
    pass
```

**NumPy-style arrays:**
```python
class Array[DType = float, *Shape]:
    pass

arr1 = Array()
arr2 = Array[int]()
```

## Variance: How Types Relate

Variance describes how type parameters behave in subtyping relationships.

### Variance Types

**Invariant (default):**
- `Cache[User]` is NOT a subtype of `Cache[Person]`
- Cannot substitute even if `User` is a subtype of `Person`
- Used for mutable containers

**Covariant:**
- `Reader[User]` IS a subtype of `Reader[Person]`
- Subtypes are preserved
- Used for read-only containers

**Contravariant:**
- `Validator[Person]` IS a subtype of `Validator[User]`
- Subtypes are reversed
- Used for consumers/callbacks

### Automatic Variance Inference

Python infers variance automatically based on how you use type parameters:

```python
class Reader[T]:
    def __init__(self, items: list[T]):
        self._items = items

    def read(self) -> T:
        return self._items[0]

class Store[T]:
    def __init__(self):
        self._items: list[T] = []

    def get(self) -> T:
        return self._items[0]

    def add(self, item: T) -> None:
        self._items.append(item)
```

Type checkers analyze:
- **Reader:** Only returns `T` -> **covariant**
- **Store:** Both reads and writes `T` -> **invariant**

No manual variance annotation needed.

## Real-World Examples

### Example 1: Generic Stack

```python
class Stack[T]:
    def __init__(self):
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop())
```

### Example 2: Generic Repository Pattern

```python
class Repository[T]:
    def __init__(self):
        self._items: dict[int, T] = {}
        self._next_id = 1

    def add(self, item: T) -> int:
        item_id = self._next_id
        self._items[item_id] = item
        self._next_id += 1
        return item_id

    def get(self, item_id: int) -> T | None:
        return self._items.get(item_id)

    def get_all(self) -> list[T]:
        return list(self._items.values())

    def delete(self, item_id: int) -> bool:
        if item_id in self._items:
            del self._items[item_id]
            return True
        return False

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

user_repo = Repository[User]()
user_id = user_repo.add(User("Alice", "alice@example.com"))
user = user_repo.get(user_id)
```

### Example 3: Generic Pair

```python
class Pair[T, U]:
    def __init__(self, first: T, second: U):
        self.first = first
        self.second = second

    def swap(self) -> 'Pair[U, T]':
        return Pair(self.second, self.first)

    def __repr__(self) -> str:
        return f"Pair({self.first}, {self.second})"

p1 = Pair[str, int]("age", 25)
p2 = p1.swap()
```

### Example 4: Generic Builder Pattern

```python
class Builder[T]:
    def __init__(self, constructor):
        self._constructor = constructor
        self._kwargs = {}

    def with_attr(self, name: str, value) -> 'Builder[T]':
        self._kwargs[name] = value
        return self

    def build(self) -> T:
        return self._constructor(**self._kwargs)

class Person:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city

person = (Builder[Person](Person)
    .with_attr("name", "Alice")
    .with_attr("age", 30)
    .with_attr("city", "NYC")
    .build())
```

### Example 5: Generic Data Validator

```python
from collections.abc import Callable

class Validator[T]:
    def __init__(self):
        self._rules: list[tuple[Callable[[T], bool], str]] = []

    def add_rule(self, rule: Callable[[T], bool], message: str) -> None:
        self._rules.append((rule, message))

    def validate(self, value: T) -> list[str]:
        errors = []
        for rule, message in self._rules:
            if not rule(value):
                errors.append(message)
        return errors

string_validator = Validator[str]()
string_validator.add_rule(lambda s: len(s) > 0, "String cannot be empty")
string_validator.add_rule(lambda s: len(s) < 100, "String too long")

errors = string_validator.validate("Hello")
print(errors)
```

## Best Practices

### 1. Use Generics When You Have Type-Agnostic Logic

**Good use case:**
```python
class Cache[K, V]:
    def __init__(self, max_size: int):
        self._cache: dict[K, V] = {}
        self._max_size = max_size
```

**Bad use case:**
```python
class Calculator[T]:
    def add(self, a: T, b: T) -> T:
        return a + b
```

### 2. Prefer Type Parameters Over `Any`

```python
from typing import Any

def first_bad(items: list[Any]) -> Any:
    return items[0]

def first_good[T](items: list[T]) -> T:
    return items[0]
```

### 3. Use Bounds for Common Interfaces

```python
from collections.abc import Sized

class Measurable[T: Sized]:
    def __init__(self, item: T):
        self.item = item

    def get_size(self) -> int:
        return len(self.item)
```

### 4. Don't Over-Genericize

```python
class Person[T]:
    pass
```

Not everything needs to be generic. Use generics when you genuinely need type flexibility.

### 5. Provide Sensible Defaults

```python
class Response[T = dict]:
    def __init__(self, data: T, status_code: int):
        self.data = data
        self.status_code = status_code
```

## Common Patterns

### Pattern 1: Generic Factory

```python
class Factory[T]:
    def __init__(self, constructor: type[T]):
        self._constructor = constructor

    def create(self, *args, **kwargs) -> T:
        return self._constructor(*args, **kwargs)

class Product:
    def __init__(self, name: str):
        self.name = name

factory = Factory[Product](Product)
product = factory.create("Widget")
```

### Pattern 2: Generic Result Type

```python
class Result[T, E]:
    def __init__(self, value: T | None, error: E | None):
        self.value = value
        self.error = error

    def is_ok(self) -> bool:
        return self.error is None

    def unwrap(self) -> T:
        if self.error:
            raise ValueError(f"Result has error: {self.error}")
        return self.value

def divide(a: int, b: int) -> Result[float, str]:
    if b == 0:
        return Result[float, str](None, "Division by zero")
    return Result[float, str](a / b, None)
```

### Pattern 3: Generic Decorator

```python
from collections.abc import Callable

def memoize[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    cache: dict = {}

    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper

@memoize
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

## Common Pitfalls

### Pitfall 1: Using `Any` Instead of Generics

```python
from typing import Any

def process(items: list[Any]) -> Any:
    return items[0]
```

### Pitfall 2: Not Constraining When Needed

```python
class Comparable[T]:
    def max(self, a: T, b: T) -> T:
        return a if a > b else b
```

### Pitfall 3: Over-Complicating Simple Code

```python
class SimpleList[T, U, V]:
    pass
```

### Pitfall 4: Ignoring Variance

```python
def add_admin(users: list[User]) -> None:
    users.append(Admin())

admins: list[Admin] = [Admin()]
add_admin(admins)
```

## When to Use Generics

### Use Generics When:

1. **You need type-safe containers**
   - Lists, stacks, queues, trees
   - Caches, repositories, stores

2. **You have reusable algorithms**
   - Sorting, searching, filtering
   - Mapping, reducing, folding

3. **You're building libraries/frameworks**
   - Generic interfaces users will implement
   - Type-safe APIs

4. **You need multiple implementations of the same interface**
   - Repository pattern for different databases
   - Strategy pattern with different algorithms

### Avoid Generics When:

1. **The code is specific to one type**
   - No need to make it generic

2. **Type relationships are complex**
   - Might make code harder to understand

3. **Simple code becomes complicated**
   - Don't over-engineer

## Key Takeaways

**Generics = Type Parameters = Blueprints for Multiple Types**

- Write once, use with many types
- Type safety without code duplication
- Clean syntax with `[T]` notation
- Use bounds when you need specific methods/attributes
- Use constraints when you need exact types
- Variance is inferred automatically
- Type defaults provide sensible fallbacks
- Prefer generics over `Any` for type safety

**Remember:** Generics make your code more flexible and maintainable while preserving type information. Use them when you have logic that truly works across multiple types, but don't over-complicate simple code.
