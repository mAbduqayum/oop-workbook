import unittest

from student import Student


class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        student = Student("Alice", "S123")
        self.assertEqual(student.name, "Alice")
        self.assertEqual(student.student_id, "S123")
        self.assertEqual(student.grades, [])

    def test_add_grade(self):
        student = Student("Bob", "S456")
        student.add_grade(85)
        self.assertEqual(student.grades, [85])

    def test_calculate_average(self):
        student = Student("Charlie", "S789")
        student.add_grade(85)
        student.add_grade(92)
        student.add_grade(78)
        self.assertEqual(student.calculate_average(), 85.0)

    def test_calculate_average_empty(self):
        student = Student("Dave", "S012")
        self.assertEqual(student.calculate_average(), 0)


if __name__ == "__main__":
    unittest.main()
