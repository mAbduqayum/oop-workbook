## Exercise: Car class

Create a `Car` class that represents vehicles with properties and behaviors that can change. This introduces modifying object state.

**Your Complete Task:**
1. Create a `Car` class with `brand`, `model`, and `fuel` attributes (fuel starts at 0)
2. Add a `start_engine()` method that prints `Engine started!`
3. Add a `add_fuel(amount)` method that increases the fuel and prints `f"Fuel: {total}"`
4. Add a `drive()` method that checks if fuel > 0, then reduces fuel by 1 and prints `f"Fuel: {fuel}"`

**Example Usage:**
```python
car1 = Car("Toyota", "Camry")
car1.start_engine()  # Engine started!
car1.add_fuel(10)    # Fuel: 10
car1.drive()         # Fuel: 9
```
