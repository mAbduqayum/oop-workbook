import pytest
from time_class import Time


class TestTimeCreation:
    def test_time_creation_basic(self):
        t = Time(1, 30, 45)
        assert t.hours == 1
        assert t.minutes == 30
        assert t.seconds == 45

    def test_time_normalization_seconds(self):
        t = Time(0, 0, 90)
        assert t.hours == 0
        assert t.minutes == 1
        assert t.seconds == 30

    def test_time_normalization_minutes(self):
        t = Time(0, 90, 0)
        assert t.hours == 1
        assert t.minutes == 30
        assert t.seconds == 0


class TestTimeAddition:
    def test_add_times(self):
        t1 = Time(1, 30, 45)
        t2 = Time(0, 45, 30)
        t3 = t1 + t2
        assert t3.hours == 2
        assert t3.minutes == 16
        assert t3.seconds == 15


class TestTimeSubtraction:
    def test_subtract_times(self):
        t1 = Time(1, 30, 45)
        t2 = Time(0, 45, 30)
        t3 = t1 - t2
        assert t3.hours == 0
        assert t3.minutes == 45
        assert t3.seconds == 15


class TestTimeMultiplication:
    def test_multiply_by_scalar(self):
        t = Time(0, 45, 30)
        t2 = t * 2
        assert t2.hours == 1
        assert t2.minutes == 31
        assert t2.seconds == 0


class TestTimeDivision:
    def test_divide_by_scalar(self):
        t = Time(2, 0, 0)
        t2 = t / 4
        assert t2.hours == 0
        assert t2.minutes == 30
        assert t2.seconds == 0

    def test_divide_by_zero_raises_error(self):
        t = Time(1, 0, 0)
        with pytest.raises(ZeroDivisionError):
            t / 0


class TestTimeComparison:
    def test_equality(self):
        t1 = Time(1, 30, 0)
        t2 = Time(0, 90, 0)
        assert t1 == t2

    def test_less_than(self):
        t1 = Time(0, 59, 59)
        t2 = Time(1, 0, 0)
        assert t1 < t2


class TestTimeStringRepresentation:
    def test_str_full(self):
        t = Time(1, 30, 45)
        assert str(t) == "1h 30m 45s"

    def test_str_zero(self):
        t = Time(0, 0, 0)
        assert str(t) == "0s"


class TestTimeTotalConversions:
    def test_total_seconds(self):
        t = Time(1, 30, 45)
        assert t.total_seconds() == 5445

    def test_total_minutes(self):
        t = Time(1, 30, 0)
        assert t.total_minutes() == 90.0

    def test_total_hours(self):
        t = Time(2, 30, 0)
        assert t.total_hours() == 2.5
