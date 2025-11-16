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
    from datetime import date

    date_range = DateRange(start_date=date(2024, 1, 1), end_date=date(2024, 12, 31))
    print(date_range.start_date)  # 2024-01-01
    print(date_range.duration)  # 366

    # Invalid range raises ValidationError
    DateRange(
        start_date=date(2024, 12, 31), end_date=date(2024, 1, 1)
    )  # ValidationError
