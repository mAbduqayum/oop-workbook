from typing import Self


class Matrix:
    def __init__(self, data) -> None:
        if not data or not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same length")

        self._data = [list(row) for row in data]
        self._rows = len(data)
        self._cols = len(data[0])

    @property
    def rows(self) -> int:
        """Return number of rows"""
        return self._rows

    @property
    def cols(self) -> int:
        """Return number of columns"""
        return self._cols

    @property
    def shape(self) -> tuple[int, int]:
        """Return (rows, cols) tuple"""
        return (self._rows, self._cols)

    def is_square(self) -> bool:
        """Check if matrix is square"""
        return self._rows == self._cols

    def __getitem__(self, index: int) -> list:
        """Access elements via matrix[i][j]"""
        return self._data[index]

    def __setitem__(self, index, value) -> None:
        """Set elements via matrix[i][j] = value"""
        self._data[index] = value

    def __add__(self, other: Self) -> Self:
        """Matrix addition"""
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError("Matrices must have same dimensions for addition")

            result = []
            for i in range(self._rows):
                row = []
                for j in range(self._cols):
                    row.append(self[i][j] + other[i][j])
                result.append(row)
            return Matrix(result)
        return NotImplemented

    def __sub__(self, other: Self) -> Self:
        """Matrix subtraction"""
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError("Matrices must have same dimensions for subtraction")

            result = []
            for i in range(self._rows):
                row = []
                for j in range(self._cols):
                    row.append(self[i][j] - other[i][j])
                result.append(row)
            return Matrix(result)
        return NotImplemented

    def __mul__(self, other: Self | int | float) -> Self:
        """Matrix multiplication or scalar multiplication"""
        if isinstance(other, Matrix):
            # Matrix multiplication
            if self._cols != other._rows:
                raise ValueError(
                    f"Incompatible dimensions: ({self._rows}x{self._cols}) * ({other._rows}x{other._cols})"
                )

            result = []
            for i in range(self._rows):
                row = []
                for j in range(other._cols):
                    value = sum(self[i][k] * other[k][j] for k in range(self._cols))
                    row.append(value)
                result.append(row)
            return Matrix(result)

        elif isinstance(other, (int, float)):
            # Scalar multiplication
            result = []
            for i in range(self._rows):
                row = []
                for j in range(self._cols):
                    row.append(self[i][j] * other)
                result.append(row)
            return Matrix(result)

        return NotImplemented

    def __rmul__(self, scalar: int | float) -> Self:
        """Right multiplication (scalar * matrix)"""
        if isinstance(scalar, (int, float)):
            return self * scalar
        return NotImplemented

    def __truediv__(self, scalar: int | float) -> Self:
        """Scalar division"""
        if isinstance(scalar, (int, float)):
            if scalar == 0:
                raise ZeroDivisionError("Cannot divide matrix by zero")

            result = []
            for i in range(self._rows):
                row = []
                for j in range(self._cols):
                    row.append(self[i][j] / scalar)
                result.append(row)
            return Matrix(result)
        return NotImplemented

    def __pow__(self, exponent: int) -> Self:
        """Matrix exponentiation"""
        if not self.is_square():
            raise ValueError("Matrix must be square for exponentiation")
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("Exponent must be a non-negative integer")

        if exponent == 0:
            return Matrix.identity(self._rows)

        result = Matrix(self._data)
        for _ in range(exponent - 1):
            result = result * self
        return result

    def __eq__(self, other: object) -> bool:
        """Equality comparison"""
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                return False
            for i in range(self._rows):
                for j in range(self._cols):
                    if self[i][j] != other[i][j]:
                        return False
            return True
        return False

    def __neg__(self) -> Self:
        """Negation"""
        result = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                row.append(-self[i][j])
            result.append(row)
        return Matrix(result)

    def transpose(self) -> Self:
        """Return transposed matrix"""
        result = []
        for j in range(self._cols):
            row = []
            for i in range(self._rows):
                row.append(self[i][j])
            result.append(row)
        return Matrix(result)

    @classmethod
    def identity(cls, size: int) -> Self:
        """Create an identity matrix of given size"""
        data = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(1 if i == j else 0)
            data.append(row)
        return cls(data)

    def __str__(self) -> str:
        """Human-readable string"""
        return str(self._data)

    def __repr__(self) -> str:
        """Developer representation"""
        return f"Matrix({self._data})"
