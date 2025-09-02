# 🕐 Python OOP Practice - Lesson 6: Clock Class

## 📝 Exercise: Build a Digital Clock

Create a `Clock` class that handles time without dates. This introduces string representation and time arithmetic.

**Your Complete Task:**
1. Create a `Clock` class that takes `hour` and `minute` in the constructor
2. Handle time overflow (25 hours becomes 1 hour, 70 minutes becomes 1 hour 10 minutes)
3. Add an `add_minutes(minutes)` method that adds minutes to the clock
4. Add a `subtract_minutes(minutes)` method that subtracts minutes from the clock
5. Add a `__str__()` method that returns time in "HH:MM" format (24-hour format)
6. Create clocks, perform time operations, and print the results

**What You'll Learn:**
- Time arithmetic and modulo operations
- The `__str__()` special method for object representation
- Handling edge cases (time overflow/underflow)
- Creating objects that can be printed naturally
- Mathematical operations on object state

**Expected Output:**
```
08:00
09:30
07:30
10:03
23:59
00:01
```

**Success Criteria:**
- ✅ Clock class properly handles hour and minute initialization
- ✅ Time overflow is handled correctly (25:70 → 02:10)
- ✅ add_minutes() method correctly adds time
- ✅ subtract_minutes() method correctly subtracts time
- ✅ __str__() method returns properly formatted "HH:MM" string
- ✅ Clocks can be printed directly with print() function