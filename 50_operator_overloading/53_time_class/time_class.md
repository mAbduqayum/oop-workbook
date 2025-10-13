# Python OOP Practice - Operator Overloading: Time Class

## Exercise: Time Duration Arithmetic with Operators

Create a `Time` class that represents time durations (hours, minutes, seconds) and supports arithmetic operations using operator overloading. Times are automatically normalized.

**Instructions:**
Implement a time duration class that handles time arithmetic with automatic normalization (e.g., 90 seconds becomes 1 minute 30 seconds). This demonstrates operator overloading for a practical, real-world use case.

This exercise shows how operator overloading can make working with custom types as natural as working with numbers.

**Your Complete Task:**
1. Create a `Time` class with constructor parameters:
   - `hours` (int, default=0): Number of hours (can be negative)
   - `minutes` (int, default=0): Number of minutes
   - `seconds` (int, default=0): Number of seconds
   - Automatically normalize (e.g., 90 seconds → 1 minute 30 seconds)
   - Support negative time durations
2. Implement `__add__(self, other)` for adding time durations
   - Time + Time: Add all components and normalize
   - Time + int: Add seconds
3. Implement `__sub__(self, other)` for subtracting time durations
   - Can result in negative time
4. Implement `__mul__(self, scalar)` for scaling time
   - Multiply duration by a number (e.g., 2x the time)
5. Implement `__rmul__(self, scalar)` for right-hand multiplication
6. Implement `__truediv__(self, scalar)` for dividing time
   - Divide duration by a number
   - Raise `ZeroDivisionError` if scalar is zero
7. Implement `__floordiv__(self, other)` for division
   - Time // Time: How many times does one duration fit into another
   - Time // int: Integer division of seconds
8. Implement `__mod__(self, other)` for modulo
   - Time % Time: Remainder after division
9. Implement `__eq__(self, other)` for equality
10. Implement `__lt__(self, other)` for less than
11. Implement `__le__(self, other)` for less than or equal
12. Implement `__gt__(self, other)` for greater than
13. Implement `__ge__(self, other)` for greater than or equal
14. Implement `__neg__(self)` for negation
15. Implement `__abs__(self)` for absolute value
16. Implement `__bool__(self)` to return `False` if time is zero
17. Implement `__str__(self)` to return formatted time like `"1h 30m 45s"` or `"-2h 15m 30s"`
    - Skip zero components (e.g., `"30m"` not `"0h 30m 0s"`)
    - Handle zero time as `"0s"`
18. Implement `__repr__(self)` to return `"Time(hours, minutes, seconds)"`
19. Add `total_seconds(self)` method that returns total seconds as int
20. Add `total_minutes(self)` method that returns total minutes as float
21. Add `total_hours(self)` method that returns total hours as float

**What You'll Learn:**
- **Automatic normalization:** Convert overflow (e.g., 90 seconds → 1m 30s)
- **Mixed operations:** Support different operand types
- **Practical operators:** Time arithmetic for real-world use cases
- **Negative values:** Handle negative time durations
- **Multiple representations:** Same duration, different formats

**Normalization Rules:**
- 60 seconds = 1 minute
- 60 minutes = 1 hour
- Keep seconds in range [0, 59]
- Keep minutes in range [0, 59]
- Hours can be any value
- Negative time: normalize and track sign

**Example Usage:**
```python
# Create time durations
t1 = Time(1, 30, 45)  # 1h 30m 45s
t2 = Time(0, 45, 30)  # 45m 30s

# Automatic normalization
t3 = Time(0, 0, 90)
print(t3)  # 1m 30s (not 0h 0m 90s)

t4 = Time(0, 90, 0)
print(t4)  # 1h 30m (not 0h 90m 0s)

t5 = Time(0, 0, 3661)
print(t5)  # 1h 1m 1s

# Addition
t6 = t1 + t2
print(t6)  # 2h 16m 15s

# Subtraction
t7 = t1 - t2
print(t7)  # 45m 15s

# Multiplication (scaling)
t8 = t2 * 2
print(t8)  # 1h 31m

t9 = 3 * Time(0, 20, 0)
print(t9)  # 1h

# Division
t10 = Time(2, 0, 0) / 4
print(t10)  # 30m

# How many times does one duration fit in another?
long_time = Time(2, 30, 0)  # 2.5 hours
short_time = Time(0, 30, 0)  # 30 minutes
print(long_time // short_time)  # 5 (fits 5 times)

# Remainder
print(Time(1, 40, 0) % Time(1, 0, 0))  # 40m

# Comparison
print(Time(1, 0, 0) > Time(0, 59, 59))  # True
print(Time(1, 30, 0) == Time(0, 90, 0))  # True (both are 1h 30m)
print(Time(2, 0, 0) < Time(1, 0, 0))  # False

# Negation
t11 = -Time(1, 30, 0)
print(t11)  # -1h 30m

# Absolute value
t12 = abs(Time(-2, -30, 0))
print(t12)  # 2h 30m

# Boolean check (zero time)
if not Time(0, 0, 0):
    print("Time is zero")

if Time(1, 0, 0):
    print("Time is non-zero")

# Total conversions
duration = Time(1, 30, 45)
print(duration.total_seconds())  # 5445
print(duration.total_minutes())  # 90.75
print(duration.total_hours())  # 1.5125

# Negative time (past events or countdowns)
past = Time(-1, -15, 0)
print(past)  # -1h 15m
print(past.total_seconds())  # -4500

# Real-world examples
movie_length = Time(2, 15, 0)
break_time = Time(0, 15, 0)
total_event = movie_length + break_time
print(f"Total event time: {total_event}")  # 2h 30m

# Splitting time
work_shift = Time(8, 0, 0)
num_tasks = 5
time_per_task = work_shift / num_tasks
print(f"Time per task: {time_per_task}")  # 1h 36m

# Meeting schedule
meeting_duration = Time(0, 45, 0)
num_meetings = 3
total_meetings = meeting_duration * num_meetings
print(f"Total meeting time: {total_meetings}")  # 2h 15m

# Countdown
remaining = Time(1, 30, 0) - Time(0, 45, 30)
print(f"Time remaining: {remaining}")  # 44m 30s

# Complex expression
result = (Time(2, 0, 0) + Time(1, 30, 0)) / 2 - Time(0, 15, 0)
print(result)  # 1h 30m

# Edge cases
print(Time(0, 0, 0))  # 0s
print(Time(-0, -0, -30))  # -30s

# Error handling
try:
    invalid = Time(1, 0, 0) / 0
except ZeroDivisionError as e:
    print(e)  # Cannot divide by zero

# Adding integers (seconds)
quick_time = Time(0, 1, 0) + 30
print(quick_time)  # 1m 30s
```

**Key Operator Overloading Concepts:**
- **Automatic normalization:** Always maintain valid time format
- **Natural arithmetic:** Use standard operators for time calculations
- **Mixed types:** Support operations with integers (seconds)
- **Negative durations:** Handle past times or countdowns
- **Division semantics:** Both scaling (/) and quotient (//)

**Test Cases to Consider:**
```python
# Normalization
assert Time(0, 0, 60) == Time(0, 1, 0)
assert Time(0, 60, 0) == Time(1, 0, 0)
assert Time(0, 0, 3600) == Time(1, 0, 0)

# Addition
assert Time(0, 30, 0) + Time(0, 30, 0) == Time(1, 0, 0)
assert Time(0, 45, 30) + Time(0, 15, 30) == Time(1, 1, 0)

# Subtraction
assert Time(1, 0, 0) - Time(0, 30, 0) == Time(0, 30, 0)
assert Time(0, 30, 0) - Time(1, 0, 0) == Time(-0, -30, 0)

# Multiplication
assert Time(0, 30, 0) * 2 == Time(1, 0, 0)
assert 3 * Time(0, 20, 0) == Time(1, 0, 0)

# Division
assert Time(1, 0, 0) / 2 == Time(0, 30, 0)
assert Time(1, 0, 0) // Time(0, 20, 0) == 3

# Comparison
assert Time(1, 0, 0) > Time(0, 59, 59)
assert Time(1, 30, 0) == Time(0, 90, 0)

# Total conversions
assert Time(1, 0, 0).total_seconds() == 3600
assert Time(0, 30, 0).total_minutes() == 30
assert Time(2, 30, 0).total_hours() == 2.5
```

**Challenge Extensions:**
- Add `from_seconds(seconds)` class method
- Implement `__format__(self, format_spec)` for custom formatting
- Add `to_12hour()` method for clock time (with AM/PM)
- Implement `to_iso8601()` for ISO duration format (e.g., "PT1H30M")
- Add `__iadd__`, `__isub__` for in-place operations
- Implement `split(num_parts)` to divide time into equal parts
- Add `round_to(unit)` method (e.g., round to nearest minute)
- Support microseconds for high-precision timing
