# Exercise: Geometric Shapes Hierarchy

Create a geometric shapes system using inheritance to demonstrate polymorphism and method overriding.

## Requirements

Design an inheritance hierarchy for geometric shapes:

### Base Class: `Shape`
- **Attributes:**
  - `color` (string): Shape's color
  - `x` (float): X coordinate
  - `y` (float): Y coordinate

- **Methods:**
  - `__init__(color, x, y)`: Constructor
  - `area()`: Calculate area (to be overridden)
  - `perimeter()`: Calculate perimeter (to be overridden)
  - `move(new_x, new_y)`: Move shape to new position
  - `get_info()`: Return basic shape information

### Derived Classes

#### `Rectangle` (inherits from Shape)
- **Additional Attributes:**
  - `width` (float): Rectangle width
  - `height` (float): Rectangle height

- **Override Methods:**
  - `area()`: Return width × height
  - `perimeter()`: Return 2 × (width + height)
- **Additional Methods:**
  - `is_square()`: Check if rectangle is a square
  - `resize(new_width, new_height)`: Change dimensions

#### `Circle` (inherits from Shape)
- **Additional Attributes:**
  - `radius` (float): Circle radius

- **Override Methods:**
  - `area()`: Return π × radius²
  - `perimeter()`: Return 2 × π × radius
- **Additional Methods:**
  - `diameter()`: Return diameter
  - `set_radius(new_radius)`: Change radius

#### `Triangle` (inherits from Shape)
- **Additional Attributes:**
  - `side_a` (float): First side length
  - `side_b` (float): Second side length
  - `side_c` (float): Third side length

- **Override Methods:**
  - `area()`: Return area using Heron's formula
  - `perimeter()`: Return sum of all sides
- **Additional Methods:**
  - `is_valid()`: Check if triangle is valid (triangle inequality)
  - `triangle_type()`: Return "equilateral", "isosceles", or "scalene"

## Example Usage

```python
import math

# Create different shapes
rectangle = Rectangle("blue", 0, 0, 5, 3)
circle = Circle("red", 10, 10, 4)
triangle = Triangle("green", 5, 5, 3, 4, 5)

# Display basic information
print("Rectangle:")
print(f"Color: {rectangle.color}")
print(f"Position: ({rectangle.x}, {rectangle.y})")
print(f"Dimensions: {rectangle.width} × {rectangle.height}")
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")
print(f"Is square: {rectangle.is_square()}")

print("\nCircle:")
print(f"Color: {circle.color}")
print(f"Position: ({circle.x}, {circle.y})")
print(f"Radius: {circle.radius}")
print(f"Diameter: {circle.diameter()}")
print(f"Area: {circle.area():.2f}")
print(f"Perimeter: {circle.perimeter():.2f}")

print("\nTriangle:")
print(f"Color: {triangle.color}")
print(f"Position: ({triangle.x}, {triangle.y})")
print(f"Sides: {triangle.side_a}, {triangle.side_b}, {triangle.side_c}")
print(f"Is valid: {triangle.is_valid()}")
print(f"Type: {triangle.triangle_type()}")
print(f"Area: {triangle.area():.2f}")
print(f"Perimeter: {triangle.perimeter()}")

# Demonstrate polymorphism
shapes = [rectangle, circle, triangle]
print("\nAll shapes areas:")
for shape in shapes:
    print(f"{shape.color} shape: {shape.area():.2f}")

print("\nAll shapes perimeters:")
for shape in shapes:
    print(f"{shape.color} shape: {shape.perimeter():.2f}")

# Move shapes
rectangle.move(2, 3)
print(f"\nRectangle moved to: ({rectangle.x}, {rectangle.y})")

# Resize rectangle
rectangle.resize(6, 6)
print(f"Rectangle resized to: {rectangle.width} × {rectangle.height}")
print(f"Is square now: {rectangle.is_square()}")
```

## Expected Output

```
Rectangle:
Color: blue
Position: (0, 0)
Dimensions: 5 × 3
Area: 15
Perimeter: 16
Is square: False

Circle:
Color: red
Position: (10, 10)
Radius: 4
Diameter: 8
Area: 50.27
Perimeter: 25.13

Triangle:
Color: green
Position: (5, 5)
Sides: 3, 4, 5
Is valid: True
Type: scalene
Area: 6.00
Perimeter: 12

All shapes areas:
blue shape: 15.00
red shape: 50.27
green shape: 6.00

All shapes perimeters:
blue shape: 16.00
red shape: 25.13
green shape: 12.00

Rectangle moved to: (2, 3)
Rectangle resized to: 6 × 6
Is square now: True
```

## Learning Objectives

- Practice inheritance with mathematical concepts
- Learn to override methods for different calculations
- Understand polymorphism with geometric shapes
- Work with mathematical formulas in object-oriented context
- Implement validation methods (triangle inequality)
- Use inheritance to create a unified interface for different shapes
- Practice method overriding for area and perimeter calculations

## Mathematical Formulas

- **Rectangle Area**: `width × height`
- **Rectangle Perimeter**: `2 × (width + height)`
- **Circle Area**: `π × radius²`
- **Circle Perimeter**: `2 × π × radius`
- **Triangle Area (Heron's formula)**: `√(s × (s-a) × (s-b) × (s-c)) where s = (a+b+c)/2`
- **Triangle Perimeter**: `a + b + c`
- **Triangle Inequality**: `a + b > c, a + c > b, b + c > a`
