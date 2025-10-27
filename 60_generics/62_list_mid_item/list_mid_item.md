# List Mid Item

## Exercise: Generic Get Middle Item Function

Implement a generic `get_mid_item` function that returns the middle element from a list. For even-length lists, return the first of the two middle elements. Raise `ValueError` with message "List is empty" for empty lists.

**Middle Element Logic:**
```
List length 1: index 0 (the only element)
List length 2: index 0 (first of two middle elements)
List length 3: index 1 (the true middle)
List length 4: index 1 (first of two middle elements)
List length 5: index 2 (the true middle)
```

**Why This Matters:**
Many algorithms need to work with the "middle" of a collection - binary search, quicksort pivot selection, median finding, etc. A generic implementation can handle lists of any type.

**Example Usage:**
```python
# Works with different types
numbers = [1, 2, 3, 4, 5]
print(get_mid_item(numbers))  # 3 (index 2)

words = ["apple", "banana", "cherry", "date"]
print(get_mid_item(words))    # "banana" (index 1)

bools = [True, False, True]
print(get_mid_item(bools))    # False (index 1)

single = [42]
print(get_mid_item(single))   # 42 (index 0)

# Type safety is preserved
mid_num: int = get_mid_item([10, 20, 30])      # Type checker knows it's int
mid_str: str = get_mid_item(["a", "b", "c"])  # Type checker knows it's str

# Error handling
empty: list[int] = []
# get_mid_item(empty)  # Raises ValueError: List is empty
```

**Testing Requirements:**
Your implementation should pass tests that verify:
- Returns correct middle element for odd-length lists
- Returns correct middle element for even-length lists (first of two middle)
- Works with lists of integers
- Works with lists of strings
- Works with lists of custom objects
- Returns the only element for single-element lists
- Raises `ValueError` for empty lists with correct message
- Type hints are correctly specified
