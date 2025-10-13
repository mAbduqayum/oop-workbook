from typing import Self


class Time:
    def __init__(self, hours=0, minutes=0, seconds=0) -> None:
        # Store total seconds and then normalize
        total_sec = hours * 3600 + minutes * 60 + seconds

        # Normalize to hours, minutes, seconds
        self.hours = total_sec // 3600
        remaining = total_sec % 3600
        self.minutes = remaining // 60
        self.seconds = remaining % 60

    def __add__(self, other: Self | int) -> Self:
        """Add time durations"""
        if isinstance(other, Time):
            return Time(
                self.hours + other.hours,
                self.minutes + other.minutes,
                self.seconds + other.seconds,
            )
        elif isinstance(other, int):
            return Time(self.hours, self.minutes, self.seconds + other)
        return NotImplemented

    def __sub__(self, other: Self | int) -> Self:
        """Subtract time durations"""
        if isinstance(other, Time):
            return Time(
                self.hours - other.hours,
                self.minutes - other.minutes,
                self.seconds - other.seconds,
            )
        elif isinstance(other, int):
            return Time(self.hours, self.minutes, self.seconds - other)
        return NotImplemented

    def __mul__(self, scalar: int | float) -> Self:
        """Multiply time by a scalar"""
        if isinstance(scalar, (int, float)):
            total_sec = self.total_seconds() * scalar
            return Time(0, 0, int(total_sec))
        return NotImplemented

    def __rmul__(self, scalar: int | float) -> Self:
        """Right multiplication"""
        return self.__mul__(scalar)

    def __truediv__(self, scalar: int | float) -> Self:
        """Divide time by a scalar"""
        if isinstance(scalar, (int, float)):
            if scalar == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            total_sec = self.total_seconds() / scalar
            return Time(0, 0, int(total_sec))
        return NotImplemented

    def __floordiv__(self, other: Self | int) -> int:
        """Floor division"""
        if isinstance(other, Time):
            return self.total_seconds() // other.total_seconds()
        elif isinstance(other, int):
            return self.total_seconds() // other
        return NotImplemented

    def __mod__(self, other: Self) -> Self:
        """Modulo operation"""
        if isinstance(other, Time):
            remainder = self.total_seconds() % other.total_seconds()
            return Time(0, 0, remainder)
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        """Equality comparison"""
        if isinstance(other, Time):
            return self.total_seconds() == other.total_seconds()
        return False

    def __lt__(self, other: Self) -> bool:
        """Less than comparison"""
        if isinstance(other, Time):
            return self.total_seconds() < other.total_seconds()
        return NotImplemented

    def __le__(self, other: Self) -> bool:
        """Less than or equal"""
        return self < other or self == other

    def __gt__(self, other: Self) -> bool:
        """Greater than comparison"""
        if isinstance(other, Time):
            return self.total_seconds() > other.total_seconds()
        return NotImplemented

    def __ge__(self, other: Self) -> bool:
        """Greater than or equal"""
        return self > other or self == other

    def __neg__(self) -> Self:
        """Negation"""
        return Time(-self.hours, -self.minutes, -self.seconds)

    def __abs__(self) -> Self:
        """Absolute value"""
        total_sec = abs(self.total_seconds())
        return Time(0, 0, total_sec)

    def __bool__(self) -> bool:
        """Boolean check - False if zero time"""
        return self.total_seconds() != 0

    def __str__(self) -> str:
        """Human-readable string"""
        if self.hours == 0 and self.minutes == 0 and self.seconds == 0:
            return "0s"

        parts = []
        if self.hours < 0 or self.minutes < 0 or self.seconds < 0:
            prefix = "-"
            h, m, s = abs(self.hours), abs(self.minutes), abs(self.seconds)
        else:
            prefix = ""
            h, m, s = self.hours, self.minutes, self.seconds

        if h != 0:
            parts.append(f"{h}h")
        if m != 0:
            parts.append(f"{m}m")
        if s != 0:
            parts.append(f"{s}s")

        return prefix + " ".join(parts)

    def __repr__(self) -> str:
        """Developer representation"""
        return f"Time({self.hours}, {self.minutes}, {self.seconds})"

    def total_seconds(self) -> int:
        """Return total seconds as int"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def total_minutes(self) -> float:
        """Return total minutes as float"""
        return self.total_seconds() / 60

    def total_hours(self) -> float:
        """Return total hours as float"""
        return self.total_seconds() / 3600
