class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.fuel = 0

    def start_engine(self):
        print("Engine started!")

    def add_fuel(self, amount):
        self.fuel += amount
        print(f"Fuel: {self.fuel}")

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 1
            print(f"Fuel: {self.fuel}")


if __name__ == "__main__":
    car1 = Car("Toyota", "Camry")
    car1.start_engine()
    car1.add_fuel(10)
    car1.drive()
