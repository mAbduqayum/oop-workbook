# Python OOP Practice - Operator Overloading: Vector2D Class

## Exercise: 2D Vector Mathematics with Operators

Create a `Vector2D` class that demonstrates operator overloading for mathematical vector operations. This is a classic use case where operator overloading makes code more intuitive and readable.

**Instructions:**
Implement a 2D vector class that supports standard vector operations using Python operators. Vectors are mathematical objects commonly used in physics, graphics, and game development.

This exercise demonstrates how operator overloading transforms verbose method calls into natural mathematical expressions.

**Your Complete Task:**
1. Create a `Vector2D` class with constructor parameters:
   - `x` (float or int): x-coordinate
   - `y` (float or int): y-coordinate
2. Implement `__add__(self, other)` for vector addition
   - `(x1, y1) + (x2, y2) = (x1+x2, y1+y2)`
3. Implement `__sub__(self, other)` for vector subtraction
   - `(x1, y1) - (x2, y2) = (x1-x2, y1-y2)`
4. Implement `__mul__(self, scalar)` for scalar multiplication
   - `(x, y) * k = (x*k, y*k)`
5. Implement `__rmul__(self, scalar)` for right-hand multiplication
   - Allows `3 * vector` syntax
6. Implement `__truediv__(self, scalar)` for scalar division
   - `(x, y) / k = (x/k, y/k)`
   - Raise `ZeroDivisionError` if scalar is zero
7. Implement `__neg__(self)` for negation
   - `-(x, y) = (-x, -y)`
8. Implement `__abs__(self)` for magnitude calculation
   - `||(x, y)|| = sqrt(x² + y²)`
9. Implement `__eq__(self, other)` for equality comparison
10. Implement `__str__(self)` to return `"(x, y)"`
11. Implement `__repr__(self)` to return `"Vector2D(x, y)"`
12. Add a `dot(self, other)` method for dot product
    - `(x1, y1) · (x2, y2) = x1*x2 + y1*y2`
13. Add a `normalize(self)` method that returns a unit vector
    - Returns vector with magnitude 1 in the same direction
    - Raise `ZeroDivisionError` if magnitude is zero

**What You'll Learn:**
- **Arithmetic operators:** Make mathematical operations intuitive
- **Unary operators:** Implement negation and magnitude
- **Right-hand operators:** Support `scalar * vector` syntax
- **Type checking:** Handle different operand types gracefully
- **Mathematical operations:** Implement vector calculus operations

**Mathematical Background:**
- **Vector Addition:** Adds corresponding components
- **Scalar Multiplication:** Scales the vector by a number
- **Dot Product:** Measures how aligned two vectors are
- **Magnitude:** Length of the vector from origin
- **Normalization:** Creates unit vector (length = 1)

**Example Usage:**
```python
import math

# Create vectors
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

# Vector addition
v3 = v1 + v2
print(v3)  # (4, 6)

# Vector subtraction
v4 = v1 - v2
print(v4)  # (2, 2)

# Scalar multiplication
v5 = v1 * 2
print(v5)  # (6, 8)

# Right-hand multiplication
v6 = 3 * v1
print(v6)  # (9, 12)

# Scalar division
v7 = v1 / 2
print(v7)  # (1.5, 2.0)

# Negation
v8 = -v1
print(v8)  # (-3, -4)

# Magnitude (length)
print(abs(v1))  # 5.0

# Equality comparison
print(v1 == Vector2D(3, 4))  # True
print(v1 == v2)  # False

# Dot product
print(v1.dot(v2))  # 3*1 + 4*2 = 11

# Normalization (unit vector)
v9 = v1.normalize()
print(v9)  # (0.6, 0.8)
print(abs(v9))  # 1.0 (unit vector has magnitude 1)

# Complex expressions work naturally!
result = (v1 + v2) * 2 - v1 / 2
print(result)  # (6.5, 8.0)

# Chain operations
v10 = v1 + v2 + Vector2D(1, 1)
print(v10)  # (5, 7)

# Physics example: velocity and acceleration
velocity = Vector2D(10, 5)  # m/s
acceleration = Vector2D(2, 1)  # m/s²
time = 3  # seconds

# v = v0 + at
new_velocity = velocity + acceleration * time
print(f"Velocity after {time}s: {new_velocity}")  # (16, 8)

# Error handling
try:
    v_invalid = v1 / 0
except ZeroDivisionError as e:
    print(e)  # Cannot divide vector by zero

try:
    zero_vector = Vector2D(0, 0)
    normalized = zero_vector.normalize()
except ZeroDivisionError as e:
    print(e)  # Cannot normalize zero vector
```

**Key Operator Overloading Concepts:**
- **Natural syntax:** `v1 + v2` instead of `v1.add(v2)`
- **Chainable operations:** Combine multiple operations in one expression
- **Return new objects:** Operators create new vectors, don't modify originals
- **Type safety:** Return `NotImplemented` for unsupported types
- **Mathematical correctness:** Follow standard vector mathematics rules

**Challenge Extensions:**
- Implement `__lt__` and `__gt__` to compare vectors by magnitude
- Add `angle(self, other)` method to find angle between vectors
- Implement `cross(self, other)` for 2D cross product (returns scalar)
- Add `distance_to(self, other)` method
- Implement `rotate(self, angle)` to rotate vector by angle (radians)
- Add `project_onto(self, other)` for vector projection
- Implement `__iadd__`, `__isub__` for in-place operations
- Add support for element-wise multiplication with another vector
