# Python OOP Practice - Operator Overloading: Matrix Class

## Exercise: Matrix Mathematics with Operators

Create a `Matrix` class that represents 2D matrices and supports matrix operations using operator overloading. This demonstrates advanced operator overloading for linear algebra operations.

**Instructions:**
Implement a matrix class that handles standard linear algebra operations with proper mathematical semantics. Matrices are fundamental in computer graphics, machine learning, and scientific computing.

This exercise demonstrates operator overloading for a complex mathematical structure where operators have precise, well-defined meanings.

**Your Complete Task:**
1. Create a `Matrix` class with constructor parameter:
   - `data` (list of lists): 2D array representing the matrix
   - Validate that all rows have the same length
   - Store dimensions (rows × columns)
   - Raise `ValueError` for invalid matrix data
2. Implement `__add__(self, other)` for matrix addition
   - Matrices must have same dimensions
   - Add corresponding elements
   - Raise `ValueError` for dimension mismatch
3. Implement `__sub__(self, other)` for matrix subtraction
4. Implement `__mul__(self, other)` for matrix multiplication OR scalar multiplication
   - Matrix * Matrix: Standard matrix multiplication (dot product)
   - Matrix * scalar: Multiply each element by scalar
   - Check dimension compatibility: (m×n) * (n×p) → (m×p)
5. Implement `__rmul__(self, scalar)` for scalar * Matrix
6. Implement `__truediv__(self, scalar)` for scalar division
   - Divide each element by scalar
   - Raise `ZeroDivisionError` if scalar is zero
7. Implement `__pow__(self, exponent)` for matrix exponentiation
   - Must be square matrix
   - Raise `ValueError` if not square or exponent < 0
8. Implement `__eq__(self, other)` for equality
9. Implement `__neg__(self)` for negation (negate all elements)
10. Implement `__getitem__(self, index)` to access elements: `matrix[i][j]`
11. Implement `__str__(self)` to return formatted matrix
12. Implement `__repr__(self)` to return `"Matrix([[...]])"`
13. Add `transpose(self)` method to return transposed matrix
14. Add `rows` property to return number of rows
15. Add `cols` property to return number of columns
16. Add `shape` property to return (rows, cols) tuple
17. Add `is_square(self)` method
18. Add `identity(size)` class method to create identity matrix

**Example Usage:**
```python
# Create matrices
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

# Addition
m3 = m1 + m2
print(m3)  # [[6, 8], [10, 12]]

# Subtraction
m4 = m2 - m1
print(m4)  # [[4, 4], [4, 4]]

# Scalar multiplication
m5 = m1 * 2
print(m5)  # [[2, 4], [6, 8]]

m6 = 3 * m1
print(m6)  # [[3, 6], [9, 12]]

# Matrix multiplication
m7 = m1 * m2
print(m7)  # [[19, 22], [43, 50]]

# Scalar division
m8 = m1 / 2
print(m8)  # [[0.5, 1.0], [1.5, 2.0]]

# Negation
m9 = -m1
print(m9)  # [[-1, -2], [-3, -4]]

# Element access
print(m1[0][1])  # 2
print(m1[1])  # [3, 4]

# Transpose
m10 = m1.transpose()
print(m10)  # [[1, 3], [2, 4]]

# Properties
print(m1.shape)  # (2, 2)
print(m1.rows)  # 2
print(m1.cols)  # 2
print(m1.is_square())  # True

# Identity matrix
identity = Matrix.identity(3)
print(identity)  # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Matrix power
m11 = m1 ** 2
print(m11)  # Same as m1 * m1

# Error handling
try:
    invalid = m1 + Matrix([[1, 2, 3]])
except ValueError as e:
    print(e)  # Dimension mismatch

try:
    wrong_mult = Matrix([[1, 2]]) * Matrix([[1], [2], [3]])
except ValueError as e:
    print(e)  # Incompatible dimensions
```

**Challenge Extensions:**
- Add `determinant()` method
- Implement `inverse()` method
- Add `trace()` for square matrices
- Implement row and column operations
