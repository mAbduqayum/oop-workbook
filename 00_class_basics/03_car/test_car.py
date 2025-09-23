from car import Car


class TestCar:
    def test_car_creation(self):
        car = Car("Toyota", "Camry")
        assert car.brand == "Toyota"
        assert car.model == "Camry"
        assert car.fuel == 0

    def test_add_fuel(self):
        car = Car("Honda", "Civic")
        car.add_fuel(10)
        assert car.fuel == 10

    def test_drive_with_fuel(self):
        car = Car("Ford", "Focus")
        car.add_fuel(5)
        car.drive()
        assert car.fuel == 4

    def test_drive_without_fuel(self):
        car = Car("BMW", "X3")
        car.drive()
        assert car.fuel == 0
