## Exercise: Triangle Class

Create a `Triangle` class that demonstrates geometric calculations and validation.

### Your Task:
1. Create a `Triangle` class with `a`, `b`, and `c` attributes
2. Validate triangle in `__init__` - raise `ValueError` if invalid triangle
3. Add a `calculate_perimeter()` method that returns the sum of all three sides
4. Add a `calculate_area()` method that uses Heron's formula to calculate the area
5. Add a `get_type()` method that returns the triangle type based on the sides (`equilateral`, `isosceles`, `scalene`)
6. Add a `get_angles()` method that returns all three angles in degrees
7. Add a `get_angle_type()` method that returns angle classification (`acute`, `right`, `obtuse`)
8. Add a `scale(factor)` method that returns a new scaled triangle
9. Add a `is_similar(other_triangle)` method to check similarity with another triangle

### Example Usage:
```python
import math

triangle1 = Triangle(3, 4, 5)
print(triangle1.calculate_perimeter())  # 12
print(triangle1.calculate_area())       # 6.0
print(triangle1.get_type())            # scalene
print(triangle1.get_angles())          # [36.87, 53.13, 90.0]
print(triangle1.get_angle_type())      # right

scaled = triangle1.scale(2)
print(scaled.a, scaled.b, scaled.c)    # 6 8 10

print(triangle1.is_similar(scaled))    # True

try:
    Triangle(1, 1, 5)
except ValueError as e:
    print(e)  # Invalid triangle
```

### Formulas:
- **Triangle Inequality**: `a + b > c`, `a + c > b`, and `b + c > a`
- **Heron's Formula**: `Area = √(s(s-a)(s-b)(s-c))` where `s = (a+b+c)/2`
- **Law of Cosines**: `cos(C) = (a² + b² - c²) / (2ab)` for angle C opposite side c
