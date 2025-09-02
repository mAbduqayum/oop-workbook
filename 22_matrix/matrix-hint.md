# 💡 Hints for Matrix Exercise

## String Parsing Strategy
- Use `.strip()` to remove extra whitespace
- Use `.split('\n')` to separate rows
- Use `.split()` to separate numbers in each row
- Convert strings to integers: `int(num)`

## Building the 2D Structure
```python
# Parse each row
rows = matrix_string.strip().split('\n')
for row in rows:
    numbers = [int(num) for num in row.split()]
    self._data.append(numbers)
```

## Understanding Indexing
- Exercise uses 1-based indexing (row 1, column 1)
- Python uses 0-based indexing internally
- Convert: `index - 1` when accessing internal data
- `matrix.row(1)` should return first row (`self._data[0]`)

## Row Access
- Rows are easy: just return the list at that index
- `self._data[index - 1]` gives you the row
- Return a copy to prevent external modification: `row[:]`

## Column Access
- Columns require collecting same index from each row
- Use list comprehension: `[row[col_index] for row in self._data]`
- Example: column 1 = `[row[0] for row in self._data]`

## Properties vs Methods
- `@property` decorator makes methods act like attributes
- Call without parentheses: `matrix.rows` not `matrix.rows()`
- Properties should return computed values
- Use properties for data that's calculated from internal state

## Property Implementation
```python
@property
def rows(self):
    return [row[:] for row in self._data]  # Return copies

@property  
def columns(self):
    # Calculate all columns and return as list
```

## Data Structure Visualization
```
String: "9 8 7\n5 3 2\n6 6 7"

Visual representation:
    1  2  3
  |---------
1 | 9  8  7
2 | 5  3  2
3 | 6  6  7

After parsing:
self._data = [
    [9, 8, 7],  # row 0 (accessed as row 1)
    [5, 3, 2],  # row 1 (accessed as row 2)
    [6, 6, 7]   # row 2 (accessed as row 3)
]
```

## Column Calculation Logic
- For each column index (0, 1, 2...)
- Go through each row and take that index
- Column 0: [9, 5, 6], Column 1: [8, 3, 6], Column 2: [7, 2, 7]

## List Comprehension Patterns
```python
# Row access (simple)
return self._data[index - 1]

# Column access (extract from all rows)
return [row[index - 1] for row in self._data]

# All rows (copy each)
return [row[:] for row in self._data]
```

## Testing Your Implementation
1. Create matrix with Exercism example: "9 8 7\n5 3 2\n6 6 7"
2. Test row(1) returns [9, 8, 7]
3. Test column(1) returns [9, 5, 6]
4. Test row(2) returns [5, 3, 2] and column(2) returns [8, 3, 6]
5. Test properties return correct 2D structures
6. Try different matrix sizes to ensure robustness

## Common Mistakes
- Forgetting to convert strings to integers
- Using 0-based indexing instead of 1-based
- Not making copies of data (returning references)
- Confusing row/column access patterns
- Forgetting `@property` decorator for properties
- Not handling empty or malformed input gracefully

## Data Protection
- Store data in `self._data` (underscore suggests "private")
- Return copies, not direct references to internal data
- This prevents external code from accidentally modifying your matrix