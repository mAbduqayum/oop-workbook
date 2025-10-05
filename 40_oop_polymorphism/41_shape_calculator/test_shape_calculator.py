import math
from abc import ABC, abstractmethod

import pytest


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
    def __init__(self, color, side1, side2, side3) -> None:
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


try:
    from shape_calculator import (
        calculate_total_area,
        filter_by_area,
        find_largest_shape,
        print_shape_report,
        sort_shapes_by_area,
    )
except ImportError:

    def calculate_total_area(shapes):
        raise NotImplementedError("Implement calculate_total_area()")

    def find_largest_shape(shapes):
        raise NotImplementedError("Implement find_largest_shape()")

    def print_shape_report(shapes):
        raise NotImplementedError("Implement print_shape_report()")

    def filter_by_area(shapes, min_area):
        raise NotImplementedError("Implement filter_by_area()")

    def sort_shapes_by_area(shapes):
        raise NotImplementedError("Implement sort_shapes_by_area()")


@pytest.fixture
def sample_shapes():
    return [
        Rectangle("red", 10, 5),  # area = 50
        Circle("blue", 5),  # area = 78.54
        Triangle("green", 5, 5, 6),  # area = 12 (Heron's formula)
        Rectangle("yellow", 3, 3),  # area = 9
        Circle("purple", 2),  # area = 12.57
    ]


class TestCalculateTotalArea:
    def test_total_area_multiple_shapes(self, sample_shapes):
        total = calculate_total_area(sample_shapes)
        expected = 50 + 78.54 + 12 + 9 + 12.57
        assert abs(total - expected) < 0.1, "Total area calculation incorrect"

    def test_total_area_single_shape(self):
        shapes = [Rectangle("red", 10, 5)]
        assert calculate_total_area(shapes) == 50

    def test_total_area_empty_list(self):
        assert calculate_total_area([]) == 0

    def test_total_area_only_circles(self):
        shapes = [Circle("red", 5), Circle("blue", 3)]
        total = calculate_total_area(shapes)
        expected = math.pi * 25 + math.pi * 9
        assert abs(total - expected) < 0.01


class TestFindLargestShape:
    def test_find_largest_in_mixed_shapes(self, sample_shapes):
        largest = find_largest_shape(sample_shapes)
        assert isinstance(largest, Circle)
        assert largest.color == "blue"
        assert largest.radius == 5

    def test_find_largest_single_shape(self):
        shapes = [Rectangle("red", 10, 5)]
        largest = find_largest_shape(shapes)
        assert largest.color == "red"

    def test_find_largest_all_same_area(self):
        shapes = [Rectangle("red", 5, 2), Rectangle("blue", 2, 5)]
        largest = find_largest_shape(shapes)
        assert largest.area() == 10

    def test_find_largest_with_triangle(self):
        shapes = [
            Triangle("green", 15, 15, 20),
            Rectangle("red", 8, 8),
        ]
        largest = find_largest_shape(shapes)
        assert isinstance(largest, Triangle)


class TestFilterByArea:
    def test_filter_above_threshold(self, sample_shapes):
        filtered = filter_by_area(sample_shapes, 20)
        assert len(filtered) == 2
        assert all(shape.area() >= 20 for shape in filtered)

    def test_filter_no_matches(self, sample_shapes):
        filtered = filter_by_area(sample_shapes, 1000)
        assert len(filtered) == 0

    def test_filter_all_match(self, sample_shapes):
        filtered = filter_by_area(sample_shapes, 0)
        assert len(filtered) == len(sample_shapes)

    def test_filter_exact_threshold(self):
        shapes = [Rectangle("red", 10, 5), Rectangle("blue", 7, 7)]
        filtered = filter_by_area(shapes, 50)
        assert len(filtered) == 1
        assert filtered[0].color == "red"


class TestSortShapesByArea:
    def test_sort_mixed_shapes(self, sample_shapes):
        sorted_shapes = sort_shapes_by_area(sample_shapes)
        areas = [shape.area() for shape in sorted_shapes]
        assert areas == sorted(areas)

    def test_sort_already_sorted(self):
        shapes = [
            Rectangle("red", 2, 2),
            Rectangle("blue", 3, 3),
            Rectangle("green", 4, 4),
        ]
        sorted_shapes = sort_shapes_by_area(shapes)
        assert sorted_shapes[0].color == "red"
        assert sorted_shapes[1].color == "blue"
        assert sorted_shapes[2].color == "green"

    def test_sort_reverse_order(self):
        shapes = [
            Rectangle("red", 4, 4),
            Rectangle("blue", 3, 3),
            Rectangle("green", 2, 2),
        ]
        sorted_shapes = sort_shapes_by_area(shapes)
        assert sorted_shapes[0].color == "green"
        assert sorted_shapes[2].color == "red"

    def test_sort_single_shape(self):
        shapes = [Circle("red", 5)]
        sorted_shapes = sort_shapes_by_area(shapes)
        assert len(sorted_shapes) == 1


class TestPrintShapeReport:
    def test_report_output(self, sample_shapes, capsys):
        print_shape_report(sample_shapes)
        captured = capsys.readouterr()
        assert "red" in captured.out.lower()
        assert "blue" in captured.out.lower()
        assert "green" in captured.out.lower()

    def test_report_includes_total(self, sample_shapes, capsys):
        print_shape_report(sample_shapes)
        captured = capsys.readouterr()
        assert "total" in captured.out.lower()


class TestPolymorphism:
    def test_works_with_new_shape_type(self):
        class Square(Shape):
            def __init__(self, color, side) -> None:
                super().__init__(color)
                self.side = side

            def area(self):
                return self.side**2

            def perimeter(self):
                return 4 * self.side

        shapes = [
            Square("red", 5),
            Rectangle("blue", 4, 6),
        ]

        total = calculate_total_area(shapes)
        assert total == 49

        largest = find_largest_shape(shapes)
        assert isinstance(largest, Square)

    def test_no_isinstance_checks_needed(self, sample_shapes):
        total = calculate_total_area(sample_shapes)
        assert total > 0

        largest = find_largest_shape(sample_shapes)
        assert hasattr(largest, "area")
        assert hasattr(largest, "perimeter")

        filtered = filter_by_area(sample_shapes, 10)
        assert isinstance(filtered, list)

        sorted_shapes = sort_shapes_by_area(sample_shapes)
        assert len(sorted_shapes) == len(sample_shapes)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
