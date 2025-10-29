from __future__ import annotations


class Time:
    def __init__(self, hours=0, minutes=0, seconds=0) -> None:
        # Store total seconds and then normalize
        total_sec = hours * 3600 + minutes * 60 + seconds

        # Normalize to hours, minutes, seconds
        self.hours = total_sec // 3600
        remaining = total_sec % 3600
        self.minutes = remaining // 60
        self.seconds = remaining % 60

    def __add__(self, other: Time | int) -> Time:
        if isinstance(other, int):
            other = Time(seconds=other)
        return Time(
            self.hours + other.hours,
            self.minutes + other.minutes,
            self.seconds + other.seconds,
        )

    def __sub__(self, other: Time | int) -> Time:
        if isinstance(other, int):
            other = Time(seconds=other)
        return Time(
            self.hours - other.hours,
            self.minutes - other.minutes,
            self.seconds - other.seconds,
        )

    def __mul__(self, scalar: int | float) -> Time:
        if isinstance(scalar, (int, float)):
            total_sec = self.total_seconds() * scalar
            return Time(0, 0, int(total_sec))

    def __rmul__(self, scalar: int | float) -> Time:
        return self.__mul__(scalar)

    def __truediv__(self, scalar: int | float) -> Time:
        if isinstance(scalar, (int, float)):
            if scalar == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            total_sec = self.total_seconds() / scalar
            return Time(0, 0, int(total_sec))

    def __eq__(self, other: object) -> bool:
        """Equality comparison"""
        if isinstance(other, Time):
            return self.total_seconds() == other.total_seconds()
        return False

    def __lt__(self, other: Time) -> bool:
        return self.total_seconds() < other.total_seconds()

    def __le__(self, other: Time) -> bool:
        """Less than or equal"""
        return self < other or self == other

    def __gt__(self, other: Time) -> bool:
        """Greater than comparison"""
        if isinstance(other, Time):
            return self.total_seconds() > other.total_seconds()
        return NotImplemented

    def __ge__(self, other: Time) -> bool:
        """Greater than or equal"""
        return self > other or self == other

    def __neg__(self) -> Time:
        """Negation"""
        return Time(-self.hours, -self.minutes, -self.seconds)

    def __abs__(self) -> Time:
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
