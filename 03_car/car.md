# 🚗 Python OOP Practice - Lesson 3: Car Class

## 📝 Exercise: Build a Car Garage

Create a `Car` class that represents vehicles with properties and behaviors that can change. This introduces modifying object state.

**Your Complete Task:**
1. Create a `Car` class with `brand`, `model`, and `fuel` attributes (fuel starts at 0)
2. Add a `start_engine()` method that prints "[brand] [model] engine started!"
3. Add a `add_fuel(amount)` method that increases the fuel and prints "Added [amount] liters. Fuel now: [total]"
4. Add a `drive()` method that checks if fuel > 0, then reduces fuel by 1 and prints "Driving the [brand] [model]! Fuel remaining: [fuel]"
5. Create 2 different cars, add fuel to them, start engines, and drive them

**What You'll Learn:**
- Classes with multiple attributes including numbers
- Methods that modify object state
- Methods that take parameters
- Conditional logic in methods
- Object state changes over time

**Expected Output:**
```
Toyota Camry engine started!
Added 10 liters. Fuel now: 10
Driving the Toyota Camry! Fuel remaining: 9
Honda Civic engine started!
Added 5 liters. Fuel now: 5
Driving the Honda Civic! Fuel remaining: 4
```

**Success Criteria:**
- ✅ Car class with brand, model, and fuel attributes
- ✅ start_engine() method uses brand and model
- ✅ add_fuel() method modifies fuel attribute
- ✅ drive() method checks fuel and decreases it
- ✅ Two cars created and operated successfully