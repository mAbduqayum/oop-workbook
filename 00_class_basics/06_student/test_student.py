from student import Student


class TestStudent:
    def test_student_creation(self):
        student = Student("Alice", "S123")
        assert student.name == "Alice"
        assert student.student_id == "S123"
        assert student.grades == []

    def test_add_grade(self):
        student = Student("Bob", "S456")
        student.add_grade(85)
        assert student.grades == [85]

    def test_calculate_average(self):
        student = Student("Charlie", "S789")
        student.add_grade(85)
        student.add_grade(92)
        student.add_grade(78)
        assert student.calculate_average() == 85.0

    def test_calculate_average_empty(self):
        student = Student("Dave", "S012")
        assert student.calculate_average() == 0
