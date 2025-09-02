# 💡 Hints for Clock Exercise

## Time Normalization Logic
- Minutes >= 60 should add to hours: `hour += 1, minute -= 60`
- Negative minutes should subtract from hours: `hour -= 1, minute += 60`
- Hours should wrap around 24: use `hour % 24`
- Create a helper method to handle this logic

## The `__str__` Special Method
- This method runs automatically when you `print()` an object
- Must `return` a string (not print!)
- Format: `f"{self.hour:02d}:{self.minute:02d}"`
- `:02d` means "2 digits with leading zeros"

## Time Arithmetic
- Adding minutes might cause hour overflow
- Subtracting minutes might cause negative minutes
- Always normalize after any time change
- Use your helper method in both add/subtract

## Constructor Tips
- Take hour and minute as parameters
- Store them as attributes
- Call normalize method to handle invalid input like Clock(25, 70)

## Helper Method Pattern
```python
def _normalize_time(self):
    # Handle minute overflow
    # Handle hour overflow
    # This method is "private" (starts with _)
```

## String Formatting
- `{self.hour:02d}` formats number with 2 digits
- Examples: 5 becomes "05", 12 stays "12"
- This ensures consistent "HH:MM" format

## Testing Edge Cases
- Test Clock(25, 0) → should become 01:00
- Test Clock(0, -30) → should become 23:30
- Test Clock(23, 59) then add 2 minutes → should become 00:01
- Test normal times like Clock(8, 30) → should stay 08:30

## Method Call Flow
1. Constructor calls `_normalize_time()`
2. `add_minutes()` changes minute, calls `_normalize_time()`
3. `subtract_minutes()` changes minute, calls `_normalize_time()`
4. `print()` automatically calls `__str__()`

## Common Mistakes
- Forgetting to normalize time after operations
- Using `print()` instead of `return` in `__str__()`
- Not handling negative minutes correctly
- Forgetting leading zeros in time format
- Not using modulo (%) for 24-hour wraparound