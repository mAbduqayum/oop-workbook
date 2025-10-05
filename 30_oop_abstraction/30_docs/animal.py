from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def eat(self):
        return f"{self.name} is eating"


class Dog(Animal):
    def make_sound(self):
        return f"{self.name} says: Woof!"


class Bird(Animal):
    def make_sound(self):
        return f"{self.name} says: Tweet tweet!"

    def move(self):
        return f"{self.name} flies through the air"


dog = Dog("Buddy", 3)
bird = Bird("Tweety", 1)

print(dog.make_sound())
print(bird.move())
print(dog.eat())
