import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color) -> None:
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, color, width, height) -> None:
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, color, radius) -> None:
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, color, base, height, side1, side2, side3) -> None:
        super().__init__(color)
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


if __name__ == "__main__":
    print("Attempting to create abstract Shape:")
    try:
        shape = Shape("red")
        print("This shouldn't work!")
    except TypeError as e:
        print(f"Error: {e}")
        print("✓ Cannot instantiate abstract class - as expected!\n")

    print("Creating concrete shapes:")
    rectangle = Rectangle("red", 10, 5)
    circle = Circle("blue", 7)
    triangle = Triangle("green", 6, 4, 5, 5, 6)

    print(f"\nRectangle ({rectangle.color}):")
    print(f"  Area: {rectangle.area():.2f}")
    print(f"  Perimeter: {rectangle.perimeter():.2f}")

    print(f"\nCircle ({circle.color}):")
    print(f"  Area: {circle.area():.2f}")
    print(f"  Perimeter: {circle.perimeter():.2f}")

    print(f"\nTriangle ({triangle.color}):")
    print(f"  Area: {triangle.area():.2f}")
    print(f"  Perimeter: {triangle.perimeter():.2f}")

    print("\n" + "=" * 50)
    print("Polymorphic function working with all shapes:")
    print("=" * 50)

    def print_shape_info(shape: Shape):
        print(f"{shape.color} {shape.__class__.__name__}")
        print(f"  Area: {shape.area():.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}\n")

    shapes = [rectangle, circle, triangle]
    for shape in shapes:
        print_shape_info(shape)
