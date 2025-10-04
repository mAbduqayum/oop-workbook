# Python OOP Practice - Polymorphism: Shape Calculator

## Exercise: Polymorphic Shape Area Calculator

Build upon the abstract `Shape` classes from the abstraction chapter to demonstrate polymorphism. Create a calculator that processes different shapes using a unified interface.

**Instructions:**
Reuse the abstract `Shape` class and concrete implementations (Rectangle, Circle, Triangle) from `30_oop_abstraction/31_shapes/`. Write polymorphic functions that work with any shape type without knowing the specific class.

This exercise demonstrates how polymorphism allows you to write code once that works with many different types.

**Your Complete Task:**
1. Import or recreate the `Shape`, `Rectangle`, `Circle`, and `Triangle` classes from the abstraction chapter
2. Create a function `calculate_total_area(shapes)` that:
   - Takes a list of different shape objects
   - Returns the sum of all shape areas
   - Works polymorphically (doesn't check types)
3. Create a function `find_largest_shape(shapes)` that:
   - Takes a list of shape objects
   - Returns the shape with the largest area
4. Create a function `print_shape_report(shapes)` that:
   - Prints a formatted report for each shape
   - Shows: color, type, area, perimeter
   - Calculates and prints total area
5. Create a function `filter_by_area(shapes, min_area)` that:
   - Returns list of shapes with area >= min_area
   - Uses polymorphic area() method
6. Create a function `sort_shapes_by_area(shapes)` that:
   - Returns shapes sorted by area (smallest to largest)
   - Uses polymorphic comparison

**What You'll Learn:**
- **Polymorphic functions:** Write once, works with all shape types
- **No type checking:** Trust the interface, not the implementation
- **List processing:** Work with heterogeneous collections
- **DRY principle:** Avoid repetitive type-specific code

**Example Usage:**
```python
from abc import ABC, abstractmethod
import math

# Create a diverse collection of shapes
shapes = [
    Rectangle("red", 10, 5),
    Circle("blue", 7),
    Triangle("green", 5, 5, 6),
    Rectangle("yellow", 8, 8),
    Circle("purple", 3),
    Triangle("orange", 9, 9, 10)
]

# Polymorphic function - works with ANY shape
total = calculate_total_area(shapes)
print(f"Total area of all shapes: {total:.2f}")
# Output: Total area of all shapes: 345.63

# Find the largest shape polymorphically
largest = find_largest_shape(shapes)
print(f"Largest shape: {largest.color} {largest.__class__.__name__} with area {largest.area():.2f}")
# Output: Largest shape: blue Circle with area 153.94

# Print detailed report
print("\n=== Shape Report ===")
print_shape_report(shapes)
# Output:
# red Rectangle - Area: 50.00, Perimeter: 30.00
# blue Circle - Area: 153.94, Perimeter: 43.98
# green Triangle - Area: 12.00, Perimeter: 16.00
# yellow Rectangle - Area: 64.00, Perimeter: 32.00
# purple Circle - Area: 28.27, Perimeter: 18.85
# orange Triangle - Area: 37.42, Perimeter: 28.00
# ─────────────────────────────────────────────
# Total Area: 345.63

# Filter shapes by minimum area
large_shapes = filter_by_area(shapes, 50)
print(f"\nShapes with area >= 50: {len(large_shapes)}")
for shape in large_shapes:
    print(f"  - {shape.color} {shape.__class__.__name__}: {shape.area():.2f}")
# Output:
# Shapes with area >= 50: 3
#   - blue Circle: 153.94
#   - yellow Rectangle: 64.00

# Sort shapes by area
sorted_shapes = sort_shapes_by_area(shapes)
print("\nShapes sorted by area:")
for shape in sorted_shapes:
    print(f"  {shape.area():.2f} - {shape.color} {shape.__class__.__name__}")
# Output:
# Shapes sorted by area:
#   12.00 - green Triangle
#   28.27 - purple Circle
#   37.42 - orange Triangle
#   50.00 - red Rectangle
#   64.00 - yellow Rectangle
#   153.94 - blue Circle
```

**Key Polymorphism Concepts:**
- **Same interface, different implementations:** All shapes have `area()` and `perimeter()` methods
- **No type checking needed:** Functions work with the interface, not specific types
- **Easy to extend:** Add new shape types without changing the calculator functions
- **Heterogeneous collections:** Mix different shape types in the same list
- **Code reuse:** Single function works for unlimited shape types

**Challenge Extensions:**
- Add `calculate_total_perimeter(shapes)` function
- Create `group_shapes_by_type(shapes)` that returns a dictionary
- Implement `find_shapes_by_color(shapes, color)`
- Add comparison operators (`__lt__`, `__gt__`) to Shape classes
- Create `calculate_paint_cost(shapes, cost_per_squnit)` function
