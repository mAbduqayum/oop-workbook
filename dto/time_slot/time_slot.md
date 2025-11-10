# TimeSlot - Time Validation and Business Logic

## Exercise: TimeSlot Model with Time Range Validation

Create a `TimeSlot` class using Pydantic's `BaseModel` with time validation and business logic.

**Task:**

1. Create a `TimeSlot` class using `BaseModel` with the following fields:
    - `start_time: time` - Start time of the slot
    - `end_time: time` - End time of the slot
    - `title: str` - Title/description of the time slot (1-50 characters)
2. Add a model validator to ensure `start_time` is before `end_time`
3. Add a model validator to ensure duration doesn't exceed 8 hours
4. Implement a `duration_minutes` property that returns the duration in minutes

**Example:**

```python
from datetime import time

slot = TimeSlot(
    start_time=time(9, 0),
    end_time=time(10, 30),
    title="Team Meeting"
)
print(slot.title)  # Team Meeting
print(slot.duration_minutes)  # 90

full_day = TimeSlot(
    start_time=time(9, 0),
    end_time=time(17, 0),
    title="Work Day"
)
print(full_day.duration_minutes)  # 480

# End before start raises ValidationError
TimeSlot(
    start_time=time(10, 0),
    end_time=time(9, 0),
    title="Invalid"
)  # ValidationError

# More than 8 hours raises ValidationError
TimeSlot(
    start_time=time(8, 0),
    end_time=time(20, 0),
    title="Too Long"
)  # ValidationError
```
