# 💡 Quick Hints

1. Parse string: `.strip().split('\n')` then `.split()` and `int()` 
2. Store in `self._data` as list of lists
3. `row(index)` - return `self._data[index - 1][:]` (1-based indexing)
4. `column(index)` - return `[row[index - 1] for row in self._data]`
5. `@property` for `rows` and `columns` - return all rows/columns