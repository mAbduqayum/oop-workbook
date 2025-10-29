from __future__ import annotations

import math


class Fraction:
    def __init__(self, numerator, denominator=1) -> None:
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        # Reduce to lowest terms
        gcd = math.gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

        # Keep denominator positive
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other: Fraction | int) -> Fraction:
        """Add two fractions: a/b + c/d = (ad + bc)/bd"""
        if isinstance(other, Fraction):
            num = (
                self.numerator * other.denominator + other.numerator * self.denominator
            )
            den = self.denominator * other.denominator
            return Fraction(num, den)
        elif isinstance(other, int):
            return self + Fraction(other)

    def __sub__(self, other: Fraction | int) -> Fraction:
        if isinstance(other, Fraction):
            num = (
                self.numerator * other.denominator - other.numerator * self.denominator
            )
            den = self.denominator * other.denominator
            return Fraction(num, den)
        elif isinstance(other, int):
            return self - Fraction(other)

    def __mul__(self, other: Fraction | int) -> Fraction:
        """Multiply fractions: (a/b) * (c/d) = (ac)/(bd)"""
        if isinstance(other, Fraction):
            return Fraction(
                self.numerator * other.numerator, self.denominator * other.denominator
            )
        elif isinstance(other, int):
            return Fraction(self.numerator * other, self.denominator)

    def __truediv__(self, other: Fraction | int) -> Fraction:
        """Divide fractions: (a/b) / (c/d) = (ad)/(bc)"""
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Fraction(
                self.numerator * other.denominator, self.denominator * other.numerator
            )
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Fraction(self.numerator, self.denominator * other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Fraction):
            return (
                self.numerator == other.numerator
                and self.denominator == other.denominator
            )
        elif isinstance(other, int):
            return self.numerator == other and self.denominator == 1
        return False

    def __lt__(self, other: Fraction) -> bool:
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other: Fraction) -> bool:
        return self < other or self == other

    def __gt__(self, other: Fraction) -> bool:
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other: Fraction) -> bool:
        return self > other or self == other

    def __neg__(self) -> Fraction:
        return Fraction(-self.numerator, self.denominator)

    def __abs__(self) -> Fraction:
        """Absolute value: |a/b| = |a|/|b|"""
        return Fraction(abs(self.numerator), abs(self.denominator))

    def __float__(self) -> float:
        return self.numerator / self.denominator

    def __int__(self) -> int:
        return self.numerator // self.denominator

    def __str__(self) -> str:
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self) -> str:
        return f"Fraction({self.numerator}, {self.denominator})"

    def reciprocal(self) -> Fraction:
        if self.numerator == 0:
            raise ZeroDivisionError("Cannot get reciprocal of zero")
        return Fraction(self.denominator, self.numerator)
