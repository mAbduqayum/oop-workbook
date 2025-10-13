import math
from typing import Self


class Vector2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Self) -> Self:
        """Vector addition: (x1, y1) + (x2, y2) = (x1+x2, y1+y2)"""
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Self) -> Self:
        """Vector subtraction"""
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar: int | float) -> Self:
        """Scalar multiplication: multiply vector by a number"""
        if isinstance(scalar, (int, float)):
            return Vector2D(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __rmul__(self, scalar: int | float) -> Self:
        """Right multiplication: allows '2 * vector' syntax"""
        return self.__mul__(scalar)

    def __truediv__(self, scalar: int | float) -> Self:
        """Scalar division"""
        if isinstance(scalar, (int, float)):
            if scalar == 0:
                raise ZeroDivisionError("Cannot divide vector by zero")
            return Vector2D(self.x / scalar, self.y / scalar)
        return NotImplemented

    def __neg__(self) -> Self:
        """Negation: -vector"""
        return Vector2D(-self.x, -self.y)

    def __abs__(self) -> float:
        """Magnitude of the vector"""
        return math.sqrt(self.x**2 + self.y**2)

    def __eq__(self, other: object) -> bool:
        """Equality comparison"""
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self) -> str:
        """Human-readable string"""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Developer representation"""
        return f"Vector2D({self.x}, {self.y})"

    def dot(self, other: Self) -> float:
        """Dot product: (x1, y1) · (x2, y2) = x1*x2 + y1*y2"""
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        raise TypeError("Dot product requires another Vector2D")

    def normalize(self) -> Self:
        """Return a unit vector in the same direction"""
        magnitude = abs(self)
        if magnitude == 0:
            raise ZeroDivisionError("Cannot normalize zero vector")
        return self / magnitude
