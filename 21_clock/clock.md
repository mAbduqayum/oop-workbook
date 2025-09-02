# 🕐 Python OOP Practice - Lesson 21: Clock Class

## 📝 Exercise: Implement a Clock That Handles Times Without Dates

Create a `Clock` class that represents time and supports arithmetic operations. This introduces object representation and equality.

**Instructions:**
Implement a clock that handles times without dates.

You should be able to add and subtract minutes to it.

Two clocks that represent the same time should be equal to each other.

**Your Complete Task:**
1. Create a `Clock` class that takes `hour` and `minute` in the constructor
2. Normalize time automatically (25 hours → 1 hour, 70 minutes → 1 hour 10 minutes)
3. Add an `add_minutes(minutes)` method that adds minutes to the clock
4. Add a `subtract_minutes(minutes)` method that subtracts minutes from the clock
5. Implement `__str__()` method that returns time in "HH:MM" format for human-readable output
6. Implement `__repr__()` method that returns valid Python code: `Clock(11, 30)`
7. Implement `__eq__()` method so two clocks with same time are equal
8. Create clocks, perform operations, and test equality

**What You'll Learn:**
- **String Representation:** `__str__()` for human-readable output, `__repr__()` for debugging
- **Object Equality:** `__eq__()` method for comparing objects
- **Time Arithmetic:** Adding/subtracting with proper overflow handling
- **Data Validation:** Automatic time normalization
- **Special Methods:** Magic methods that make objects behave naturally

**Example Usage:**
```python
clock1 = Clock(11, 30)
clock2 = Clock(11, 30)
print(str(clock1))      # 11:30
print(repr(clock1))     # Clock(11, 30)
print(clock1 == clock2) # True

clock3 = Clock(12, 0)
print(clock1 == clock3) # False

clock1.add_minutes(60)
print(clock1)           # 12:30
clock1.subtract_minutes(120)
print(clock1)           # 10:30
```

**Success Criteria:**
- ✅ Clock class handles hour and minute with automatic normalization
- ✅ `__str__()` returns "HH:MM" format for display
- ✅ `__repr__()` returns "Clock(hour, minute)" for debugging
- ✅ `__eq__()` allows clock comparison with == operator
- ✅ add_minutes() and subtract_minutes() work with overflow/underflow
- ✅ Two clocks with same time are equal
- ✅ Time normalization handles edge cases (25:70 → 02:10)