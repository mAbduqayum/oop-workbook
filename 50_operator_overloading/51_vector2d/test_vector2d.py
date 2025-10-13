import math

import pytest
from vector2d import Vector2D


class TestVector2DCreation:
    def test_vector_creation(self):
        v = Vector2D(3, 4)
        assert v.x == 3
        assert v.y == 4

    def test_vector_with_floats(self):
        v = Vector2D(1.5, 2.5)
        assert v.x == 1.5
        assert v.y == 2.5


class TestVector2DAddition:
    def test_vector_addition(self):
        v1 = Vector2D(3, 4)
        v2 = Vector2D(1, 2)
        v3 = v1 + v2
        assert v3.x == 4
        assert v3.y == 6

    def test_addition_creates_new_vector(self):
        v1 = Vector2D(1, 2)
        v2 = Vector2D(3, 4)
        v3 = v1 + v2
        assert v1.x == 1 and v1.y == 2  # Original unchanged
        assert v2.x == 3 and v2.y == 4  # Original unchanged


class TestVector2DSubtraction:
    def test_vector_subtraction(self):
        v1 = Vector2D(3, 4)
        v2 = Vector2D(1, 2)
        v3 = v1 - v2
        assert v3.x == 2
        assert v3.y == 2

    def test_subtraction_creates_new_vector(self):
        v1 = Vector2D(5, 5)
        v2 = Vector2D(2, 3)
        v3 = v1 - v2
        assert v1.x == 5 and v1.y == 5  # Original unchanged


class TestVector2DMultiplication:
    def test_scalar_multiplication(self):
        v = Vector2D(3, 4)
        v2 = v * 2
        assert v2.x == 6
        assert v2.y == 8

    def test_right_multiplication(self):
        v = Vector2D(3, 4)
        v2 = 2 * v
        assert v2.x == 6
        assert v2.y == 8

    def test_multiplication_with_negative(self):
        v = Vector2D(2, 3)
        v2 = v * -1
        assert v2.x == -2
        assert v2.y == -3


class TestVector2DDivision:
    def test_scalar_division(self):
        v = Vector2D(6, 8)
        v2 = v / 2
        assert v2.x == 3
        assert v2.y == 4

    def test_division_by_zero_raises_error(self):
        v = Vector2D(1, 2)
        with pytest.raises(ZeroDivisionError):
            v / 0


class TestVector2DNegation:
    def test_negation(self):
        v = Vector2D(3, 4)
        v2 = -v
        assert v2.x == -3
        assert v2.y == -4

    def test_double_negation(self):
        v = Vector2D(3, 4)
        v2 = -(-v)
        assert v2.x == 3
        assert v2.y == 4


class TestVector2DMagnitude:
    def test_magnitude(self):
        v = Vector2D(3, 4)
        assert abs(v) == 5.0

    def test_magnitude_unit_vector(self):
        v = Vector2D(1, 0)
        assert abs(v) == 1.0

    def test_magnitude_zero_vector(self):
        v = Vector2D(0, 0)
        assert abs(v) == 0.0


class TestVector2DEquality:
    def test_equality(self):
        v1 = Vector2D(3, 4)
        v2 = Vector2D(3, 4)
        assert v1 == v2

    def test_inequality(self):
        v1 = Vector2D(3, 4)
        v2 = Vector2D(1, 2)
        assert v1 != v2

    def test_not_equal_to_tuple(self):
        v = Vector2D(3, 4)
        assert v != (3, 4)


class TestVector2DStringRepresentation:
    def test_str(self):
        v = Vector2D(3, 4)
        assert str(v) == "(3, 4)"

    def test_repr(self):
        v = Vector2D(3, 4)
        assert repr(v) == "Vector2D(3, 4)"


class TestVector2DDotProduct:
    def test_dot_product(self):
        v1 = Vector2D(3, 4)
        v2 = Vector2D(1, 2)
        assert v1.dot(v2) == 11  # 3*1 + 4*2

    def test_dot_product_perpendicular(self):
        v1 = Vector2D(1, 0)
        v2 = Vector2D(0, 1)
        assert v1.dot(v2) == 0


class TestVector2DNormalize:
    def test_normalize(self):
        v = Vector2D(3, 4)
        v_norm = v.normalize()
        assert abs(abs(v_norm) - 1.0) < 0.0001
        assert abs(v_norm.x - 0.6) < 0.0001
        assert abs(v_norm.y - 0.8) < 0.0001

    def test_normalize_zero_vector_raises_error(self):
        v = Vector2D(0, 0)
        with pytest.raises(ZeroDivisionError):
            v.normalize()


class TestVector2DComplexExpressions:
    def test_complex_expression(self):
        v1 = Vector2D(3, 4)
        v2 = Vector2D(1, 2)
        result = (v1 + v2) * 2 - v1 / 2
        assert abs(result.x - 6.5) < 0.0001
        assert abs(result.y - 10.0) < 0.0001

    def test_chaining_operations(self):
        v1 = Vector2D(1, 1)
        v2 = Vector2D(2, 2)
        v3 = Vector2D(3, 3)
        result = v1 + v2 + v3
        assert result.x == 6
        assert result.y == 6
