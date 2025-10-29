from __future__ import annotations

import math


class Vector2D:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: int | float) -> Vector2D:
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: int | float) -> Vector2D:
        return self.__mul__(scalar)

    def __truediv__(self, scalar: int | float) -> Vector2D:
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide vector by zero")
        return Vector2D(self.x / scalar, self.y / scalar)

    def __neg__(self) -> Vector2D:
        return Vector2D(-self.x, -self.y)

    def __abs__(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def dot(self, other: Vector2D) -> float:
        return self.x * other.x + self.y * other.y

    def normalize(self) -> Vector2D:
        magnitude = abs(self)
        if magnitude == 0:
            raise ZeroDivisionError("Cannot normalize zero vector")
        return self / magnitude
