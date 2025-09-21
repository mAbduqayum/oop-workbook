"""
COMPOSITION EXAMPLE - "HAS-A" Relationship (Strong)

Composition demonstrates a strong "has-a" relationship where objects
are built by combining other objects as integral parts.

Key Characteristics:
- Container "has-a" component (exclusive ownership)
- Components cannot exist without the container
- Tight coupling - components are created and destroyed with container
- Container controls component lifecycle
- Components are integral parts of the whole
"""


# Component classes - these will be "composed" into larger objects
class Engine:
    """Engine component - cannot exist independently in this context"""

    def __init__(self, engine_type, horsepower, fuel_type) -> None:
        self.engine_type = engine_type
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.is_running = False
        self.temperature = 20  # Celsius

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.temperature = 90
            return f"{self.engine_type} engine started! ({self.horsepower} HP)"
        return f"Engine already running."

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.temperature = 20
            return f"Engine stopped and cooling down."
        return f"Engine already stopped."

    def accelerate(self):
        if self.is_running:
            return f"Engine revving! Power: {self.horsepower} HP"
        return f"Cannot accelerate - engine not running."

    def get_status(self):
        status = "Running" if self.is_running else "Stopped"
        return f"{self.engine_type} - {status} - Temp: {self.temperature}°C"


class Transmission:
    """Transmission component"""

    def __init__(self, transmission_type, num_gears) -> None:
        self.transmission_type = transmission_type
        self.num_gears = num_gears
        self.current_gear = 0  # 0 = Park, 1-6 = gears
        self.is_engaged = False

    def shift_gear(self, gear):
        if 0 <= gear <= self.num_gears:
            self.current_gear = gear
            self.is_engaged = gear > 0
            gear_name = "Park" if gear == 0 else f"Gear {gear}"
            return f"Shifted to {gear_name}"
        return f"Invalid gear! Available: 0-{self.num_gears}"

    def get_status(self):
        gear_name = "Park" if self.current_gear == 0 else f"Gear {self.current_gear}"
        return f"{self.transmission_type} - {gear_name}"


class Wheel:
    """Wheel component"""

    def __init__(self, size, tire_type) -> None:
        self.size = size  # in inches
        self.tire_type = tire_type
        self.pressure = 32  # PSI
        self.wear_level = 0  # 0-100%

    def rotate(self):
        self.wear_level += 0.1
        return f'{self.size}" wheel rotating'

    def brake(self):
        self.wear_level += 0.2
        return f'{self.size}" wheel braking'

    def check_pressure(self):
        if self.pressure < 25:
            return f"Low pressure: {self.pressure} PSI"
        elif self.pressure > 40:
            return f"High pressure: {self.pressure} PSI"
        else:
            return f"Normal pressure: {self.pressure} PSI"

    def get_status(self):
        return f'{self.size}" {self.tire_type} - {self.pressure} PSI - Wear: {self.wear_level:.1f}%'


class FuelTank:
    """Fuel tank component"""

    def __init__(self, capacity) -> None:
        self.capacity = capacity  # in liters
        self.current_fuel = capacity * 0.8  # Start with 80% fuel
        self.fuel_type = "Gasoline"

    def add_fuel(self, amount):
        if self.current_fuel + amount <= self.capacity:
            self.current_fuel += amount
            return f"Added {amount}L fuel. Total: {self.current_fuel}L"
        else:
            overflow = (self.current_fuel + amount) - self.capacity
            self.current_fuel = self.capacity
            return f"Tank full! Overflow: {overflow}L"

    def consume_fuel(self, amount):
        if self.current_fuel >= amount:
            self.current_fuel -= amount
            return f"Consumed {amount}L fuel. Remaining: {self.current_fuel}L"
        else:
            self.current_fuel = 0
            return f"Not enough fuel! Tank empty."

    def get_fuel_level(self):
        percentage = (self.current_fuel / self.capacity) * 100
        return f"Fuel: {self.current_fuel:.1f}L / {self.capacity}L ({percentage:.1f}%)"


# Container class that uses composition
class Car:
    """
    Car uses COMPOSITION - it HAS-A Engine, Transmission, Wheels, etc.
    The components are created when the car is created and destroyed when car is destroyed.
    Components cannot exist independently - they are integral parts of the car.
    """

    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.is_started = False

        # COMPOSITION: Car creates and owns these components
        # These components cannot exist without the car
        self.engine = Engine("V6", 300, "Gasoline")
        self.transmission = Transmission("Automatic", 6)
        self.fuel_tank = FuelTank(60)

        # Create 4 wheels
        self.wheels = [
            Wheel(17, "All-Season"),
            Wheel(17, "All-Season"),
            Wheel(17, "All-Season"),
            Wheel(17, "All-Season"),
        ]

        print(f"Car manufactured: {self.year} {self.make} {self.model}")
        print("Components created and integrated into the car.")

    def start_car(self):
        """Start the car - requires multiple components to work together"""
        if not self.is_started:
            if self.fuel_tank.current_fuel > 0:
                engine_msg = self.engine.start()
                trans_msg = self.transmission.shift_gear(1)
                self.is_started = True
                return f"Car started! {engine_msg} {trans_msg}"
            else:
                return "Cannot start - no fuel!"
        return "Car already started."

    def drive(self, distance_km):
        """Drive the car - demonstrates component interaction"""
        if not self.is_started:
            return "Cannot drive - car not started!"

        if self.fuel_tank.current_fuel <= 0:
            return "Cannot drive - no fuel!"

        # Calculate fuel consumption (simplified)
        fuel_needed = distance_km * 0.1  # 10L per 100km
        fuel_msg = self.fuel_tank.consume_fuel(fuel_needed)

        # Rotate wheels
        wheel_messages = [wheel.rotate() for wheel in self.wheels]

        # Accelerate engine
        engine_msg = self.engine.accelerate()

        return f"Drove {distance_km}km. {fuel_msg} {engine_msg}"

    def brake(self):
        """Brake the car - uses wheel components"""
        if self.is_started:
            brake_messages = [wheel.brake() for wheel in self.wheels]
            return f"Car braking! All wheels engaged."
        return "Car not running."

    def stop_car(self):
        """Stop the car"""
        if self.is_started:
            engine_msg = self.engine.stop()
            trans_msg = self.transmission.shift_gear(0)
            self.is_started = False
            return f"Car stopped. {engine_msg} {trans_msg}"
        return "Car already stopped."

    def get_status(self):
        """Get comprehensive car status - delegates to components"""
        status = f"\n{self.year} {self.make} {self.model} Status:"
        status += f"\nRunning: {self.is_started}"
        status += f"\nEngine: {self.engine.get_status()}"
        status += f"\nTransmission: {self.transmission.get_status()}"
        status += f"\nFuel: {self.fuel_tank.get_fuel_level()}"
        status += f"\nWheels:"
        for i, wheel in enumerate(self.wheels, 1):
            status += f"\n  Wheel {i}: {wheel.get_status()}"
        return status

    def maintenance_check(self):
        """Perform maintenance on all components"""
        results = []
        results.append(f"Engine: {self.engine.get_status()}")
        results.append(f"Transmission: {self.transmission.get_status()}")
        results.append(f"Fuel Tank: {self.fuel_tank.get_fuel_level()}")

        for i, wheel in enumerate(self.wheels, 1):
            results.append(f"Wheel {i}: {wheel.check_pressure()}")

        return "Maintenance Check:\n" + "\n".join(results)

    def __del__(self) -> None:
        """When car is destroyed, all components are destroyed too"""
        print(f"Car demolished: {self.year} {self.make} {self.model}")
        print(
            "All components (engine, transmission, wheels, fuel tank) destroyed with the car."
        )


# Demonstration of Composition
def demonstrate_composition():
    """Demonstrate composition concepts with examples"""

    print("=" * 60)
    print("COMPOSITION DEMONSTRATION - 'HAS-A' Relationship (Strong)")
    print("=" * 60)

    # Create a car - this creates all components automatically
    print("\n1. OBJECT CREATION - Components created with container:")
    print("-" * 50)
    my_car = Car("Toyota", "Camry", 2023)

    print("\n2. COMPONENT INTEGRATION - Components work together:")
    print("-" * 50)
    print(f"   {my_car.start_car()}")
    print(f"   {my_car.drive(50)}")
    print(f"   {my_car.brake()}")

    print("\n3. DELEGATED BEHAVIOR - Car delegates to components:")
    print("-" * 50)
    print(my_car.get_status())

    print("\n4. COMPONENT DEPENDENCY - Components need each other:")
    print("-" * 50)
    print(f"   Engine without fuel: {my_car.fuel_tank.consume_fuel(60)}")
    print(f"   Try to drive: {my_car.drive(10)}")

    print("\n5. MAINTENANCE - Operating on all components:")
    print("-" * 50)
    print(my_car.maintenance_check())

    print("\n6. LIFECYCLE DEPENDENCY:")
    print("-" * 50)
    print("   When car is destroyed, ALL components are destroyed too.")
    print("   Components cannot exist independently of the car.")

    # Create another car to show independent composition
    print("\n7. INDEPENDENT COMPOSITION:")
    print("-" * 50)
    another_car = Car("Honda", "Civic", 2024)
    print("   Each car has its own independent set of components.")

    print(f"\nCar 1 engine status: {my_car.engine.get_status()}")
    print(f"Car 2 engine status: {another_car.engine.get_status()}")

    # Stop cars
    print(f"\n   {my_car.stop_car()}")
    print(f"   {another_car.stop_car()}")

    print("\n" + "=" * 60)
    print("KEY COMPOSITION CONCEPTS DEMONSTRATED:")
    print("=" * 60)
    print("✓ HAS-A Relationship: Car HAS-A Engine, Transmission, Wheels")
    print("✓ Exclusive Ownership: Components belong only to one car")
    print("✓ Lifecycle Dependency: Components destroyed with car")
    print("✓ Tight Coupling: Components designed specifically for cars")
    print("✓ Delegation: Car delegates behavior to components")
    print("✓ Component Integration: Components work together as a system")


if __name__ == "__main__":
    demonstrate_composition()
