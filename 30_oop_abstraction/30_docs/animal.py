from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class - cannot be instantiated directly"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        """Every animal MUST implement this"""
        pass

    @abstractmethod
    def move(self):
        """Every animal MUST implement this"""
        pass

    def eat(self):
        """Concrete method - inherited by all"""
        return f"{self.name} is eating"


class Dog(Animal):
    def make_sound(self):
        return f"{self.name} says: Woof!"

    # def move(self):
    #     return f"{self.name} runs on four legs"


class Bird(Animal):
    def make_sound(self):
        return f"{self.name} says: Tweet tweet!"

    def move(self):
        return f"{self.name} flies through the air"


# Cannot instantiate abstract class
# animal = Animal("Generic", 5)  # TypeError!

# But concrete classes work fine
dog = Dog("Buddy", 3)
bird = Bird("Tweety", 1)

print(dog.make_sound())   # Buddy says: Woof!
print(bird.move())        # Tweety flies through the air
print(dog.eat())          # Buddy is eating (inherited)
