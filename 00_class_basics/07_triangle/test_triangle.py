import pytest

from triangle import Triangle


class TestTriangle:
    def test_valid_triangle_creation(self):
        triangle = Triangle(3, 4, 5)
        assert triangle.a == 3
        assert triangle.b == 4
        assert triangle.c == 5

    def test_invalid_triangle_creation(self):
        with pytest.raises(ValueError):
            Triangle(1, 1, 5)

    def test_calculate_perimeter(self):
        triangle = Triangle(3, 4, 5)
        assert triangle.calculate_perimeter() == 12

    def test_calculate_area(self):
        triangle = Triangle(3, 4, 5)
        assert triangle.calculate_area() == 6.0

    def test_get_type_scalene(self):
        triangle = Triangle(3, 4, 5)
        assert triangle.get_type() == "scalene"

    def test_get_type_isosceles(self):
        triangle = Triangle(5, 5, 8)
        assert triangle.get_type() == "isosceles"

    def test_get_type_equilateral(self):
        triangle = Triangle(5, 5, 5)
        assert triangle.get_type() == "equilateral"

    def test_get_angle_type_right(self):
        triangle = Triangle(3, 4, 5)
        assert triangle.get_angle_type() == "right"

    def test_scale(self):
        triangle = Triangle(3, 4, 5)
        scaled = triangle.scale(2)
        assert scaled.a == 6
        assert scaled.b == 8
        assert scaled.c == 10

    def test_is_similar(self):
        t = Triangle(3, 4, 5)
        rotated_t = Triangle(4, 5, 3)
        scaled_t = t.scale(1.5)
        un_similar = Triangle(5, 12, 13)
        assert t.is_similar(scaled_t)
        assert t.is_similar(rotated_t)
        assert not t.is_similar(un_similar)
