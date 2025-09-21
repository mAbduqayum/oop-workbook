import unittest

from triangle import Triangle


class TestTriangle(unittest.TestCase):
    def test_valid_triangle_creation(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.a, 3)
        self.assertEqual(triangle.b, 4)
        self.assertEqual(triangle.c, 5)

    def test_invalid_triangle_creation(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 5)

    def test_calculate_perimeter(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.calculate_perimeter(), 12)

    def test_calculate_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.calculate_area(), 6.0)

    def test_get_type_scalene(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.get_type(), "scalene")

    def test_get_type_isosceles(self):
        triangle = Triangle(5, 5, 8)
        self.assertEqual(triangle.get_type(), "isosceles")

    def test_get_type_equilateral(self):
        triangle = Triangle(5, 5, 5)
        self.assertEqual(triangle.get_type(), "equilateral")

    def test_get_angle_type_right(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.get_angle_type(), "right")

    def test_scale(self):
        triangle = Triangle(3, 4, 5)
        scaled = triangle.scale(2)
        self.assertEqual(scaled.a, 6)
        self.assertEqual(scaled.b, 8)
        self.assertEqual(scaled.c, 10)

    def test_is_similar(self):
        triangle1 = Triangle(3, 4, 5)
        triangle2 = triangle1.scale(2)
        self.assertTrue(triangle1.is_similar(triangle2))


if __name__ == "__main__":
    unittest.main()
