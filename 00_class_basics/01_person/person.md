# 🐍 Python OOP Practice - Lesson 1: Person Class

## 📝 Exercise: Create a Person Class System

Create a complete `Person` class that demonstrates the fundamentals of Object-Oriented Programming.

**Your Task:**
1. Create a `Person` class with a `name` attribute
2. Add a `say_hello()` method that prints "Hello, my name is [name]"
3. Create 3 different `Person` objects with different names
4. Make each person say hello to demonstrate they're independent objects

**What You'll Learn:**
- Basic class syntax and `__init__` constructor
- Instance methods and the `self` parameter
- Creating multiple objects from the same class
- How each object maintains its own data

**Example Usage:**
```python
# Create three different Person objects
person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person("Charlie")

# Make each person say hello
person1.say_hello()  # Hello, my name is Alice
person2.say_hello()  # Hello, my name is Bob
person3.say_hello()  # Hello, my name is Charlie
```

**Success Criteria:**
- ✅ Class defined with proper syntax
- ✅ Constructor takes and stores name
- ✅ Method uses self to access attributes
- ✅ Three different objects created and working independently
