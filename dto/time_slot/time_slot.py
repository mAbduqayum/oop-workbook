from datetime import datetime, time, timedelta

from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self


class TimeSlot(BaseModel):
    start_time: time
    end_time: time
    title: str = Field(min_length=1, max_length=50)

    def _get_duration(self) -> timedelta:
        start_dt = datetime.combine(datetime.today(), self.start_time)
        end_dt = datetime.combine(datetime.today(), self.end_time)
        return end_dt - start_dt

    @model_validator(mode="after")
    def validate_times(self) -> Self:
        duration = self._get_duration()

        if duration.total_seconds() <= 0:
            raise ValueError("start_time must be before end_time")

        if duration > timedelta(hours=8):
            raise ValueError("duration cannot exceed 8 hours")

        return self

    @property
    def duration_minutes(self) -> int:
        return int(self._get_duration().total_seconds() / 60)
