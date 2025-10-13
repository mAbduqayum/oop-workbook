# Python Type Hinting Guide

## What is Type Hinting?

Type hinting is a way to explicitly specify what type of data a variable, parameter, or return value should be. Python is dynamically typed, meaning you don't *have* to specify types, but type hints make your code more readable, catch bugs early, and enable better IDE support.

**Think of it as adding labels:** Instead of mystery boxes, you label each box with what's inside.

## Why Use Type Hints?

1. **Better Documentation** - Code becomes self-explanatory
2. **Early Bug Detection** - Catch type errors before runtime
3. **IDE Support** - Better autocomplete and suggestions
4. **Maintainability** - Easier for others (and future you) to understand

## Basic Type Hints

### Variable Type Hints

```python
# Basic types
name: str = "Alice"
age: int = 25
height: float = 5.8
is_student: bool = True

# Without initial value
score: int
score = 95
```

### Function Parameter and Return Type Hints

```python
def greet(name: str) -> str:
    """Returns a greeting message"""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """Adds two integers and returns the sum"""
    return a + b

def print_info(name: str, age: int) -> None:
    """Prints info, returns nothing (None)"""
    print(f"{name} is {age} years old")
```

## Type Hints in Classes

### Basic Class with Type Hints

```python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
    
    def get_info(self) -> str:
        return f"{self.name} is {self.age} years old"
    
    def have_birthday(self) -> None:
        self.age += 1
```

### Class with More Complex Types

```python
class Student:
    def __init__(self, name: str, student_id: str, grades: list[float]) -> None:
        self.name: str = name
        self.student_id: str = student_id
        self.grades: list[float] = grades
    
    def add_grade(self, grade: float) -> None:
        self.grades.append(grade)
    
    def get_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def get_grades(self) -> list[float]:
        return self.grades
```

## Common Built-in Type Hints

### Collections

```python
# Lists
numbers: list[int] = [1, 2, 3, 4, 5]
names: list[str] = ["Alice", "Bob", "Charlie"]

# Tuples (fixed size)
coordinates: tuple[float, float] = (10.5, 20.3)
rgb_color: tuple[int, int, int] = (255, 128, 0)

# Dictionaries
student_grades: dict[str, float] = {"Alice": 95.5, "Bob": 87.3}
config: dict[str, int] = {"timeout": 30, "max_retries": 3}

# Sets
unique_ids: set[int] = {1, 2, 3, 4, 5}
tags: set[str] = {"python", "programming", "oop"}
```

### Optional Values

```python
from typing import Optional

# Optional means "can be the type OR None"
def find_student(student_id: str) -> Optional[str]:
    """Returns student name or None if not found"""
    if student_id == "123":
        return "Alice"
    return None

# Modern syntax (Python 3.10+)
def get_user_email(user_id: int) -> str | None:
    """Returns email or None"""
    if user_id > 0:
        return "user@example.com"
    return None
```

## Advanced Type Hints for OOP

### Type Hints with Inheritance

```python
class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
    
    def make_sound(self) -> str:
        return "Some sound"


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)
        self.breed: str = breed
    
    def make_sound(self) -> str:
        return f"{self.name} says: Woof!"
    
    def fetch(self, item: str) -> str:
        return f"{self.name} fetched the {item}!"
```

### Self-Referencing Types

```python
from __future__ import annotations

class BankAccount:
    def __init__(self, holder: str, balance: float) -> None:
        self.holder: str = holder
        self._balance: float = balance
    
    def transfer_to(self, recipient: BankAccount, amount: float) -> bool:
        """Transfer money to another BankAccount"""
        if self._balance >= amount:
            self._balance -= amount
            recipient._balance += amount
            return True
        return False
```

### Union Types (Multiple Possible Types)

```python
from typing import Union

# Old syntax
def process_id(user_id: Union[int, str]) -> str:
    """Accepts either int or str"""
    return str(user_id)

# Modern syntax (Python 3.10+)
def process_value(value: int | float | str) -> str:
    """Accepts int, float, or str"""
    return str(value)
```

## Type Hints with Abstract Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color: str) -> None:
        self.color: str = color
    
    @abstractmethod
    def area(self) -> float:
        """Calculate area - must be implemented"""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate perimeter - must be implemented"""
        pass


class Rectangle(Shape):
    def __init__(self, color: str, width: float, height: float) -> None:
        super().__init__(color)
        self.width: float = width
        self.height: float = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
```

## Polymorphism with Type Hints

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Process payment and return success status"""
        pass


class CreditCard(PaymentMethod):
    def __init__(self, card_number: str, cvv: str) -> None:
        self.card_number: str = card_number
        self.cvv: str = cvv
    
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount} via Credit Card")
        return True


class PayPal(PaymentMethod):
    def __init__(self, email: str) -> None:
        self.email: str = email
    
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount} via PayPal")
        return True


def checkout(payment: PaymentMethod, total: float) -> None:
    """Works with any PaymentMethod subclass"""
    payment.process_payment(total)
```

## Special Typing Module Types

### Any (Accepts Anything)

```python
from typing import Any

def print_value(value: Any) -> None:
    """Accepts any type"""
    print(value)
```

### Callable (Functions as Parameters)

```python
from typing import Callable

def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    """Takes a function as parameter"""
    return operation(x, y)

def add(a: int, b: int) -> int:
    return a + b

result = apply_operation(5, 3, add)  # Works!
```

### Generic Types

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Box(Generic[T]):
    """A generic box that can hold any type"""
    def __init__(self, item: T) -> None:
        self.item: T = item
    
    def get_item(self) -> T:
        return self.item

# Create boxes with different types
int_box: Box[int] = Box(42)
str_box: Box[str] = Box("Hello")
```

## Type Hints with Properties

```python
class BankAccount:
    def __init__(self, holder: str, balance: float) -> None:
        self.holder: str = holder
        self._balance: float = balance
    
    @property
    def balance(self) -> float:
        """Getter with return type hint"""
        return self._balance
    
    @balance.setter
    def balance(self, amount: float) -> None:
        """Setter with parameter type hint"""
        if amount >= 0:
            self._balance = amount
```

## Practical Example: Complete Class with Type Hints

```python
from typing import Optional

class Library:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.books: dict[str, int] = {}  # book_title -> quantity
    
    def add_book(self, title: str, quantity: int = 1) -> None:
        """Add books to the library"""
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity
    
    def remove_book(self, title: str, quantity: int = 1) -> bool:
        """Remove books from library, returns success status"""
        if title in self.books and self.books[title] >= quantity:
            self.books[title] -= quantity
            if self.books[title] == 0:
                del self.books[title]
            return True
        return False
    
    def get_quantity(self, title: str) -> int:
        """Get quantity of a specific book"""
        return self.books.get(title, 0)
    
    def list_books(self) -> list[str]:
        """Get list of all book titles"""
        return list(self.books.keys())
    
    def find_book(self, title: str) -> Optional[int]:
        """Find book and return quantity, or None if not found"""
        return self.books.get(title)


# Usage with type hints
library: Library = Library("City Library")
library.add_book("Python Basics", 5)
library.add_book("OOP Guide", 3)

quantity: int = library.get_quantity("Python Basics")
all_books: list[str] = library.list_books()
```

## Common Mistakes to Avoid

### ❌ Don't Over-Complicate

```python
# Too complex
from typing import Union, Optional, List, Dict, Tuple

def process(data: Union[List[Dict[str, Union[int, str]]], Tuple[int, ...], None]) -> Optional[Dict[str, Union[int, float]]]:
    pass

# Better - keep it simple
def process(data: list[dict] | None) -> dict | None:
    pass
```

### ❌ Don't Forget `-> None` for Methods

```python
# Wrong
def __init__(self, name: str):
    self.name = name

# Correct
def __init__(self, name: str) -> None:
    self.name = name
```

### ✅ Use Modern Syntax (Python 3.10+)

```python
# Old style
from typing import List, Dict, Optional

def get_scores() -> Optional[List[int]]:
    pass

# Modern style (Python 3.10+)
def get_scores() -> list[int] | None:
    pass
```

## Type Checking Tools

### Using mypy

```bash
# Install mypy
pip install mypy

# Check your code
mypy your_script.py
```

### Using IDE Support

Most modern IDEs (VS Code, PyCharm) automatically check type hints and show warnings.

## Quick Reference

| Type | Example | Description |
|------|---------|-------------|
| `int` | `age: int = 25` | Integer numbers |
| `float` | `price: float = 19.99` | Decimal numbers |
| `str` | `name: str = "Alice"` | Text strings |
| `bool` | `is_active: bool = True` | True/False values |
| `list[T]` | `numbers: list[int]` | List of items |
| `dict[K, V]` | `scores: dict[str, int]` | Key-value pairs |
| `tuple[T, ...]` | `point: tuple[int, int]` | Fixed-size tuple |
| `set[T]` | `tags: set[str]` | Unique items |
| `None` | `-> None` | Returns nothing |
| `Optional[T]` | `Optional[str]` | Value or None |
| `T \| None` | `str \| None` | Modern optional |
| `Any` | `value: Any` | Any type |

## Key Takeaways

✅ **Type hints are optional** but highly recommended

✅ **Improve code readability** and catch bugs early

✅ **IDE support** gets much better with type hints

✅ **Use modern syntax** (`list[int]` instead of `List[int]`)

✅ **Always add `-> None`** to `__init__` methods

✅ **Start simple** - don't over-complicate type hints

✅ **Use type checking tools** like `mypy` to verify correctness

**Remember:** Type hints are documentation that Python can check. They make your OOP code clearer and more maintainable!
