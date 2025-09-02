# 💡 Hints for Student Class Exercise

## Class with List Attribute
- Initialize `grades` as empty list: `self.grades = []`
- Lists are mutable - you can add items later
- Each student object gets its own separate grades list

## Adding Items to Lists
- Use `append()` method: `self.grades.append(grade)`
- Check if grade is valid before adding: `if 0 <= grade <= 100:`
- Always validate input data

## Working with Lists of Numbers
- Check if list is empty: `if not self.grades:`
- Sum all grades: `sum(self.grades)`
- Count items: `len(self.grades)`
- Loop through items: `for grade in self.grades:`

## GPA Conversion Logic
- Convert percentage grades to 4.0 scale
- Common scale: 90-100 = A (4.0), 80-89 = B (3.0), etc.
- Calculate average of converted grades
- Use conditional statements (if/elif) for grade ranges

## Method That Changes Attributes
- `change_major()` should update `self.major`
- Store old value if you want to show the change
- Methods can modify any attribute of the object

## List vs Single Value Attributes
- `name`, `student_id`, `major` are single values
- `grades` is a list that grows over time
- Methods can work with both types of attributes

## Mathematical Operations
- Average = sum of all values / count of values
- Use `sum()` and `len()` functions
- Format decimals with `:.2f` for 2 decimal places

## Step-by-Step Approach
1. Write class with `__init__` method for all attributes
2. Add `add_grade()` method with validation
3. Add `calculate_gpa()` method with conversion logic
4. Add `change_major()` method
5. Create three students and test all methods

## Common Pitfalls
- Don't forget to initialize `grades` as empty list
- Validate grade range (0-100) before adding
- Handle empty grades list in GPA calculation
- Remember to update the attribute in `change_major()`