# 🔢 Python OOP Practice - Lesson 24: Counter Class

## 📝 Exercise: Bounded Counter with State Management

Create a `Counter` class that manages a count value with configurable minimum and maximum bounds. This demonstrates state management with constraints and validation.

**Instructions:**
Implement a counter that can increment, decrement, and reset while respecting boundary limits.

The counter should enforce minimum and maximum values and prevent invalid operations.

You should be able to configure the bounds and get information about the counter's state.

**Your Complete Task:**
1. Create a `Counter` class that takes optional `min_value` (default 0) and `max_value` (default 100) in constructor
2. Initialize counter to the minimum value
3. Store the current count privately with underscore prefix (`_count`)
4. Add `increment(step=1)` method that increases count by step amount
5. Add `decrement(step=1)` method that decreases count by step amount
6. Add `reset()` method that sets count back to minimum value
7. Add `value` property that returns current count (read-only)
8. Add `is_at_min` property that returns True if counter is at minimum
9. Add `is_at_max` property that returns True if counter is at maximum
10. Prevent incrementing beyond max_value and decrementing below min_value
11. Raise `ValueError` if trying to create counter with min_value >= max_value
12. Add `__str__()` method that returns "Counter: count/max (min-max)"

**What You'll Learn:**
- **State Management:** Tracking and validating object state changes
- **Boundary Validation:** Preventing invalid state transitions
- **Read-Only Properties:** Exposing data without allowing direct modification
- **Default Parameters:** Flexible constructor design
- **Constraint Enforcement:** Maintaining object invariants

**Example Usage:**
```python
# Create counter with default bounds (0-100)
counter = Counter()
print(counter)              # "Counter: 0/100 (0-100)"
print(counter.value)        # 0
print(counter.is_at_min)    # True
print(counter.is_at_max)    # False

# Increment operations
counter.increment()         # +1
print(counter.value)        # 1
counter.increment(5)        # +5
print(counter.value)        # 6

# Decrement operations
counter.decrement()         # -1
print(counter.value)        # 5
counter.decrement(3)        # -3
print(counter.value)        # 2

# Reset counter
counter.reset()
print(counter.value)        # 0

# Custom bounds
game_counter = Counter(min_value=1, max_value=10)
print(game_counter.value)   # 1
game_counter.increment(15)  # Should not exceed max
print(game_counter.value)   # 10 (capped at maximum)
print(game_counter.is_at_max)  # True

# Boundary testing
game_counter.decrement(20)  # Should not go below min
print(game_counter.value)   # 1 (capped at minimum)

# Invalid counter creation
try:
    bad_counter = Counter(min_value=10, max_value=5)
except ValueError as e:
    print(e)  # "min_value must be less than max_value"
```

**Bonus Challenge:**
Add a `history` property that tracks all operations performed on the counter as a list of strings (e.g., ["increment(1)", "decrement(3)", "reset()"]).
