# 📘 OOP Dictionary

This dictionary will be updated **every week** with new terms.  

---

## 📅 Week 1 – Basic Terms

| Term | Definition | Example |
|------|------------|---------|
| **Class** | A blueprint or template for creating objects. | `class Student:` |
| **Object** | An instance of a class. | `s1 = Student()` |
| **Attribute (Property, Field)** | Variables that belong to a class/object. | `self.name`, `self.age` |
| **Method** | Functions that belong to a class/object. | `def introduce(self):` |
| **Constructor** | A special method used to initialize objects. | `__init__(self, name)` |
| **Instance** | A concrete object created from a class. | `car = Car("BMW")` |

---

## 📅 Week 2 – Core OOP Principles

| Term | Definition | Example |
|------|------------|---------|
| **Encapsulation** | Hiding internal details of an object and exposing only necessary parts. | Using private variables like `_name` and providing `get_name()` |
| **Inheritance** | A class can reuse and extend another class. | `class Dog(Animal):` |
| **Composition** | A “has-a” relationship; strong dependency — a whole is built from parts and may manage their lifecycle. | `class Car: def __init__(self): self.engine = Engine()` |
| **Aggregation** | A weaker “has-a” relationship; parts can exist independently of the whole. | `class Team: def __init__(self, players): self.players = players` |

---

## 📅 Week 3 – Encapsulation

| Term | Definition | Example |
|------|------------|---------|
| **Private Attribute** | An attribute intended for internal use only. | `self.__balance` |
| **Getter** | A method that returns the value of a private attribute. | `def get_balance(self): return self.__balance` |
| **Setter** | A method that modifies the value of a private attribute safely. | `def set_balance(self, amount): self.__balance = amount` |
| **Name Mangling** | A mechanism to make private attributes less accessible. | `obj._ClassName__balance` |

---

## 📅 Week 4 – Inheritance

| Term | Definition | Example |
|------|------------|---------|
| **Parent Class (Base Class)** | The class being inherited from. | `class Animal:` |
| **Child Class (Subclass)** | The class that inherits from another class. | `class Dog(Animal):` |
| **Method Overriding** | Redefining a parent method in a child class. | `def speak(self): return "Woof"` |
| **super()** | Calls the parent class method or constructor. | `super().__init__(name)` |

---

## 📅 Week 5 – Abstraction

| Term | Definition | Example |
|------|------------|---------|
| **Abstraction** | Hiding complex implementation details and showing only the necessary features. | `from abc import ABC, abstractmethod` |
| **Abstract Class** | A class that cannot be instantiated directly. | `class Shape(ABC):` |
| **Abstract Method** | A method declared but not implemented in an abstract class. | `@abstractmethod def area(self): pass` |
| **Interface** | A contract that defines methods without implementation. | `class Drawable(ABC): @abstractmethod def draw(self): pass` |

---

## 📅 Week 6 – Polymorphism

| Term | Definition | Example |
|------|------------|---------|
| **Polymorphism** | The ability of different objects to respond to the same method call in different ways. | `for animal in animals: animal.speak()` |
| **Duck Typing** | Behavior depends on methods, not class type. | `if it quacks like a duck...` |
| **Method Overloading (Pseudo)** | Defining multiple versions of a method (emulated in Python using default arguments). | `def add(a, b=0): return a + b` |
| **Method Overriding** | Changing a method’s behavior in a subclass. | `class Dog(Animal): def speak(self): return "Woof"` |

---

## 📅 Week 7 – Operator Overloading / Generics

| Term | Definition | Example |
|------|------------|---------|
| **Operator Overloading** | Redefining how operators work for custom classes. | `def __add__(self, other): return self.value + other.value` |
| **Magic Methods (Dunder Methods)** | Special methods that start and end with `__`. | `__str__`, `__len__`, `__eq__` |
| **Generics** | Writing flexible, reusable code for multiple data types. | `from typing import TypeVar, Generic` |
| **TypeVar** | A type placeholder in generic programming. | `T = TypeVar('T')` |

---

