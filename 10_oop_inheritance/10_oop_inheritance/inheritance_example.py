"""
INHERITANCE EXAMPLE - "IS-A" Relationship

Inheritance demonstrates an "is-a" relationship where a child class
inherits properties and methods from a parent class.

Key Characteristics:
- Child "is-a" type of parent
- Shared lifecycle (child cannot exist without being a parent type)
- Method overriding possible
- Tight coupling between parent and child
- Polymorphism support
"""

# Parent class (Base class)
class Animal:
    """Base class representing a generic animal"""

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def make_sound(self):
        return f"{self.name} makes a sound."

    def move(self):
        return f"{self.name} is moving."

    def get_info(self):
        return f"Name: {self.name}, Species: {self.species}"


# Child classes (Derived classes)
class Dog(Animal):
    """Dog IS-A Animal"""

    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, "Canine")
        self.breed = breed
        self.loyalty = 100

    # Override parent method
    def make_sound(self):
        return f"{self.name} barks: Woof! Woof!"

    # Override parent method
    def move(self):
        return f"{self.name} runs on four legs."

    # Add dog-specific behavior
    def fetch(self):
        return f"{self.name} fetches the ball!"

    def wag_tail(self):
        return f"{self.name} is wagging tail happily!"

    def get_info(self):
        # Extend parent method
        base_info = super().get_info()
        return f"{base_info}, Breed: {self.breed}"


class Cat(Animal):
    """Cat IS-A Animal"""

    def __init__(self, name, coat_color):
        super().__init__(name, "Feline")
        self.coat_color = coat_color
        self.independence = 95

    # Override parent method
    def make_sound(self):
        return f"{self.name} meows: Meow! Meow!"

    # Override parent method
    def move(self):
        return f"{self.name} moves gracefully and silently."

    # Add cat-specific behavior
    def purr(self):
        return f"{self.name} is purring contentedly."

    def climb(self):
        return f"{self.name} climbs up the tree."

    def hunt(self):
        return f"{self.name} is hunting mice."

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Coat Color: {self.coat_color}"


class Bird(Animal):
    """Bird IS-A Animal"""

    def __init__(self, name, wingspan):
        super().__init__(name, "Avian")
        self.wingspan = wingspan
        self.can_fly = True

    # Override parent method
    def make_sound(self):
        return f"{self.name} chirps: Tweet! Tweet!"

    # Override parent method
    def move(self):
        if self.can_fly:
            return f"{self.name} flies through the sky."
        else:
            return f"{self.name} hops on the ground."

    # Add bird-specific behavior
    def fly(self):
        if self.can_fly:
            return f"{self.name} soars with {self.wingspan}cm wingspan!"
        else:
            return f"{self.name} cannot fly."

    def build_nest(self):
        return f"{self.name} is building a nest."

    def migrate(self):
        return f"{self.name} is migrating to warmer regions."

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Wingspan: {self.wingspan}cm"


# Demonstration of Inheritance
def demonstrate_inheritance():
    """Demonstrate inheritance concepts with examples"""

    print("=" * 60)
    print("INHERITANCE DEMONSTRATION - 'IS-A' Relationship")
    print("=" * 60)

    # Create instances of different animals
    animals = [
        Dog("Buddy", "Golden Retriever"),
        Cat("Whiskers", "Orange Tabby"),
        Bird("Robin", 25),
        Dog("Max", "German Shepherd"),
        Cat("Luna", "Black")
    ]

    print("\n1. POLYMORPHISM - Same method, different behavior:")
    print("-" * 50)
    for animal in animals:
        print(f"   {animal.make_sound()}")

    print("\n2. INHERITANCE - Child objects have parent methods:")
    print("-" * 50)
    for animal in animals:
        print(f"   {animal.eat()}")
        print(f"   {animal.move()}")
        print()

    print("3. METHOD OVERRIDING - Specialized behavior:")
    print("-" * 50)
    buddy = Dog("Buddy", "Golden Retriever")
    print(f"   Generic Animal sound: Would be 'makes a sound'")
    print(f"   Dog sound: {buddy.make_sound()}")
    print(f"   Dog-specific behavior: {buddy.fetch()}")
    print()

    whiskers = Cat("Whiskers", "Orange Tabby")
    print(f"   Cat sound: {whiskers.make_sound()}")
    print(f"   Cat-specific behavior: {whiskers.purr()}")
    print()

    robin = Bird("Robin", 25)
    print(f"   Bird sound: {robin.make_sound()}")
    print(f"   Bird-specific behavior: {robin.fly()}")
    print()

    print("4. ISINSTANCE - Type checking:")
    print("-" * 50)
    print(f"   buddy is Animal: {isinstance(buddy, Animal)}")
    print(f"   buddy is Dog: {isinstance(buddy, Dog)}")
    print(f"   buddy is Cat: {isinstance(buddy, Cat)}")
    print()

    print("5. SHARED PROPERTIES - Inherited from parent:")
    print("-" * 50)
    for animal in animals[:3]:
        print(f"   {animal.get_info()}")
        print(f"   Is alive: {animal.is_alive}")

    print("\n6. INHERITANCE HIERARCHY:")
    print("-" * 50)
    print("   Animal (Parent)")
    print("   ├── Dog (Child) - inherits eat(), sleep(), make_sound(), move()")
    print("   ├── Cat (Child) - inherits eat(), sleep(), make_sound(), move()")
    print("   └── Bird (Child) - inherits eat(), sleep(), make_sound(), move()")

    print("\n" + "=" * 60)
    print("KEY INHERITANCE CONCEPTS DEMONSTRATED:")
    print("=" * 60)
    print("✓ IS-A Relationship: Dog IS-A Animal, Cat IS-A Animal")
    print("✓ Method Overriding: Each animal makes different sounds")
    print("✓ Code Reuse: All animals inherit eat(), sleep() methods")
    print("✓ Polymorphism: Same interface, different implementations")
    print("✓ Shared Lifecycle: Cannot have Dog without Animal base")
    print("✓ Type Hierarchy: Clear parent-child relationships")


if __name__ == "__main__":
    demonstrate_inheritance()