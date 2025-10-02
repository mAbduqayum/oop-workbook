# Python OOP Practice - Abstraction: Shape Hierarchy

## Exercise: Abstract Base Class for Geometric Shapes

Create an abstract `Shape` class and concrete implementations that demonstrate abstraction through geometric shape calculations.

**Instructions:**
Implement a shape hierarchy using Abstract Base Classes (ABC) to enforce that all shapes must calculate their area and perimeter.

This exercise demonstrates how abstraction creates clear contracts that all implementations must follow.

**Your Complete Task:**
1. Create an abstract `Shape` class that inherits from `ABC`
2. Add constructor with `color` parameter (string)
3. Add abstract method `area()` that returns a float
4. Add abstract method `perimeter()` that returns a float
5. Create `Rectangle` class that inherits from `Shape`:
   - Constructor parameters: `color`, `width`, `height`
   - Implement `area()` to return `width * height`
   - Implement `perimeter()` to return `2 * (width + height)`
6. Create `Circle` class that inherits from `Shape`:
   - Constructor parameters: `color`, `radius`
   - Implement `area()` to return `π * radius²`
   - Implement `perimeter()` to return `2 * π * radius`
7. Create `Triangle` class that inherits from `Shape`:
   - Constructor parameters: `color`, `base`, `height`, `side1`, `side2`, `side3`
   - Implement `area()` to return `0.5 * base * height`
   - Implement `perimeter()` to return `side1 + side2 + side3`

**What You'll Learn:**
- **Abstract Base Classes:** Using ABC to create interfaces
- **Abstract Methods:** Enforcing method implementation in child classes
- **Contract Enforcement:** Python prevents instantiation of incomplete classes
- **Polymorphic Design:** All shapes share the same interface

**Example Usage:**
```python
from abc import ABC, abstractmethod
import math

# This should fail - cannot instantiate abstract class
try:
    shape = Shape("red")
except TypeError as e:
    print(f"Error: {e}")

# Create concrete shapes
rectangle = Rectangle("red", 10, 5)
circle = Circle("blue", 7)
triangle = Triangle("green", 6, 4, 5, 5, 6)

# All shapes have area() and perimeter()
print(f"Rectangle area: {rectangle.area():.2f}")        # 50.00
print(f"Rectangle perimeter: {rectangle.perimeter():.2f}") # 30.00

print(f"Circle area: {circle.area():.2f}")              # 153.94
print(f"Circle perimeter: {circle.perimeter():.2f}")    # 43.98

print(f"Triangle area: {triangle.area():.2f}")          # 12.00
print(f"Triangle perimeter: {triangle.perimeter():.2f}") # 16.00

# Function that works with ANY shape
def print_shape_info(shape: Shape):
    print(f"{shape.color} {shape.__class__.__name__}")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")

shapes = [rectangle, circle, triangle]
for shape in shapes:
    print_shape_info(shape)
```

**Key Abstraction Concepts:**
- **Cannot instantiate abstract classes** - `Shape` is a template, not a concrete object
- **Enforced implementation** - All child classes MUST implement `area()` and `perimeter()`
- **Clear contract** - Anyone using a `Shape` knows these methods exist
- **Polymorphic interface** - Functions can work with any `Shape` subclass
