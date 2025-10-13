import pytest
from fraction import Fraction


class TestFractionCreation:
    def test_fraction_creation(self):
        f = Fraction(1, 2)
        assert f.numerator == 1
        assert f.denominator == 2

    def test_fraction_automatic_reduction(self):
        f = Fraction(2, 4)
        assert f.numerator == 1
        assert f.denominator == 2

    def test_fraction_with_negative_denominator(self):
        f = Fraction(1, -2)
        assert f.numerator == -1
        assert f.denominator == 2

    def test_fraction_both_negative(self):
        f = Fraction(-1, -2)
        assert f.numerator == 1
        assert f.denominator == 2

    def test_fraction_default_denominator(self):
        f = Fraction(5)
        assert f.numerator == 5
        assert f.denominator == 1

    def test_zero_denominator_raises_error(self):
        with pytest.raises(ZeroDivisionError):
            Fraction(1, 0)


class TestFractionAddition:
    def test_add_fractions(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        f3 = f1 + f2
        assert f3.numerator == 5
        assert f3.denominator == 6

    def test_add_fraction_and_integer(self):
        f1 = Fraction(1, 2)
        f2 = f1 + 1
        assert f2.numerator == 3
        assert f2.denominator == 2

    def test_addition_creates_new_fraction(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        f3 = f1 + f2
        assert f1.numerator == 1 and f1.denominator == 2


class TestFractionSubtraction:
    def test_subtract_fractions(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        f3 = f1 - f2
        assert f3.numerator == 1
        assert f3.denominator == 6

    def test_subtract_fraction_and_integer(self):
        f1 = Fraction(3, 2)
        f2 = f1 - 1
        assert f2.numerator == 1
        assert f2.denominator == 2


class TestFractionMultiplication:
    def test_multiply_fractions(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        f3 = f1 * f2
        assert f3.numerator == 1
        assert f3.denominator == 6

    def test_multiply_fraction_by_integer(self):
        f1 = Fraction(3, 4)
        f2 = f1 * 2
        assert f2.numerator == 3
        assert f2.denominator == 2


class TestFractionDivision:
    def test_divide_fractions(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        f3 = f1 / f2
        assert f3.numerator == 3
        assert f3.denominator == 2

    def test_divide_fraction_by_integer(self):
        f1 = Fraction(3, 4)
        f2 = f1 / 2
        assert f2.numerator == 3
        assert f2.denominator == 8

    def test_divide_by_zero_raises_error(self):
        f1 = Fraction(1, 2)
        with pytest.raises(ZeroDivisionError):
            f1 / Fraction(0, 1)

    def test_divide_by_zero_integer_raises_error(self):
        f1 = Fraction(1, 2)
        with pytest.raises(ZeroDivisionError):
            f1 / 0


class TestFractionComparison:
    def test_equality(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        assert f1 == f2

    def test_equality_with_integer(self):
        f1 = Fraction(2, 1)
        assert f1 == 2

    def test_less_than(self):
        f1 = Fraction(1, 3)
        f2 = Fraction(1, 2)
        assert f1 < f2

    def test_less_than_or_equal(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        assert f1 <= f2

    def test_greater_than(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        assert f1 > f2

    def test_greater_than_or_equal(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(3, 4)
        assert f1 >= f2


class TestFractionNegation:
    def test_negation(self):
        f = Fraction(1, 2)
        f_neg = -f
        assert f_neg.numerator == -1
        assert f_neg.denominator == 2

    def test_double_negation(self):
        f = Fraction(1, 2)
        f_neg = -(-f)
        assert f_neg.numerator == 1
        assert f_neg.denominator == 2


class TestFractionAbsoluteValue:
    def test_abs_positive(self):
        f = Fraction(3, 4)
        f_abs = abs(f)
        assert f_abs.numerator == 3
        assert f_abs.denominator == 4

    def test_abs_negative(self):
        f = Fraction(-3, 4)
        f_abs = abs(f)
        assert f_abs.numerator == 3
        assert f_abs.denominator == 4


class TestFractionConversion:
    def test_to_float(self):
        f = Fraction(1, 2)
        assert float(f) == 0.5

    def test_to_int(self):
        f = Fraction(5, 2)
        assert int(f) == 2


class TestFractionReciprocal:
    def test_reciprocal(self):
        f = Fraction(2, 3)
        f_rec = f.reciprocal()
        assert f_rec.numerator == 3
        assert f_rec.denominator == 2

    def test_reciprocal_of_zero_raises_error(self):
        f = Fraction(0, 1)
        with pytest.raises(ZeroDivisionError):
            f.reciprocal()


class TestFractionStringRepresentation:
    def test_str_regular_fraction(self):
        f = Fraction(1, 2)
        assert str(f) == "1/2"

    def test_str_whole_number(self):
        f = Fraction(4, 2)
        assert str(f) == "2"

    def test_repr(self):
        f = Fraction(1, 2)
        assert repr(f) == "Fraction(1, 2)"


class TestFractionComplexExpressions:
    def test_complex_expression(self):
        result = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 6)
        assert result == Fraction(1, 1)

    def test_chaining_operations(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        result = (f1 + f2) * Fraction(2, 3) / Fraction(1, 2)
        assert result == Fraction(1, 1)
