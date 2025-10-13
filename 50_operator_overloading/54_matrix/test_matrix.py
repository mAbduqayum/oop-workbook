import pytest
from matrix import Matrix


class TestMatrixCreation:
    def test_matrix_creation(self):
        m = Matrix([[1, 2], [3, 4]])
        assert m[0][0] == 1
        assert m[0][1] == 2
        assert m[1][0] == 3
        assert m[1][1] == 4

    def test_matrix_invalid_data_raises_error(self):
        with pytest.raises(ValueError):
            Matrix([[1, 2], [3]])  # Inconsistent row lengths


class TestMatrixProperties:
    def test_rows_property(self):
        m = Matrix([[1, 2], [3, 4], [5, 6]])
        assert m.rows == 3

    def test_cols_property(self):
        m = Matrix([[1, 2, 3], [4, 5, 6]])
        assert m.cols == 3

    def test_shape_property(self):
        m = Matrix([[1, 2], [3, 4]])
        assert m.shape == (2, 2)

    def test_is_square(self):
        m1 = Matrix([[1, 2], [3, 4]])
        assert m1.is_square()

        m2 = Matrix([[1, 2, 3], [4, 5, 6]])
        assert not m2.is_square()


class TestMatrixAddition:
    def test_add_matrices(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        m3 = m1 + m2
        assert m3[0][0] == 6
        assert m3[0][1] == 8
        assert m3[1][0] == 10
        assert m3[1][1] == 12

    def test_add_incompatible_dimensions_raises_error(self):
        m1 = Matrix([[1, 2]])
        m2 = Matrix([[1], [2]])
        with pytest.raises(ValueError):
            m1 + m2


class TestMatrixSubtraction:
    def test_subtract_matrices(self):
        m1 = Matrix([[5, 6], [7, 8]])
        m2 = Matrix([[1, 2], [3, 4]])
        m3 = m1 - m2
        assert m3[0][0] == 4
        assert m3[0][1] == 4
        assert m3[1][0] == 4
        assert m3[1][1] == 4


class TestMatrixScalarMultiplication:
    def test_scalar_multiplication(self):
        m = Matrix([[1, 2], [3, 4]])
        m2 = m * 2
        assert m2[0][0] == 2
        assert m2[0][1] == 4
        assert m2[1][0] == 6
        assert m2[1][1] == 8

    def test_right_scalar_multiplication(self):
        m = Matrix([[1, 2], [3, 4]])
        m2 = 3 * m
        assert m2[0][0] == 3
        assert m2[1][1] == 12


class TestMatrixMultiplication:
    def test_matrix_multiplication(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        m3 = m1 * m2
        assert m3[0][0] == 19  # 1*5 + 2*7
        assert m3[0][1] == 22  # 1*6 + 2*8
        assert m3[1][0] == 43  # 3*5 + 4*7
        assert m3[1][1] == 50  # 3*6 + 4*8

    def test_matrix_multiplication_incompatible_raises_error(self):
        m1 = Matrix([[1, 2]])
        m2 = Matrix([[1], [2], [3]])
        with pytest.raises(ValueError):
            m1 * m2


class TestMatrixDivision:
    def test_scalar_division(self):
        m = Matrix([[2, 4], [6, 8]])
        m2 = m / 2
        assert m2[0][0] == 1.0
        assert m2[0][1] == 2.0
        assert m2[1][0] == 3.0
        assert m2[1][1] == 4.0

    def test_divide_by_zero_raises_error(self):
        m = Matrix([[1, 2]])
        with pytest.raises(ZeroDivisionError):
            m / 0


class TestMatrixNegation:
    def test_negation(self):
        m = Matrix([[1, 2], [3, 4]])
        m_neg = -m
        assert m_neg[0][0] == -1
        assert m_neg[1][1] == -4


class TestMatrixEquality:
    def test_equality(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 2], [3, 4]])
        assert m1 == m2

    def test_inequality(self):
        m1 = Matrix([[1, 2]])
        m2 = Matrix([[3, 4]])
        assert m1 != m2


class TestMatrixTranspose:
    def test_transpose(self):
        m = Matrix([[1, 2], [3, 4]])
        m_t = m.transpose()
        assert m_t[0][0] == 1
        assert m_t[0][1] == 3
        assert m_t[1][0] == 2
        assert m_t[1][1] == 4


class TestMatrixIdentity:
    def test_identity_matrix(self):
        identity = Matrix.identity(3)
        assert identity[0][0] == 1
        assert identity[1][1] == 1
        assert identity[2][2] == 1
        assert identity[0][1] == 0
        assert identity[1][2] == 0


class TestMatrixStringRepresentation:
    def test_str(self):
        m = Matrix([[1, 2], [3, 4]])
        assert "[[1, 2], [3, 4]]" in str(m)

    def test_repr(self):
        m = Matrix([[1, 2]])
        assert "Matrix" in repr(m)
