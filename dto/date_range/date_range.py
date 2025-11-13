from datetime import date

from pydantic import BaseModel, model_validator
from typing_extensions import Self


class DateRange(BaseModel):
    start_date: date
    end_date: date

    @model_validator(mode="after")
    def validate_date_range(self) -> Self:
        if self.start_date > self.end_date:
            raise ValueError("start_date must be before or equal to end_date")
        return self

    @property
    def duration(self) -> int:
        """Return the number of days in the date range (inclusive)."""
        return (self.end_date - self.start_date).days + 1


if __name__ == "__main__":
    date_range = DateRange(start_date=date(2024, 1, 1), end_date=date(2024, 12, 31))
    print(f"Start: {date_range.start_date}")
    print(f"End: {date_range.end_date}")
    print(f"Duration: {date_range.duration} days")
