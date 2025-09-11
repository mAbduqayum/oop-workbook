# 🎓 Python OOP Practice - Lesson: Student Class

## 📝 Exercise: Build a Student Grade Tracking System

Create a `Student` class that manages student information and grades. This introduces list management and mathematical calculations.

**Your Complete Task:**
1. Create a `Student` class with `name`, `student_id`, `grades` (empty list), and `major` attributes
2. Add an `add_grade(grade)` method that adds a grade (0-100) to the grades list
3. Add a `calculate_gpa()` method that converts grades to 4.0 scale and returns average
4. Add a `change_major(new_major)` method that updates the major
5. Create three student objects with different information
6. Add multiple grades to each student (at least 3 grades per student)
7. Calculate and display each student's GPA
8. Change one student's major and confirm the change

**What You'll Learn:**
- **List Management:** Adding items to object attributes that are lists
- **Mathematical Operations:** Converting grades and calculating averages
- **Data Validation:** Ensuring grades are within valid range (0-100)
- **State Modification:** Changing object attributes after creation
- **Complex Object State:** Objects with multiple types of data (strings, numbers, lists)

**Example Usage:**
```python
# Create student objects
student1 = Student("Alice Johnson", "S12345", "Computer Science")
student2 = Student("Bob Smith", "S12346", "Mathematics")
student3 = Student("Carol Davis", "S12347", "Physics")

# Add grades to each student
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

student2.add_grade(95)
student2.add_grade(88)
student2.add_grade(91)

student3.add_grade(82)
student3.add_grade(89)
student3.add_grade(85)

# Calculate and display GPAs
print(f"Alice's GPA: {student1.calculate_gpa():.2f}")  # Alice's GPA: 3.17
print(f"Bob's GPA: {student2.calculate_gpa():.2f}")    # Bob's GPA: 3.58
print(f"Carol's GPA: {student3.calculate_gpa():.2f}")  # Carol's GPA: 3.17

# Change a student's major
print(f"Alice's current major: {student1.major}")      # Alice's current major: Computer Science
student1.change_major("Data Science")
print(f"Alice's new major: {student1.major}")          # Alice's new major: Data Science
```

