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

