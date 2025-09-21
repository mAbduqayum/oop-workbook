import unittest

from car import Car


class TestCar(unittest.TestCase):
    def test_car_creation(self):
        car = Car("Toyota", "Camry")
        self.assertEqual(car.brand, "Toyota")
        self.assertEqual(car.model, "Camry")
        self.assertEqual(car.fuel, 0)

    def test_add_fuel(self):
        car = Car("Honda", "Civic")
        car.add_fuel(10)
        self.assertEqual(car.fuel, 10)

    def test_drive_with_fuel(self):
        car = Car("Ford", "Focus")
        car.add_fuel(5)
        car.drive()
        self.assertEqual(car.fuel, 4)


if __name__ == "__main__":
    unittest.main()
