# DateRange - Pydantic Date Validation

## Exercise: DateRange Model with Date Validation

Create a `DateRange` class using Pydantic's `BaseModel` with validation to ensure the start date comes before the end
date.

**Task:**

1. Create a `DateRange` class using `BaseModel` with the following fields:
    - `start_date: date` - Start date of the range
    - `end_date: date` - End date of the range
2. Add a model validator to ensure `start_date` is before or equal to `end_date`
3. Implement a `duration` property that returns the number of days in the range

**Example:**

```python
from datetime import date

date_range = DateRange(start_date=date(2024, 1, 1), end_date=date(2024, 12, 31))
print(date_range.start_date)  # 2024-01-01
print(date_range.duration)  # 366

# Invalid range raises ValidationError
DateRange(start_date=date(2024, 12, 31), end_date=date(2024, 1, 1))  # ValidationError
```
