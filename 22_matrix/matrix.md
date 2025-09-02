# 🔢 Python OOP Practice - Lesson 22: Matrix Class

## 📝 Exercise: Parse Matrix Rows and Columns

**Instructions:**
Given a string representing a matrix of numbers, return the rows and columns of that matrix.

So given a string with embedded newlines like:
```
9 8 7
5 3 2
6 6 7
```

representing this matrix:
```
    1  2  3
  |---------
1 | 9  8  7
2 | 5  3  2
3 | 6  6  7
```

your code should be able to spit out:

- A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows
- A list of the columns, reading each column top-to-bottom while moving from left-to-right

**The rows for our example matrix:**
```
9, 8, 7
5, 3, 2
6, 6, 7
```

**And its columns:**
```
9, 5, 6
8, 3, 6
7, 2, 7
```

In this exercise you're going to create a class. Don't worry, it's not as complicated as you think!

**Your Complete Task:**
1. Create a `Matrix` class that takes a matrix string in the constructor
2. Parse the string into a 2D structure (rows separated by newlines, numbers by spaces)
3. Add a `row(index)` method that returns the specified row as a list (1-indexed)
4. Add a `column(index)` method that returns the specified column as a list (1-indexed)
5. Add a `rows` property that returns all rows as a list of lists
6. Add a `columns` property that returns all columns as a list of lists

**What You'll Learn:**
- **String Parsing:** Converting text input into structured data
- **2D Data Structures:** Working with lists of lists
- **Properties:** Using `@property` decorator for computed attributes
- **Index Conversion:** Handling 1-based vs 0-based indexing
- **Data Access Patterns:** Different ways to slice and access 2D data

**Example Usage:**
```python
matrix_string = "9 8 7\n5 3 2\n6 6 7"
matrix = Matrix(matrix_string)

# Access individual rows and columns
print(matrix.row(1))     # [9, 8, 7]
print(matrix.column(2))  # [8, 3, 6]

# Access all rows and columns
print(matrix.rows)       # [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
print(matrix.columns)    # [[9, 5, 6], [8, 3, 6], [7, 2, 7]]
```

**Success Criteria:**
- ✅ Matrix class parses string input correctly
- ✅ row(index) returns correct row using 1-based indexing
- ✅ column(index) returns correct column using 1-based indexing
- ✅ rows property returns all rows as list of lists
- ✅ columns property returns all columns as list of lists
- ✅ Handles the example matrix (9 8 7 / 5 3 2 / 6 6 7) correctly