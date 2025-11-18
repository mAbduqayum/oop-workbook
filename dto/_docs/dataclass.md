# Python Dataclasses

## What Are Dataclasses?

Dataclasses are a Python feature (introduced in 3.7) that automatically generates special methods for classes that
primarily store data. They significantly reduce boilerplate code.

## Core Features

### Basic Syntax

```python
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
    label: str = "origin"


p = Point(1.5, 2.5)
print(p)
```

This automatically generates:

- `__init__(self, x, y, label="origin")`
- `__repr__()`
- `__eq__()`

### Automatically Generated Methods

```python
@dataclass
class Product:
    name: str
    price: float


p1 = Product("Laptop", 999.99)
p2 = Product("Laptop", 999.99)

print(p1)
print(p1 == p2)
```

## Field Types and Options

### Basic Fields

```python
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    grades: list[int]
    email: str | None = None
```

### Field Function

```python
from dataclasses import dataclass, field


@dataclass
class Config:
    name: str
    tags: list[str] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass
class Secret:
    username: str
    password: str = field(repr=False)
    internal_id: int = field(init=False, default=0)
    timestamp: float = field(compare=False, default=0.0)
```

### Field Parameters

- `default`: Default value for the field
- `default_factory`: Function to generate default value
- `init`: Include in `__init__` (default: True)
- `repr`: Include in `__repr__` (default: True)
- `compare`: Include in comparison methods (default: True)
- `hash`: Include in `__hash__` (default: None)
- `metadata`: Additional metadata dictionary

## Advanced Features

### Frozen Dataclasses (Immutability)

```python
@dataclass(frozen=True)
class Point:
    x: float
    y: float


p = Point(1.0, 2.0)
```

**Use Cases:**

- Dictionary keys
- Set elements
- Thread-safe data structures
- Value objects

```python
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float


locations = {
    Coordinate(40.7128, -74.0060): "New York",
    Coordinate(51.5074, -0.1278): "London",
}
```

### Ordering

```python
@dataclass(order=True)
class Task:
    priority: int
    name: str = field(compare=False)


tasks = [
    Task(3, "Low priority"),
    Task(1, "High priority"),
    Task(2, "Medium priority"),
]

sorted_tasks = sorted(tasks)
```

### Slots (Memory Optimization)

```python
@dataclass(slots=True)
class OptimizedPoint:
    x: float
    y: float


p = OptimizedPoint(1.0, 2.0)
```

**Benefits:**

- Faster attribute access
- Reduced memory usage (20-30% savings)
- Prevents dynamic attribute assignment

**Benchmark:** For 1 million instances, slots can save ~50MB of memory.

### Post-Init Processing

```python
from dataclasses import dataclass, field


@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self):
        self.area = self.width * self.height


r = Rectangle(5.0, 3.0)
print(r.area)
```

### InitVar Fields

```python
from dataclasses import dataclass, InitVar, field


@dataclass
class DatabaseRecord:
    name: str
    database_url: InitVar[str]
    connection: object = field(init=False)

    def __post_init__(self, database_url: str):
        self.connection = create_connection(database_url)
```

**Note:** InitVar fields are passed to `__post_init__()` but not stored as attributes.

### Frozen + Post-Init

```python
@dataclass(frozen=True)
class ProcessedData:
    raw_value: str
    processed: str = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'processed', self.raw_value.upper())


data = ProcessedData("hello")
print(data.processed)
```

## Utility Functions

### asdict() and astuple()

```python
from dataclasses import dataclass, asdict, astuple


@dataclass
class Person:
    name: str
    age: int
    city: str


p = Person("Alice", 30, "NYC")
print(asdict(p))
print(astuple(p))
```

**Performance Note:** `asdict()` uses deep copy, which is slow for large structures.

Fast alternative:

```python
from dataclasses import fields

data = {f.name: getattr(obj, f.name) for f in fields(obj)}
```

### replace()

```python
from dataclasses import replace

p1 = Person("Alice", 30, "NYC")
p2 = replace(p1, age=31)
print(p2)
```

### fields()

```python
from dataclasses import fields

for f in fields(Person):
    print(f"{f.name}: {f.type}")
```

## Inheritance

```python
@dataclass
class Animal:
    name: str
    age: int


@dataclass
class Dog(Animal):
    breed: str


dog = Dog("Buddy", 5, "Golden Retriever")
```

## Generics

```python
from dataclasses import dataclass


@dataclass
class Box[T]:
    value: T


int_box = Box[int](42)
str_box = Box[str]("hello")
```

## Nested Dataclasses

```python
@dataclass
class Address:
    street: str
    city: str
    country: str


@dataclass
class Person:
    name: str
    address: Address


person = Person(
    name="Alice",
    address=Address("123 Main St", "NYC", "USA")
)
```

## Comparison with Alternatives

| Feature        | Dataclass         | NamedTuple | Regular Class |
|----------------|-------------------|------------|---------------|
| Mutability     | Mutable (default) | Immutable  | Mutable       |
| Performance    | Fast              | Fastest    | Medium        |
| Memory         | Good              | Best       | Worst         |
| Type Hints     | Yes               | Yes        | Optional      |
| Inheritance    | Full support      | Limited    | Full support  |
| Default Values | Yes               | Yes        | Yes           |
| Post Init      | Yes               | No         | Yes           |
| Slots          | Yes (3.10+)       | Automatic  | Manual        |

## When to Use Dataclasses

### Use Dataclasses When:

- Creating simple data containers
- Need automatic method generation
- Type hints are important
- Want mutability or immutability options
- Building internal domain objects
- Performance matters
- Avoiding external dependencies

### Don't Use Dataclasses When:

- Need data validation (use Pydantic)
- Parsing untrusted external data (use Pydantic)
- Need JSON schema generation (use Pydantic)
- Require complex serialization logic

## Best Practices

### 1. Always Use Type Hints

```python
@dataclass
class Good:
    name: str
    count: int
```

### 2. Use default_factory for Mutable Defaults

```python
@dataclass
class Config:
    items: list[str] = field(default_factory=list)
    settings: dict[str, int] = field(default_factory=dict)
```

### 3. Use frozen=True for Value Objects

```python
@dataclass(frozen=True)
class Money:
    amount: float
    currency: str
```

### 4. Use slots=True for Memory Optimization

```python
@dataclass(slots=True)
class Event:
    timestamp: float
    event_type: str
    data: dict[str, str]
```

### 5. Use Field Options Appropriately

```python
@dataclass
class User:
    username: str
    email: str
    password: str = field(repr=False)
    created_at: float = field(compare=False, default=0.0)
    _internal_id: int = field(init=False, repr=False, default=0)
```

## Common Pitfalls

### Mutable Default Values

```python
@dataclass
class Bad:
    items: list[str] = []


@dataclass
class Good:
    items: list[str] = field(default_factory=list)
```

### Modifying Frozen Dataclasses

```python
@dataclass(frozen=True)
class Point:
    x: float
    y: float


p = Point(1.0, 2.0)

p2 = replace(p, x=3.0)
```

### Field Ordering with Defaults

```python
@dataclass
class Person:
    name: str
    age: int = 0
    city: str
```

## Real-World Examples

### Domain Model

```python
@dataclass(frozen=True)
class Order:
    order_id: int
    user_id: int
    items: tuple[str, ...]
    total: float
    status: str = "pending"


@dataclass(frozen=True)
class OrderItem:
    product_id: int
    quantity: int
    price: float
```

### Configuration

```python
@dataclass(frozen=True)
class DatabaseConfig:
    host: str
    port: int
    database: str
    username: str
    password: str = field(repr=False)
    pool_size: int = 10


config = DatabaseConfig(
    host="localhost",
    port=5432,
    database="mydb",
    username="admin",
    password="secret"
)
```

### Event Sourcing

```python
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Event:
    event_id: int
    event_type: str
    timestamp: datetime
    payload: dict[str, str]


@dataclass(frozen=True, slots=True)
class UserCreatedEvent(Event):
    user_id: int
    username: str
```

## Performance Considerations

**Creation Speed** (relative to dict = 1.0x):

- Dict: 1.0x
- Dataclass: 1.3x
- Dataclass with slots: 1.2x
- NamedTuple: 1.1x

**Memory Usage** (per 1M instances):

- Dict: ~320 MB
- Dataclass: ~280 MB
- Dataclass with slots: ~220 MB
- NamedTuple: ~200 MB

## Summary

- Dataclasses reduce boilerplate for data-centric classes
- Use `frozen=True` for immutability
- Use `slots=True` for memory optimization
- Use `field()` for advanced options
- Use `__post_init__()` for computed fields
- Always use `default_factory` for mutable defaults
- Perfect for internal domain objects
- Use Pydantic for validation needs
