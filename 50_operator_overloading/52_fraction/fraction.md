# Python OOP Practice - Operator Overloading: Fraction Class

## Exercise: Rational Number Arithmetic with Operators

Create a `Fraction` class that represents rational numbers (fractions) and supports arithmetic operations using operator overloading. Fractions are automatically reduced to lowest terms.

**Instructions:**
Implement a fraction class that handles proper fraction arithmetic with automatic simplification. This demonstrates how operator overloading can make mathematical operations intuitive while maintaining mathematical correctness.

This exercise shows the power of operator overloading for creating custom numeric types that behave like built-in numbers.

**Your Complete Task:**
1. Create a `Fraction` class with constructor parameters:
   - `numerator` (int): The numerator
   - `denominator` (int, default=1): The denominator
   - Automatically reduce to lowest terms using GCD
   - Keep denominator positive (move negative sign to numerator)
   - Raise `ZeroDivisionError` if denominator is zero
2. Implement `__add__(self, other)` for addition
   - Fraction + Fraction: `a/b + c/d = (ad + bc)/bd`
   - Fraction + int: Convert int to fraction first
3. Implement `__sub__(self, other)` for subtraction
   - Fraction - Fraction: `a/b - c/d = (ad - bc)/bd`
4. Implement `__mul__(self, other)` for multiplication
   - Fraction * Fraction: `(a/b) * (c/d) = (ac)/(bd)`
   - Fraction * int: `(a/b) * c = (ac)/b`
5. Implement `__truediv__(self, other)` for division
   - Fraction / Fraction: `(a/b) / (c/d) = (ad)/(bc)`
   - Raise `ZeroDivisionError` if dividing by zero
6. Implement `__eq__(self, other)` for equality
7. Implement `__lt__(self, other)` for less than comparison
8. Implement `__le__(self, other)` for less than or equal
9. Implement `__gt__(self, other)` for greater than
10. Implement `__ge__(self, other)` for greater than or equal
11. Implement `__neg__(self)` for negation: `-a/b = (-a)/b`
12. Implement `__abs__(self)` for absolute value: `|a/b| = |a|/b`
13. Implement `__float__(self)` for float conversion
14. Implement `__int__(self)` for integer conversion (truncate)
15. Implement `__str__(self)` to return `"numerator/denominator"` (or just `"numerator"` if denominator is 1)
16. Implement `__repr__(self)` to return `"Fraction(numerator, denominator)"`
17. Add `reciprocal(self)` method that returns `denominator/numerator`
    - Raise `ZeroDivisionError` if numerator is zero

**What You'll Learn:**
- **Automatic simplification:** Reduce fractions to lowest terms
- **Mathematical operators:** Implement all arithmetic operations
- **Comparison operators:** Compare fractions properly
- **Type conversion:** Convert to float and int
- **Edge cases:** Handle zero denominators and negative fractions
- **Mixed operations:** Support operations between fractions and integers

**Mathematical Background:**
- **GCD:** Greatest Common Divisor simplifies fractions
- **Addition:** Requires common denominator
- **Multiplication:** Multiply numerators and denominators
- **Division:** Multiply by reciprocal
- **Comparison:** Cross-multiply to compare

**Example Usage:**
```python
import math

# Create fractions
f1 = Fraction(1, 2)  # 1/2
f2 = Fraction(1, 3)  # 1/3
f3 = Fraction(2, 4)  # Automatically reduced to 1/2

# Automatic reduction
print(f3)  # 1/2 (not 2/4)
print(Fraction(6, 9))  # 2/3

# Addition
f4 = f1 + f2
print(f4)  # 5/6

# Subtraction
f5 = f1 - f2
print(f5)  # 1/6

# Multiplication
f6 = f1 * f2
print(f6)  # 1/6

# Division
f7 = f1 / f2
print(f7)  # 3/2

# Mixed operations with integers
f8 = f1 + 1
print(f8)  # 3/2

f9 = Fraction(3, 4) * 2
print(f9)  # 3/2

# Comparison operators
print(f1 > f2)  # True (1/2 > 1/3)
print(f1 == Fraction(2, 4))  # True (automatically reduced)
print(Fraction(1, 2) < Fraction(2, 3))  # True

# Negation
f10 = -f1
print(f10)  # -1/2

# Absolute value
f11 = abs(Fraction(-3, 4))
print(f11)  # 3/4

# Reciprocal
f12 = Fraction(2, 3).reciprocal()
print(f12)  # 3/2

# Type conversion
print(float(Fraction(1, 2)))  # 0.5
print(int(Fraction(5, 2)))  # 2

# Complex expressions
result = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 6)
print(result)  # 1

# Practical example: splitting a pizza
pizza = Fraction(1, 1)  # One whole pizza
slice1 = Fraction(1, 8)  # 1/8 of pizza
slice2 = Fraction(1, 4)  # 1/4 of pizza

eaten = slice1 + slice2 + slice1
print(f"Eaten: {eaten}")  # 1/2
remaining = pizza - eaten
print(f"Remaining: {remaining}")  # 1/2

# Recipe scaling
recipe_flour = Fraction(2, 3)  # 2/3 cup
scale_factor = Fraction(3, 2)  # Make 1.5x the recipe
new_amount = recipe_flour * scale_factor
print(f"Scaled flour: {new_amount} cups")  # 1 cups

# Negative fractions handled correctly
print(Fraction(-1, 2))  # -1/2
print(Fraction(1, -2))  # -1/2 (negative moved to numerator)
print(Fraction(-1, -2))  # 1/2 (both negatives cancel)

# Error handling
try:
    invalid = Fraction(1, 0)
except ZeroDivisionError as e:
    print(e)  # Denominator cannot be zero

try:
    reciprocal_zero = Fraction(0, 1).reciprocal()
except ZeroDivisionError as e:
    print(e)  # Cannot get reciprocal of zero

try:
    div_by_zero = f1 / Fraction(0, 1)
except ZeroDivisionError as e:
    print(e)  # Cannot divide by zero

# Chaining operations
result2 = (Fraction(1, 2) + Fraction(1, 4)) * Fraction(2, 3) / Fraction(1, 2)
print(result2)  # 1
```

**Key Operator Overloading Concepts:**
- **Automatic normalization:** Fractions always in simplest form
- **Mathematical correctness:** Follows proper fraction arithmetic rules
- **Natural syntax:** Use standard arithmetic operators
- **Type flexibility:** Works with both fractions and integers
- **Immutability:** Operations create new fractions, don't modify originals

**Test Cases to Consider:**
```python
# Identity operations
assert Fraction(1, 2) + Fraction(0, 1) == Fraction(1, 2)
assert Fraction(1, 2) * Fraction(1, 1) == Fraction(1, 2)

# Automatic reduction
assert Fraction(2, 4) == Fraction(1, 2)
assert Fraction(6, 9) == Fraction(2, 3)

# Negative handling
assert Fraction(-1, 2) == Fraction(1, -2)
assert Fraction(-1, -2) == Fraction(1, 2)

# Mixed operations
assert Fraction(1, 2) + 1 == Fraction(3, 2)
assert Fraction(3, 4) * 2 == Fraction(3, 2)

# Comparisons
assert Fraction(1, 2) > Fraction(1, 3)
assert Fraction(1, 2) == Fraction(2, 4)
assert Fraction(1, 3) < Fraction(1, 2)

# Edge cases
assert Fraction(0, 5) == Fraction(0, 1)
assert abs(Fraction(-3, 4)) == Fraction(3, 4)
```

**Challenge Extensions:**
- Implement `__radd__`, `__rsub__`, `__rmul__`, `__rtruediv__` for right-hand operations
- Add `__pow__(self, exponent)` for fraction exponentiation
- Implement `__iadd__`, `__imul__` for in-place operations
- Add `simplify()` method (already done in `__init__`)
- Implement `mixed_number()` method to return (whole, numerator, denominator)
- Add support for continued fraction representation
- Implement `__hash__()` to make fractions hashable (usable in sets/dicts)
- Add `from_decimal(decimal_str)` class method
