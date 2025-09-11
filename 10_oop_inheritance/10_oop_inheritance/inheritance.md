# Object-Oriented Programming: Inheritance

## What is Inheritance?

Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a class to inherit properties and methods from another class. Think of it like a family tree - children inherit traits from their parents, and grandchildren inherit traits from both parents and grandparents.

## Real-Life Analogy

Imagine you're designing a system for different types of vehicles:

- All vehicles have common properties: `brand`, `model`, `year`
- All vehicles can perform common actions: `start()`, `stop()`, `honk()`
- But each type of vehicle has specific features:
    - Cars have `doors` and can `open_trunk()`
    - Motorcycles have `engine_type` and can `pop_wheelie()`
    - Trucks have `cargo_capacity` and can `load_cargo()`

Instead of writing separate classes with duplicate code, inheritance lets us create a base `Vehicle` class and have specific vehicle types inherit from it.

## Basic Inheritance Syntax

```python
# Parent class (Base class / Superclass)
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        return f"{self.brand} {self.model} is starting..."
    
    def stop(self):
        return f"{self.brand} {self.model} has stopped."

# Child class (Derived class / Subclass)
class Car(Vehicle):  # Car inherits from Vehicle
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)  # Call parent constructor
        self.doors = doors
    
    def open_trunk(self):
        return f"Opening {self.brand} {self.model}'s trunk"

# Usage
my_car = Car("Toyota", "Camry", 2023, 4)
print(my_car.start())  # Inherited method
print(my_car.open_trunk())  # Car-specific method
```

## Types of Inheritance

### 1. Single Inheritance

One child class inherits from one parent class.

```python
# Real-life example: Animal hierarchy
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

class Dog(Animal):  # Single inheritance
    def __init__(self, name, breed):
        super().__init__(name, "Canine")
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball"

# Usage
buddy = Dog("Buddy", "Golden Retriever")
print(buddy.eat())    # Inherited from Animal
print(buddy.bark())   # Dog-specific method
```

### 2. Multiple Inheritance

One child class inherits from multiple parent classes.

```python
# Real-life example: Modern devices
class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
    
    def make_call(self, number):
        return f"Calling {number} from {self.phone_number}"
    
    def receive_call(self):
        return "Answering incoming call"

class Camera:
    def __init__(self, megapixels):
        self.megapixels = megapixels
    
    def take_photo(self):
        return f"Taking photo with {self.megapixels}MP camera"
    
    def record_video(self):
        return "Recording video"

class Computer:
    def __init__(self, processor):
        self.processor = processor
    
    def run_app(self, app_name):
        return f"Running {app_name} on {self.processor} processor"

# Multiple inheritance
class Smartphone(Phone, Camera, Computer):
    def __init__(self, phone_number, megapixels, processor, brand):
        Phone.__init__(self, phone_number)
        Camera.__init__(self, megapixels)
        Computer.__init__(self, processor)
        self.brand = brand
    
    def multitask(self):
        return f"{self.brand} smartphone multitasking"

# Usage
iphone = Smartphone("555-1234", 48, "A17 Pro", "iPhone")
print(iphone.make_call("555-5678"))  # From Phone
print(iphone.take_photo())           # From Camera
print(iphone.run_app("Instagram"))   # From Computer
print(iphone.multitask())            # Smartphone-specific
```

### 3. Multilevel Inheritance

A chain of inheritance where a class inherits from another class, which itself inherits from another class.

```python
# Real-life example: Academic hierarchy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"

class Student(Person):  # Student inherits from Person
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []
    
    def enroll(self, course):
        self.courses.append(course)
        return f"{self.name} enrolled in {course}"

class GraduateStudent(Student):  # GraduateStudent inherits from Student
    def __init__(self, name, age, student_id, research_area):
        super().__init__(name, age, student_id)
        self.research_area = research_area
        self.thesis_topic = None
    
    def choose_thesis(self, topic):
        self.thesis_topic = topic
        return f"{self.name} chose thesis topic: {topic}"
    
    def publish_paper(self, title):
        return f"{self.name} published: {title}"

# Usage
grad_student = GraduateStudent("Alice", 25, "GS001", "Machine Learning")
print(grad_student.introduce())        # From Person
print(grad_student.enroll("Deep Learning"))  # From Student
print(grad_student.choose_thesis("Neural Networks"))  # GraduateStudent-specific
```

### 4. Hierarchical Inheritance

Multiple child classes inherit from the same parent class.

```python
# Real-life example: Employee types in a company
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def work(self):
        return f"{self.name} is working"
    
    def get_salary(self):
        return f"{self.name}'s salary: ${self.salary}"

class Developer(Employee):  # Inherits from Employee
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language
    
    def code(self):
        return f"{self.name} is coding in {self.programming_language}"
    
    def debug(self):
        return f"{self.name} is debugging code"

class Designer(Employee):  # Also inherits from Employee
    def __init__(self, name, employee_id, salary, design_tool):
        super().__init__(name, employee_id, salary)
        self.design_tool = design_tool
    
    def design(self):
        return f"{self.name} is designing using {self.design_tool}"
    
    def create_mockup(self):
        return f"{self.name} created a new mockup"

class Manager(Employee):  # Also inherits from Employee
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size
    
    def manage_team(self):
        return f"{self.name} is managing a team of {self.team_size}"
    
    def schedule_meeting(self, topic):
        return f"{self.name} scheduled meeting about {topic}"

# Usage
dev = Developer("John", "DEV001", 75000, "Python")
designer = Designer("Sarah", "DES001", 65000, "Figma")
manager = Manager("Mike", "MGR001", 85000, 8)

print(dev.work())              # Inherited from Employee
print(dev.code())              # Developer-specific
print(designer.design())       # Designer-specific
print(manager.manage_team())   # Manager-specific
```

### 5. Hybrid Inheritance

A combination of multiple inheritance types.

```python
# Real-life example: Academic and administrative roles
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary
    
    def get_payroll(self):
        return f"Employee {self.employee_id}: ${self.salary}"

class Teacher(Person, Employee):  # Multiple inheritance
    def __init__(self, name, age, employee_id, salary, subject):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, salary)
        self.subject = subject
    
    def teach(self):
        return f"{self.name} is teaching {self.subject}"

class Principal(Teacher):  # Multilevel inheritance
    def __init__(self, name, age, employee_id, salary, subject, school_name):
        super().__init__(name, age, employee_id, salary, subject)
        self.school_name = school_name
    
    def manage_school(self):
        return f"{self.name} is managing {self.school_name}"

# Usage
principal = Principal("Dr. Smith", 45, "EMP123", 90000, "Mathematics", "Lincoln High")
print(principal.teach())         # From Teacher
print(principal.get_payroll())   # From Employee
print(principal.manage_school()) # Principal-specific
```

## Key Concepts

### Method Overriding

Child classes can override parent methods to provide specific implementations.

```python
class Animal:
    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def make_sound(self):  # Override parent method
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):  # Override parent method
        return "Meow! Meow!"

# Usage
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.make_sound())
# Output:
# Woof! Woof!
# Meow! Meow!
# Some generic animal sound
```

### super() Function

The `super()` function allows you to call methods from the parent class.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # Call parent constructor
        self.side = side
    
    def diagonal(self):
        return (self.side * 2) ** 0.5

# Usage
square = Square(5)
print(f"Area: {square.area()}")        # Inherited method
print(f"Perimeter: {square.perimeter()}")  # Inherited method
print(f"Diagonal: {square.diagonal()}")    # Square-specific method
```

## Benefits of Inheritance

1. **Code Reusability**: Write common code once in the parent class
2. **Maintainability**: Changes to common functionality only need to be made in one place
3. **Extensibility**: Easy to add new types without modifying existing code
4. **Polymorphism**: Different objects can be treated uniformly through their common interface

## Best Practices

1. **Use inheritance for "is-a" relationships**: A car "is-a" vehicle, a dog "is-an" animal
2. **Keep inheritance hierarchies shallow**: Avoid deep inheritance chains
3. **Use composition for "has-a" relationships**: A car "has-a" engine (don't inherit from engine)
4. **Override methods meaningfully**: Only override when you need different behavior
5. **Use super() when calling parent methods**: Maintains the inheritance chain properly

## Common Pitfalls

1. **Diamond Problem**: In multiple inheritance, be careful about method resolution order
2. **Tight Coupling**: Don't create overly dependent relationships between classes
3. **Inappropriate Inheritance**: Not every relationship should use inheritance
4. **Deep Hierarchies**: Too many levels make code hard to understand and maintain

## Practice Exercise

Try creating an inheritance hierarchy for a library system:
- Base class: `LibraryItem` (title, author, item_id)
- Derived classes: `Book`, `Magazine`, `DVD`
- Each should have specific properties and methods
- Implement method overriding for a `get_info()` method

Remember: Inheritance is a powerful tool, but use it wisely. Always ask yourself: "Does this relationship make sense? Is there a simpler way to achieve this?"
