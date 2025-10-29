from __future__ import annotations


class Matrix:
    def __init__(self, data) -> None:
        if not data or not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same length")

        self._data = [list(row) for row in data]
        self._rows = len(data)
        self._cols = len(data[0])

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def shape(self) -> tuple[int, int]:
        return (self._rows, self._cols)

    def is_square(self) -> bool:
        return self._rows == self._cols

    def __getitem__(self, index: int) -> list:
        return self._data[index]

    def __setitem__(self, index, value) -> None:
        self._data[index] = value

    def __add__(self, other: Matrix) -> Matrix:
        if self.shape != other.shape:
            raise ValueError("Matrices must have same dimensions for addition")

        result = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                row.append(self[i][j] + other[i][j])
            result.append(row)
        return Matrix(result)

    def __sub__(self, other: Matrix) -> Matrix:
        if self.shape != other.shape:
            raise ValueError("Matrices must have same dimensions for subtraction")

        result = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                row.append(self[i][j] - other[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other: "Matrix | int | float") -> Matrix:
        if isinstance(other, Matrix):
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

    def __rmul__(self, scalar: int | float) -> Matrix:
        return self * scalar

    def __truediv__(self, scalar: int | float) -> Matrix:
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide matrix by zero")

        result = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                row.append(self[i][j] / scalar)
            result.append(row)
        return Matrix(result)

    def __pow__(self, exponent: int) -> Matrix:
        if not self.is_square():
            raise ValueError("Matrix must be square for exponentiation")
        if exponent < 0:
            raise ValueError("Exponent must be a non-negative integer")

        if exponent == 0:
            return Matrix.identity(self._rows)

        result = Matrix(self._data)
        for _ in range(exponent - 1):
            result = result * self
        return result

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix):
            return False
        if self.shape != other.shape:
            return False
        for i in range(self._rows):
            for j in range(self._cols):
                if self[i][j] != other[i][j]:
                    return False
        return True

    def __neg__(self) -> Matrix:
        result = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                row.append(-self[i][j])
            result.append(row)
        return Matrix(result)

    def transpose(self) -> Matrix:
        result = []
        for j in range(self._cols):
            row = []
            for i in range(self._rows):
                row.append(self[i][j])
            result.append(row)
        return Matrix(result)

    @classmethod
    def identity(cls, size: int) -> Matrix:
        data = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(1 if i == j else 0)
            data.append(row)
        return cls(data)

    def __str__(self) -> str:
        return str(self._data)

    def __repr__(self) -> str:
        return f"Matrix({self._data})"
