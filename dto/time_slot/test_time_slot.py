from datetime import time

import pytest
from pydantic import ValidationError
from time_slot import TimeSlot


def test_time_slot_basic():
    slot = TimeSlot(start_time=time(9, 0), end_time=time(10, 30), title="Team Meeting")
    assert slot.start_time == time(9, 0)
    assert slot.end_time == time(10, 30)
    assert slot.title == "Team Meeting"


def test_duration_minutes_90():
    slot = TimeSlot(start_time=time(9, 0), end_time=time(10, 30), title="Team Meeting")
    assert slot.duration_minutes == 90


def test_duration_minutes_480():
    slot = TimeSlot(start_time=time(9, 0), end_time=time(17, 0), title="Work Day")
    assert slot.duration_minutes == 480


def test_duration_minutes_60():
    slot = TimeSlot(start_time=time(14, 0), end_time=time(15, 0), title="Lunch Break")
    assert slot.duration_minutes == 60


def test_duration_minutes_30():
    slot = TimeSlot(start_time=time(10, 0), end_time=time(10, 30), title="Quick Sync")
    assert slot.duration_minutes == 30


def test_full_work_day():
    slot = TimeSlot(start_time=time(9, 0), end_time=time(17, 0), title="Work Day")
    assert slot.duration_minutes == 480


def test_end_before_start_raises_error():
    with pytest.raises(ValidationError):
        TimeSlot(start_time=time(10, 0), end_time=time(9, 0), title="Invalid")


def test_same_start_and_end_raises_error():
    with pytest.raises(ValidationError):
        TimeSlot(start_time=time(10, 0), end_time=time(10, 0), title="Invalid")


def test_duration_exceeds_8_hours():
    with pytest.raises(ValidationError):
        TimeSlot(start_time=time(8, 0), end_time=time(20, 0), title="Too Long")


def test_duration_exceeds_8_hours_by_one_minute():
    with pytest.raises(ValidationError):
        TimeSlot(start_time=time(9, 0), end_time=time(17, 1), title="Too Long")


def test_exactly_8_hours_allowed():
    slot = TimeSlot(start_time=time(9, 0), end_time=time(17, 0), title="Full Day")
    assert slot.duration_minutes == 480


def test_empty_title():
    with pytest.raises(ValidationError):
        TimeSlot(start_time=time(9, 0), end_time=time(10, 0), title="")


def test_title_too_long():
    with pytest.raises(ValidationError):
        TimeSlot(start_time=time(9, 0), end_time=time(10, 0), title="x" * 51)


def test_serialization():
    slot = TimeSlot(start_time=time(9, 0), end_time=time(10, 30), title="Team Meeting")
    data = slot.model_dump()
    assert data["start_time"] == time(9, 0)
    assert data["end_time"] == time(10, 30)
    assert data["title"] == "Team Meeting"
