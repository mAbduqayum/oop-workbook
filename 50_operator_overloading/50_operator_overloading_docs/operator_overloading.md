# Object-Oriented Programming: Operator Overloading

## What is Operator Overloading?

**Operator overloading** allows you to define how standard Python operators (`+`, `-`, `*`, `/`, `==`, `<`, etc.) work with your custom classes. It's about giving custom meaning to operators when they're used with your objects.

Think of it this way: When you write `3 + 5`, Python knows how to add integers. When you write `"Hello" + "World"`, Python knows how to concatenate strings. With operator overloading, you can teach Python how to add your own custom objects, like `Vector2D(1, 2) + Vector2D(3, 4)`.

**Key Insight:** Operator overloading makes your custom classes feel like built-in types, creating more intuitive and readable code.

## Real-World Analogy

**The Universal Remote:**
- The same button (`+`) does different things with different devices (TV volume, music player track, game players)
- The operator has different meanings depending on the object type
- The interface is consistent, but the behavior is customized

## Common Magic Methods for Operator Overloading

Python uses special "magic methods" (also called "dunder methods" for double underscore) to implement operator overloading:

### Arithmetic Operators

| Operator | Method                      | Example  | Description    |
|----------|-----------------------------|----------|----------------|
| `+`      | `__add__(self, other)`      | `a + b`  | Addition       |
| `-`      | `__sub__(self, other)`      | `a - b`  | Subtraction    |
| `*`      | `__mul__(self, other)`      | `a * b`  | Multiplication |
| `/`      | `__truediv__(self, other)`  | `a / b`  | Division       |
| `//`     | `__floordiv__(self, other)` | `a // b` | Floor division |
| `%`      | `__mod__(self, other)`      | `a % b`  | Modulo         |
| `**`     | `__pow__(self, other)`      | `a ** b` | Power          |

### Comparison Operators

| Operator | Method                | Example  | Description           |
|----------|-----------------------|----------|-----------------------|
| `==`     | `__eq__(self, other)` | `a == b` | Equal to              |
| `!=`     | `__ne__(self, other)` | `a != b` | Not equal to          |
| `<`      | `__lt__(self, other)` | `a < b`  | Less than             |
| `<=`     | `__le__(self, other)` | `a <= b` | Less than or equal    |
| `>`      | `__gt__(self, other)` | `a > b`  | Greater than          |
| `>=`     | `__ge__(self, other)` | `a >= b` | Greater than or equal |

### Unary Operators

| Operator | Method          | Example  | Description    |
|----------|-----------------|----------|----------------|
| `-`      | `__neg__(self)` | `-a`     | Negation       |
| `+`      | `__pos__(self)` | `+a`     | Unary plus     |
| `abs()`  | `__abs__(self)` | `abs(a)` | Absolute value |

### String Representation

| Method           | Function                   | Description                       |
|------------------|----------------------------|-----------------------------------|
| `__str__(self)`  | `str(obj)` or `print(obj)` | Human-readable string             |
| `__repr__(self)` | `repr(obj)`                | Developer-friendly representation |

### In-Place Operators

| Operator | Method                      | Example  | Description             |
|----------|-----------------------------|----------|-------------------------|
| `+=`     | `__iadd__(self, other)`     | `a += b` | In-place addition       |
| `-=`     | `__isub__(self, other)`     | `a -= b` | In-place subtraction    |
| `*=`     | `__imul__(self, other)`     | `a *= b` | In-place multiplication |
| `/=`     | `__itruediv__(self, other)` | `a /= b` | In-place division       |

## Basic Example Structure

When implementing operator overloading, you typically need:

```python
from typing import Self


class MyClass:
    def __init__(self, value: int) -> None:
        self.value = value
    
    def __add__(self, other: Self) -> Self:
        """Define addition behavior"""
        if isinstance(other, MyClass):
            # Implement addition logic
            return MyClass(self.value + other.value)
        return NotImplemented
    
    def __eq__(self, other: object) -> bool:
        """Define equality behavior"""
        if isinstance(other, MyClass):
            return self.value == other.value
        return False
    
    def __str__(self) -> str:
        """Human-readable representation"""
        return f"MyClass({self.value})"
    
    def __repr__(self) -> str:
        """Developer representation"""
        return f"MyClass({self.value})"
```

## Right-Hand and In-Place Operations

### Right-Hand Operations (`__radd__`, `__rmul__`, etc.)

When Python evaluates `a + b`, it first tries `a.__add__(b)`. If that returns `NotImplemented`, it tries `b.__radd__(a)`.

**Pattern:**
```python
from typing import Self


def __radd__(self, other: Self) -> Self:
    """Right-hand addition: allows 5 + my_object"""
    return self.__add__(other)  # Usually delegates to __add__
```

### In-Place Operations (`__iadd__`, `__imul__`, etc.)

In-place operators like `+=` modify the object instead of creating a new one:

**Pattern:**
```python
from typing import Self


def __iadd__(self, other: Self) -> Self:
    """In-place addition: modifies self"""
    if isinstance(other, MyClass):
        self.value += other.value
    else:
        return NotImplemented
    return self  # Must return self!
```

## Best Practices for Operator Overloading

### 1. **Follow the Principle of The Least Surprise**

Operators should do what users expect:

```python
from typing import Self


# ✅ GOOD - Intuitive behavior
class Point:
    def __add__(self, other: Self) -> Self:
        """Adding points makes sense"""
        return Point(self.x + other.x, self.y + other.y)

# ❌ BAD - Surprising behavior
class Person:
    def __add__(self, other: Self) -> str:
        """Adding people? What does this even mean?"""
        return f"{self.name} and {other.name}"  # Confusing!
```

### 2. **Return `NotImplemented` for Unsupported Types**

Let Python try alternative approaches:

```python
from typing import Self


def __add__(self, other: Self) -> Self:
    if isinstance(other, Vector2D):
        return Vector2D(self.x + other.x, self.y + other.y)
    # Don't raise TypeError! Return NotImplemented
    return NotImplemented
```

### 3. **Be Consistent Across Related Operators**

If you implement `__eq__`, consider implementing other comparisons:

```python
from typing import Self


class Money:
    def __eq__(self, other: object) -> bool:
        return self.amount == other.amount
    
    def __lt__(self, other: Self) -> bool:
        return self.amount < other.amount
    
    def __le__(self, other: Self) -> bool:
        return self.amount <= other.amount
    
    # __gt__ and __ge__ are automatically derived
```

### 4. **Implement `__str__` and `__repr__`**

Always provide string representations:

```python
def __str__(self) -> str:
    """For end users: print(obj)"""
    return f"Vector({self.x}, {self.y})"

def __repr__(self) -> str:
    """For developers: repr(obj)"""
    return f"Vector2D({self.x}, {self.y})"
```

### 5. **Handle Type Errors Gracefully**

Check types and return `NotImplemented`:

```python
from typing import Self


def __add__(self, other: Self | int | float) -> Self:
    if isinstance(other, Vector2D):
        return Vector2D(self.x + other.x, self.y + other.y)
    elif isinstance(other, (int, float)):
        # Maybe allow adding a scalar
        return Vector2D(self.x + other, self.y + other)
    return NotImplemented  # Let Python handle the error
```


## Common Pitfalls to Avoid

### ❌ Pitfall 1: Not Returning the Correct Type

```python
from typing import Self


# BAD - Returns wrong type
class Vector2D:
    def __add__(self, other: Self) -> tuple:  # Wrong return type!
        return (self.x + other.x, self.y + other.y)  # Returns tuple!

# GOOD - Returns the same type
class Vector2D:
    def __add__(self, other: Self) -> Self:
        return Vector2D(self.x + other.x, self.y + other.y)
```

### ❌ Pitfall 2: Modifying Self in Regular Operators

```python
from typing import Self


# BAD - Modifies self
class Point:
    def __add__(self, other: Self) -> Self:
        self.x += other.x  # Don't modify self!
        return self

# GOOD - Creates a new object
class Point:
    def __add__(self, other: Self) -> Self:
        return Point(self.x + other.x, self.y + other.y)
```

### ❌ Pitfall 3: Raising TypeError Instead of Returning NotImplemented

```python
from typing import Self


# BAD - Raises error immediately
class Vector2D:
    def __add__(self, other: Self) -> Self:
        if not isinstance(other, Vector2D):
            raise TypeError("Can only add Vector2D")
        return Vector2D(self.x + other.x, self.y + other.y)

# GOOD - Returns NotImplemented
class Vector2D:
    def __add__(self, other: Self) -> Self:
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented  # Let Python try __radd__
```
