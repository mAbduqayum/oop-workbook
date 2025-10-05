"""
AGGREGATION EXAMPLE - "HAS-A" Relationship (Weak)

Aggregation demonstrates a weak "has-a" relationship where objects
are grouped together but maintain independent lifecycles.

Key Characteristics:
- Container "has-a" component (shared ownership)
- Components can exist independently of the container
- Loose coupling - components have their own lifecycle
- Components can be part of multiple containers
- Relationship can change at runtime
"""


# Independent classes that can exist on their own
class Student:
    """Student can exist independently of any university"""

    def __init__(self, student_id, name, major, gpa=3.0) -> None:
        self.student_id = student_id
        self.name = name
        self.major = major
        self.gpa = gpa
        self.universities = []  # Can attend multiple universities
        self.courses = []
        self.graduation_year = None

    def enroll_in_university(self, university):
        """Student can enroll in a university"""
        if university not in self.universities:
            self.universities.append(university)
            return f"{self.name} enrolled in {university.name}"
        return f"{self.name} already enrolled in {university.name}"

    def leave_university(self, university):
        """Student can leave a university but continues to exist"""
        if university in self.universities:
            self.universities.remove(university)
            return f"{self.name} left {university.name}"
        return f"{self.name} was not enrolled in {university.name}"

    def enroll_in_course(self, course):
        """Student can enroll in courses"""
        if course not in self.courses:
            self.courses.append(course)
            return f"{self.name} enrolled in {course.name}"
        return f"{self.name} already enrolled in {course.name}"

    def graduate(self, year):
        """Student graduates but continues to exist as alumni"""
        self.graduation_year = year
        return f"{self.name} graduated in {year}"

    def get_info(self):
        unis = [uni.name for uni in self.universities]
        courses = [course.name for course in self.courses]
        status = "Graduate" if self.graduation_year else "Current Student"
        return (
            f"Student: {self.name} (ID: {self.student_id})\n"
            f"Major: {self.major}, GPA: {self.gpa}\n"
            f"Status: {status}\n"
            f"Universities: {unis}\n"
            f"Courses: {courses}"
        )


class Professor:
    """Professor can exist independently and work at multiple universities"""

    def __init__(self, employee_id, name, department, specialization) -> None:
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.specialization = specialization
        self.universities = []  # Can work at multiple universities
        self.courses_teaching = []
        self.research_projects = []

    def join_university(self, university):
        """Professor can join a university"""
        if university not in self.universities:
            self.universities.append(university)
            return f"Prof. {self.name} joined {university.name}"
        return f"Prof. {self.name} already works at {university.name}"

    def leave_university(self, university):
        """Professor can leave but continues to exist"""
        if university in self.universities:
            self.universities.remove(university)
            return f"Prof. {self.name} left {university.name}"
        return f"Prof. {self.name} doesn't work at {university.name}"

    def teach_course(self, course):
        """Professor can teach courses"""
        if course not in self.courses_teaching:
            self.courses_teaching.append(course)
            return f"Prof. {self.name} now teaching {course.name}"
        return f"Prof. {self.name} already teaching {course.name}"

    def start_research(self, project_name):
        """Professor can start research projects"""
        if project_name not in self.research_projects:
            self.research_projects.append(project_name)
            return f"Prof. {self.name} started research: {project_name}"
        return f"Prof. {self.name} already researching: {project_name}"

    def get_info(self):
        unis = [uni.name for uni in self.universities]
        courses = [course.name for course in self.courses_teaching]
        return (
            f"Professor: {self.name} (ID: {self.employee_id})\n"
            f"Department: {self.department}\n"
            f"Specialization: {self.specialization}\n"
            f"Universities: {unis}\n"
            f"Teaching: {courses}\n"
            f"Research Projects: {self.research_projects}"
        )


class Course:
    """Course can exist independently and be offered by multiple universities"""

    def __init__(self, course_code, name, credits, description) -> None:
        self.course_code = course_code
        self.name = name
        self.credits = credits
        self.description = description
        self.universities = []  # Can be offered at multiple universities
        self.enrolled_students = []
        self.instructors = []

    def add_to_university(self, university):
        """Course can be added to university catalog"""
        if university not in self.universities:
            self.universities.append(university)
            return f"Course {self.name} added to {university.name}"
        return f"Course {self.name} already at {university.name}"

    def enroll_student(self, student):
        """Student can enroll in course"""
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            return f"{student.name} enrolled in {self.name}"
        return f"{student.name} already enrolled in {self.name}"

    def assign_instructor(self, professor):
        """Professor can be assigned to teach course"""
        if professor not in self.instructors:
            self.instructors.append(professor)
            return f"Prof. {professor.name} assigned to {self.name}"
        return f"Prof. {professor.name} already teaching {self.name}"

    def get_info(self):
        unis = [uni.name for uni in self.universities]
        students = [s.name for s in self.enrolled_students]
        instructors = [p.name for p in self.instructors]
        return (
            f"Course: {self.name} ({self.course_code})\n"
            f"Credits: {self.credits}\n"
            f"Offered at: {unis}\n"
            f"Students: {len(students)} enrolled\n"
            f"Instructors: {instructors}"
        )


class Department:
    """Department aggregates professors and courses"""

    def __init__(self, name, university) -> None:
        self.name = name
        self.university = university
        self.professors = []  # Aggregation - professors exist independently
        self.courses = []  # Aggregation - courses exist independently
        self.head = None

    def add_professor(self, professor):
        """Add existing professor to department"""
        if professor not in self.professors:
            self.professors.append(professor)
            return f"Prof. {professor.name} added to {self.name} department"
        return f"Prof. {professor.name} already in {self.name} department"

    def remove_professor(self, professor):
        """Remove professor from department (professor continues to exist)"""
        if professor in self.professors:
            self.professors.remove(professor)
            if self.head == professor:
                self.head = None
            return f"Prof. {professor.name} removed from {self.name} department"
        return f"Prof. {professor.name} not in {self.name} department"

    def add_course(self, course):
        """Add existing course to department"""
        if course not in self.courses:
            self.courses.append(course)
            return f"Course {course.name} added to {self.name} department"
        return f"Course {course.name} already in {self.name} department"

    def appoint_head(self, professor):
        """Appoint department head"""
        if professor in self.professors:
            self.head = professor
            return f"Prof. {professor.name} appointed as head of {self.name}"
        return f"Prof. {professor.name} must be in department first"

    def get_info(self):
        prof_names = [p.name for p in self.professors]
        course_names = [c.name for c in self.courses]
        head_name = self.head.name if self.head else "None"
        return (
            f"Department: {self.name}\n"
            f"University: {self.university.name}\n"
            f"Head: {head_name}\n"
            f"Professors: {prof_names}\n"
            f"Courses: {course_names}"
        )


# Container class that uses aggregation
class University:
    """
    University uses AGGREGATION - it HAS Students, Professors, Courses
    These exist independently and can be part of multiple universities
    or exist without any university affiliation.
    """

    def __init__(self, name, location, founded_year) -> None:
        self.name = name
        self.location = location
        self.founded_year = founded_year

        # AGGREGATION: University aggregates existing independent objects
        self.students = []  # Students exist independently
        self.professors = []  # Professors exist independently
        self.courses = []  # Courses exist independently
        self.departments = []  # Departments are part of university structure

        print(f"University established: {self.name} ({self.founded_year})")

    def enroll_student(self, student):
        """Enroll an existing student"""
        if student not in self.students:
            self.students.append(student)
            student.enroll_in_university(self)
            return f"{student.name} enrolled at {self.name}"
        return f"{student.name} already enrolled at {self.name}"

    def graduate_student(self, student, year):
        """Graduate a student (student still exists as alumni)"""
        if student in self.students:
            self.students.remove(student)
            student.graduate(year)
            student.leave_university(self)
            return f"{student.name} graduated from {self.name} in {year}"
        return f"{student.name} not enrolled at {self.name}"

    def hire_professor(self, professor):
        """Hire an existing professor"""
        if professor not in self.professors:
            self.professors.append(professor)
            professor.join_university(self)
            return f"Prof. {professor.name} hired at {self.name}"
        return f"Prof. {professor.name} already works at {self.name}"

    def dismiss_professor(self, professor):
        """Dismiss a professor (professor continues to exist)"""
        if professor in self.professors:
            self.professors.remove(professor)
            professor.leave_university(self)
            return f"Prof. {professor.name} left {self.name}"
        return f"Prof. {professor.name} doesn't work at {self.name}"

    def offer_course(self, course):
        """Add existing course to university catalog"""
        if course not in self.courses:
            self.courses.append(course)
            course.add_to_university(self)
            return f"Course {course.name} now offered at {self.name}"
        return f"Course {course.name} already offered at {self.name}"

    def create_department(self, name):
        """Create a new department (composition within university)"""
        department = Department(name, self)
        self.departments.append(department)
        return f"{name} department created at {self.name}"

    def get_statistics(self):
        """Get university statistics"""
        return (
            f"\n{self.name} Statistics:\n"
            f"Location: {self.location}\n"
            f"Founded: {self.founded_year}\n"
            f"Students: {len(self.students)}\n"
            f"Professors: {len(self.professors)}\n"
            f"Courses: {len(self.courses)}\n"
            f"Departments: {len(self.departments)}"
        )

    def get_detailed_info(self):
        """Get detailed information about all aggregated objects"""
        info = f"\n{self.name} Detailed Information:"
        info += f"\n{'=' * 50}"

        if self.students:
            info += f"\nSTUDENTS ({len(self.students)}):"
            for student in self.students[:3]:  # Show first 3
                info += f"\n- {student.name} ({student.major})"

        if self.professors:
            info += f"\nPROFESSORS ({len(self.professors)}):"
            for prof in self.professors[:3]:  # Show first 3
                info += f"\n- {prof.name} ({prof.department})"

        if self.courses:
            info += f"\nCOURSES ({len(self.courses)}):"
            for course in self.courses[:3]:  # Show first 3
                info += f"\n- {course.name} ({course.credits} credits)"

        return info

    def __del__(self) -> None:
        """When university closes, aggregated objects continue to exist"""
        print(f"University closed: {self.name}")
        print("Students, professors, and courses continue to exist independently.")


# Demonstration of Aggregation
def demonstrate_aggregation():
    """Demonstrate aggregation concepts with examples"""

    print("=" * 60)
    print("AGGREGATION DEMONSTRATION - 'HAS-A' Relationship (Weak)")
    print("=" * 60)

    # Create independent objects first (they exist before being aggregated)
    print("\n1. INDEPENDENT OBJECT CREATION:")
    print("-" * 50)
    alice = Student("S001", "Alice Johnson", "Computer Science", 3.8)
    bob = Student("S002", "Bob Smith", "Mathematics", 3.6)
    charlie = Student("S003", "Charlie Brown", "Physics", 3.9)

    prof_davis = Professor("P001", "Dr. Davis", "Computer Science", "Machine Learning")
    prof_wilson = Professor("P002", "Dr. Wilson", "Mathematics", "Statistics")

    cs101 = Course(
        "CS101", "Introduction to Programming", 3, "Basic programming concepts"
    )
    math201 = Course("MATH201", "Calculus II", 4, "Advanced calculus")

    print("   Students, professors, and courses created independently")
    print("   They exist without any university affiliation")

    # Create universities and aggregate existing objects
    print("\n2. UNIVERSITY CREATION AND AGGREGATION:")
    print("-" * 50)
    tech_university = University("Tech University", "Silicon Valley", 1965)
    state_college = University("State College", "Downtown", 1890)

    # Aggregate existing objects
    print(f"   {tech_university.enroll_student(alice)}")
    print(f"   {tech_university.enroll_student(bob)}")
    print(f"   {tech_university.hire_professor(prof_davis)}")
    print(f"   {tech_university.offer_course(cs101)}")

    print(f"   {state_college.enroll_student(charlie)}")
    print(f"   {state_college.hire_professor(prof_wilson)}")
    print(f"   {state_college.offer_course(math201)}")

    print("\n3. SHARED OWNERSHIP - Objects can belong to multiple containers:")
    print("-" * 50)
    # Bob transfers to State College (shared between universities temporarily)
    print(f"   {state_college.enroll_student(bob)}")
    print(f"   Bob is now enrolled at both universities!")

    # Professor can work at multiple universities
    print(f"   {state_college.hire_professor(prof_davis)}")
    print(f"   Dr. Davis now works at both universities!")

    # Course can be offered at multiple universities
    print(f"   {state_college.offer_course(cs101)}")
    print(f"   CS101 is now offered at both universities!")

    print("\n4. INDEPENDENT LIFECYCLE - Objects exist independently:")
    print("-" * 50)
    print("   Before university closure:")
    print(tech_university.get_statistics())

    # University closes but objects continue to exist
    print("\n   Tech University closes...")
    del tech_university

    print(f"\n   Alice still exists: {alice.name} (GPA: {alice.gpa})")
    print(f"   Prof. Davis still exists: {prof_davis.name}")
    print(f"   CS101 course still exists: {cs101.name}")
    print("   All objects maintain their state and can join other universities")

    print("\n5. DYNAMIC RELATIONSHIPS - Objects can change affiliations:")
    print("-" * 50)
    new_university = University("Innovation Institute", "Research Park", 2020)
    print(f"   {new_university.enroll_student(alice)}")
    print(f"   {new_university.hire_professor(prof_davis)}")
    print(f"   Alice and Dr. Davis joined the new university")

    print("\n6. AGGREGATION IN ACTION - Course enrollment:")
    print("-" * 50)
    cs101.enroll_student(alice)
    cs101.assign_instructor(prof_davis)
    alice.enroll_in_course(cs101)
    prof_davis.teach_course(cs101)

    print("   Course enrollment demonstrates aggregation:")
    print(f"   - {cs101.get_info()}")

    print("\n" + "=" * 60)
    print("KEY AGGREGATION CONCEPTS DEMONSTRATED:")
    print("=" * 60)
    print("✓ HAS-A Relationship: University HAS Students, Professors, Courses")
    print("✓ Independent Lifecycle: Objects exist before and after aggregation")
    print("✓ Shared Ownership: Objects can belong to multiple containers")
    print("✓ Loose Coupling: Objects maintain their own state and behavior")
    print("✓ Dynamic Relationships: Affiliations can change at runtime")
    print("✓ Object Survival: Objects survive container destruction")


if __name__ == "__main__":
    demonstrate_aggregation()
