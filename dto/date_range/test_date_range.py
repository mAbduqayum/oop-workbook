from datetime import date

import pytest
from date_range import DateRange
from pydantic import ValidationError


def test_valid_date_range():
    date_range = DateRange(start_date=date(2024, 1, 1), end_date=date(2024, 12, 31))
    assert date_range.start_date == date(2024, 1, 1)
    assert date_range.end_date == date(2024, 12, 31)


def test_single_day_range():
    date_range = DateRange(start_date=date(2024, 5, 15), end_date=date(2024, 5, 15))
    assert date_range.start_date == date(2024, 5, 15)
    assert date_range.end_date == date(2024, 5, 15)
    assert date_range.duration == 1


def test_invalid_date_range():
    with pytest.raises(ValidationError) as exc_info:
        DateRange(start_date=date(2024, 12, 31), end_date=date(2024, 1, 1))
    assert "start_date must be before or equal to end_date" in str(exc_info.value)


def test_duration_property():
    date_range = DateRange(start_date=date(2024, 1, 1), end_date=date(2024, 12, 31))
    assert date_range.duration == 366  # 2024 is a leap year

    date_range2 = DateRange(start_date=date(2024, 1, 1), end_date=date(2024, 1, 10))
    assert date_range2.duration == 10


def test_serialization():
    date_range = DateRange(start_date=date(2024, 1, 1), end_date=date(2024, 12, 31))
    data = date_range.model_dump()
    assert data == {"start_date": date(2024, 1, 1), "end_date": date(2024, 12, 31)}


def test_json_serialization():
    date_range = DateRange(start_date=date(2024, 1, 1), end_date=date(2024, 12, 31))
    json_str = date_range.model_dump_json()
    date_range2 = DateRange.model_validate_json(json_str)
    assert date_range == date_range2


def test_model_validate():
    data = {"start_date": "2024-01-01", "end_date": "2024-12-31"}
    date_range = DateRange.model_validate(data)
    assert date_range.start_date == date(2024, 1, 1)
    assert date_range.end_date == date(2024, 12, 31)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
