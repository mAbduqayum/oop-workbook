import math
from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    def __init__(self, color: str) -> None:
        self.color = color

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, color: str, width: float, height: float) -> None:
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, color: str, radius: float) -> None:
        super().__init__(color)
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, color: str, side1: float, side2: float, side3: float) -> None:
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self) -> float:
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3


def calculate_total_area(shapes: List[Shape]) -> float:
    return sum(shape.area() for shape in shapes)


def find_largest_shape(shapes: List[Shape]) -> Shape | None:
    if not shapes:
        return None
    return max(shapes, key=lambda shape: shape.area())


def print_shape_report(shapes: List[Shape]) -> None:
    print("Shape Report")
    print("=" * 50)

    for shape in shapes:
        shape_type = shape.__class__.__name__
        print(
            f"{shape.color} {shape_type} - Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}"
        )

    print("─" * 50)
    total = calculate_total_area(shapes)
    print(f"Total Area: {total:.2f}")


def filter_by_area(shapes: List[Shape], min_area: float) -> List[Shape]:
    return [shape for shape in shapes if shape.area() >= min_area]


def sort_shapes_by_area(shapes: List[Shape]) -> List[Shape]:
    return sorted(shapes, key=lambda shape: shape.area())


if __name__ == "__main__":
    shapes = [
        Rectangle("red", 10, 5),
        Circle("blue", 7),
        Triangle("green", 5, 5, 6),
        Rectangle("yellow", 8, 8),
        Circle("purple", 3),
        Triangle("orange", 9, 9, 10),
    ]

    total = calculate_total_area(shapes)
    print(f"Total area of all shapes: {total:.2f}\n")

    largest = find_largest_shape(shapes)
    print(
        f"Largest shape: {largest.color} {largest.__class__.__name__} with area {largest.area():.2f}\n"
    )

    # Print detailed report
    print_shape_report(shapes)

    print("\n\nShapes with area >= 50:")
    large_shapes = filter_by_area(shapes, 50)
    for shape in large_shapes:
        print(f"  - {shape.color} {shape.__class__.__name__}: {shape.area():.2f}")

    print("\n\nShapes sorted by area:")
    sorted_shapes = sort_shapes_by_area(shapes)
    for shape in sorted_shapes:
        print(f"  {shape.area():6.2f} - {shape.color} {shape.__class__.__name__}")
