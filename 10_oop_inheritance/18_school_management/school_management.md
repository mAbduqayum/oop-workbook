# Exercise: School Management System

Design classes for a comprehensive school management system using inheritance and role-based functionality.

## Requirements

Create a person hierarchy with different roles and responsibilities in a school system:

### Base Class: `Person`
- **Attributes:**
  - `name` (string): Full name
  - `person_id` (string): Unique identifier
  - `contact_info` (dict): Email, phone, address
  - `date_of_birth` (string): Birth date
  - `emergency_contact` (dict): Emergency contact information

- **Methods:**
  - `__init__(name, person_id, contact_info)`: Constructor
  - `get_info()`: Return formatted person information (to be overridden)
  - `update_contact(info_type, value)`: Update contact information
  - `get_age()`: Calculate age from date of birth
  - `send_notification(message)`: Send notification to person

### Derived Class: `Student`
- **Additional Attributes:**
  - `grade` (int): Current grade level (K-12)
  - `subjects` (list): List of enrolled subjects
  - `grades` (dict): Subject grades dictionary
  - `attendance` (dict): Attendance record by date
  - `gpa` (float): Current GPA

- **Override Methods:**
  - `get_info()`: Include student-specific information
  - Additional methods: `enroll_subject(subject)`, `add_grade(subject, grade)`, `mark_attendance(date, status)`, `calculate_gpa()`, `get_transcript()`

### Derived Class: `Teacher`
- **Additional Attributes:**
  - `department` (string): Teaching department
  - `subjects_taught` (list): Subjects they teach
  - `salary` (float): Annual salary
  - `classes` (list): List of assigned classes
  - `office_hours` (dict): Office hours schedule

- **Override Methods:**
  - `get_info()`: Include teacher-specific information
  - Additional methods: `assign_class(class_name)`, `add_subject(subject)`, `grade_student(student_id, subject, grade)`, `set_office_hours(schedule)`

### Derived Class: `Staff`
- **Additional Attributes:**
  - `role` (string): Job role (administrator, janitor, nurse, etc.)
  - `department` (string): Working department
  - `shift` (string): Work shift (morning, afternoon, night)
  - `salary` (float): Annual salary
  - `supervisor` (string): Supervisor name

- **Override Methods:**
  - `get_info()`: Include staff-specific information
  - Additional methods: `assign_task(task)`, `clock_in()`, `clock_out()`, `request_leave(date, reason)`

## Additional System Classes

### Class: `SchoolClass`
- **Attributes:**
  - `class_id` (string): Class identifier
  - `subject` (string): Subject being taught
  - `teacher` (Teacher): Assigned teacher
  - `students` (list): Enrolled students
  - `schedule` (dict): Class schedule
  - `room` (string): Classroom location

### Class: `School`
- **Attributes:**
  - `name` (string): School name
  - `people` (list): All people in the system
  - `classes` (list): All classes

- **Methods:**
  - `add_person(person)`: Add person to school
  - `find_person(person_id)`: Find person by ID
  - `get_students_by_grade(grade)`: Get all students in a grade
  - `get_teachers_by_department(dept)`: Get teachers by department
  - `generate_report()`: Generate school report

## Example Usage

```python
# Create school
school = School("Washington High School")

# Create people
student = Student("John Doe", "S001", {"email": "john@email.com", "phone": "555-1234"})
teacher = Teacher("Ms. Smith", "T001", {"email": "smith@school.edu", "phone": "555-5678"})
staff = Staff("Bob Wilson", "ST001", {"email": "bob@school.edu", "phone": "555-9012"})

# Set up student
student.grade = 10
student.enroll_subject("Mathematics")
student.enroll_subject("English")
student.add_grade("Mathematics", 87)
student.add_grade("English", 92)

# Set up teacher
teacher.department = "Mathematics"
teacher.add_subject("Algebra")
teacher.add_subject("Geometry")
teacher.assign_class("Math 101")

# Set up staff
staff.role = "Administrator"
staff.department = "Office"
staff.shift = "morning"

# Add to school
school.add_person(student)
school.add_person(teacher)
school.add_person(staff)

# Display information
print(student.get_info())
print(teacher.get_info())
print(staff.get_info())

# Generate reports
print(f"Student GPA: {student.calculate_gpa():.2f}")
print(school.generate_report())
```

## Expected Output

```
Student: John Doe (ID: S001)
Grade: 10, GPA: 89.5
Subjects: Mathematics, English
Contact: john@email.com, 555-1234
Grades: Mathematics: 87, English: 92

Teacher: Ms. Smith (ID: T001)
Department: Mathematics
Subjects Taught: Algebra, Geometry
Classes: Math 101
Office Hours: Not Set
Contact: smith@school.edu, 555-5678

Staff: Bob Wilson (ID: ST001)
Role: Administrator, Department: Office
Shift: morning
Contact: bob@school.edu, 555-9012

Student GPA: 89.50

Washington High School Report:
Total People: 3
Students: 1, Teachers: 1, Staff: 1
Average Student GPA: 89.5
```

## Learning Objectives

- Design complex inheritance hierarchies
- Implement role-based access and functionality
- Practice composition (School contains People and Classes)
- Work with data management and reporting
- Handle different types of records (grades, attendance)
- Implement search and filtering functionality
- Understand real-world system design patterns