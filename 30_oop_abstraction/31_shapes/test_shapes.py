import math

import pytest
from shapes import Circle, Rectangle, Shape, Triangle


class TestShape:
    def test_cannot_instantiate_abstract_shape(self):
        with pytest.raises(TypeError):
            Shape("red")


class TestRectangle:
    def test_rectangle_creation(self):
        rect = Rectangle("red", 10, 5)
        assert rect.color == "red"
        assert rect.width == 10
        assert rect.height == 5

    def test_rectangle_area(self):
        rect = Rectangle("blue", 10, 5)
        assert rect.area() == 50

    def test_rectangle_perimeter(self):
        rect = Rectangle("green", 10, 5)
        assert rect.perimeter() == 30

    def test_rectangle_is_shape(self):
        rect = Rectangle("yellow", 8, 4)
        assert isinstance(rect, Shape)


class TestCircle:
    def test_circle_creation(self):
        circle = Circle("blue", 7)
        assert circle.color == "blue"
        assert circle.radius == 7

    def test_circle_area(self):
        circle = Circle("red", 7)
        expected_area = math.pi * 7**2
        assert abs(circle.area() - expected_area) < 0.01

    def test_circle_perimeter(self):
        circle = Circle("green", 7)
        expected_perimeter = 2 * math.pi * 7
        assert abs(circle.perimeter() - expected_perimeter) < 0.01

    def test_circle_is_shape(self):
        circle = Circle("purple", 5)
        assert isinstance(circle, Shape)


class TestTriangle:
    def test_triangle_creation(self):
        triangle = Triangle("green", 6, 4, 5, 5, 6)
        assert triangle.color == "green"
        assert triangle.base == 6
        assert triangle.height == 4
        assert triangle.side1 == 5
        assert triangle.side2 == 5
        assert triangle.side3 == 6

    def test_triangle_area(self):
        triangle = Triangle("red", 6, 4, 5, 5, 6)
        assert triangle.area() == 12.0

    def test_triangle_perimeter(self):
        triangle = Triangle("blue", 6, 4, 5, 5, 6)
        assert triangle.perimeter() == 16

    def test_triangle_is_shape(self):
        triangle = Triangle("orange", 3, 4, 3, 4, 5)
        assert isinstance(triangle, Shape)


class TestPolymorphism:
    def test_all_shapes_have_area_method(self):
        shapes = [
            Rectangle("red", 10, 5),
            Circle("blue", 7),
            Triangle("green", 6, 4, 5, 5, 6),
        ]
        for shape in shapes:
            assert hasattr(shape, "area")
            assert callable(shape.area)
            assert isinstance(shape.area(), (int, float))

    def test_all_shapes_have_perimeter_method(self):
        shapes = [
            Rectangle("red", 10, 5),
            Circle("blue", 7),
            Triangle("green", 6, 4, 5, 5, 6),
        ]
        for shape in shapes:
            assert hasattr(shape, "perimeter")
            assert callable(shape.perimeter)
            assert isinstance(shape.perimeter(), (int, float))

    def test_polymorphic_function(self):
        def get_area(shape: Shape) -> float:
            return shape.area()

        rect = Rectangle("red", 10, 5)
        circle = Circle("blue", 7)
        triangle = Triangle("green", 6, 4, 5, 5, 6)

        assert get_area(rect) == 50
        assert abs(get_area(circle) - (math.pi * 49)) < 0.01
        assert get_area(triangle) == 12.0
