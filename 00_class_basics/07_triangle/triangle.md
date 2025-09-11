# 🐍 Python OOP Practice - Lesson: Triangle Class

## 📝 Exercise: Create a Triangle Class System

Create a complete `Triangle` class that demonstrates Object-Oriented Programming with geometric calculations and advanced triangle properties.

**Your Task:**
1. Create a `Triangle` class with `side_a`, `side_b`, and `side_c` attributes
2. Validate triangle in `__init__` - raise `ValueError` if invalid triangle
3. Add a `calculate_perimeter()` method that returns the sum of all three sides
4. Add a `calculate_area()` method that uses Heron's formula to calculate the area
5. Add a `get_type()` method that returns triangle type based on sides ("equilateral", "isosceles", "scalene")
6. Add a `get_angles()` method that returns all three angles in degrees
7. Add a `get_angle_type()` method that returns angle classification ("acute", "right", "obtuse")
8. Add a `scale(factor)` method that returns a new scaled triangle
9. Add a `is_similar(other_triangle)` method to check similarity with another triangle

**What You'll Learn:**
- Class initialization with validation and error handling
- Mathematical calculations within methods
- Law of cosines for angle calculation
- Triangle classification by sides and angles
- Object comparison and similarity checking
- Creating new objects from existing ones

**Mathematical Formulas:**
- **Perimeter**: `P = a + b + c`
- **Heron's Formula**: `Area = √(s(s-a)(s-b)(s-c))` where `s = (a+b+c)/2`
- **Triangle Inequality**: A triangle is valid if `a + b > c`, `a + c > b`, and `b + c > a`
- **Law of Cosines**: `cos(C) = (a² + b² - c²) / (2ab)` for angle C opposite side c
- **Triangle Types by Sides**: 
  - Equilateral: all sides equal
  - Isosceles: two sides equal
  - Scalene: all sides different
- **Triangle Types by Angles**:
  - Acute: all angles < 90°
  - Right: one angle = 90°
  - Obtuse: one angle > 90°

**Example Usage:**
```python
import math

# Create triangle objects
triangle1 = Triangle(3, 4, 5)  # Valid right triangle
triangle2 = Triangle(10, 10, 10)  # Valid equilateral triangle
triangle3 = Triangle(5, 5, 8)  # Valid isosceles triangle

# This should raise ValueError
try:
    invalid_triangle = Triangle(1, 1, 5)
except ValueError as e:
    print(f"Error: {e}")  # Error: Invalid triangle: sides do not satisfy triangle inequality

# Basic calculations
print(f"Triangle 1 perimeter: {triangle1.calculate_perimeter()}")  # 12
print(f"Triangle 1 area: {triangle1.calculate_area():.2f}")  # 6.00

# Triangle classification
print(f"Triangle 1 type: {triangle1.get_type()}")  # scalene
print(f"Triangle 2 type: {triangle2.get_type()}")  # equilateral
print(f"Triangle 3 type: {triangle3.get_type()}")  # isosceles

# Angle calculations
angles1 = triangle1.get_angles()
print(f"Triangle 1 angles: {[round(a, 1) for a in angles1]}")  # [36.9, 53.1, 90.0]
print(f"Triangle 1 angle type: {triangle1.get_angle_type()}")  # right

angles2 = triangle2.get_angles()
print(f"Triangle 2 angles: {[round(a, 1) for a in angles2]}")  # [60.0, 60.0, 60.0]
print(f"Triangle 2 angle type: {triangle2.get_angle_type()}")  # acute

# Scaling
scaled_triangle = triangle1.scale(2)
print(f"Original: {triangle1.side_a}, {triangle1.side_b}, {triangle1.side_c}")  # 3, 4, 5
print(f"Scaled: {scaled_triangle.side_a}, {scaled_triangle.side_b}, {scaled_triangle.side_c}")  # 6, 8, 10

# Similarity checking
similar_triangle = Triangle(6, 8, 10)
print(f"Triangles similar: {triangle1.is_similar(similar_triangle)}")  # True
print(f"Triangles similar: {triangle1.is_similar(triangle2)}")  # False
```