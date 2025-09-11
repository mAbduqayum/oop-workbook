# Exercise: Animal Hierarchy

Create a simple animal classification system using inheritance, following the pattern from the inheritance guide.

## Requirements

Design a basic inheritance hierarchy for animals:

### Base Class: `Animal`
- **Attributes:**
  - `name` (string): Animal's name
  - `species` (string): Animal species

- **Methods:**
  - `__init__(name, species)`: Constructor
  - `eat()`: Eating behavior
  - `sleep()`: Sleeping behavior
  - `move()`: Movement behavior (to be overridden)
  - `make_sound()`: Animal sound (to be overridden)

### Derived Classes

#### `Dog` (inherits from Animal)
- **Additional Attributes:**
  - `breed` (string): Dog breed

- **Override Methods:**
  - `make_sound()`: Return "Woof! Woof!"
  - `move()`: Return "Running on four legs"
- **Additional Methods:**
  - `bark()`: Dog barking behavior
  - `fetch()`: Playing fetch
  - `wag_tail()`: Tail wagging behavior

#### `Cat` (inherits from Animal)
- **Additional Attributes:**
  - `coat_color` (string): Fur color

- **Override Methods:**
  - `make_sound()`: Return "Meow! Meow!"
  - `move()`: Return "Stalking silently"
- **Additional Methods:**
  - `meow()`: Cat meowing behavior
  - `purr()`: Purring behavior
  - `climb()`: Climbing behavior

#### `Bird` (inherits from Animal)
- **Additional Attributes:**
  - `wingspan` (float): Wing span in meters

- **Override Methods:**
  - `make_sound()`: Return "Tweet! Tweet!"
  - `move()`: Return "Flying with wings"
- **Additional Methods:**
  - `fly()`: Flying behavior
  - `sing()`: Singing behavior
  - `build_nest()`: Nest building behavior

## Example Usage

```python
# Create different animals
dog = Dog("Buddy", "Golden Retriever", "Golden Retriever")
cat = Cat("Whiskers", "Domestic Cat", "Orange")
bird = Bird("Tweety", "Canary", 0.15)

# Display basic information
print(f"Dog: {dog.name} ({dog.species})")
print(f"Breed: {dog.breed}")
print(f"Sound: {dog.make_sound()}")
print(f"Movement: {dog.move()}")
dog.bark()
dog.fetch()

print(f"\nCat: {cat.name} ({cat.species})")
print(f"Color: {cat.coat_color}")
print(f"Sound: {cat.make_sound()}")
print(f"Movement: {cat.move()}")
cat.purr()
cat.climb()

print(f"\nBird: {bird.name} ({bird.species})")
print(f"Wingspan: {bird.wingspan}m")
print(f"Sound: {bird.make_sound()}")
print(f"Movement: {bird.move()}")
bird.fly()
bird.sing()

# Demonstrate polymorphism
animals = [dog, cat, bird]
print("\nAll animals making sounds:")
for animal in animals:
    print(f"{animal.name}: {animal.make_sound()}")

print("\nAll animals moving:")
for animal in animals:
    print(f"{animal.name}: {animal.move()}")
```

## Expected Output

```
Dog: Buddy (Golden Retriever)
Breed: Golden Retriever
Sound: Woof! Woof!
Movement: Running on four legs
Buddy is barking loudly!
Buddy is fetching the ball!

Cat: Whiskers (Domestic Cat)
Color: Orange
Sound: Meow! Meow!
Movement: Stalking silently
Whiskers is purring contentedly
Whiskers is climbing up the tree

Bird: Tweety (Canary)
Wingspan: 0.15m
Sound: Tweet! Tweet!
Movement: Flying with wings
Tweety is flying gracefully
Tweety is singing a beautiful song

All animals making sounds:
Buddy: Woof! Woof!
Whiskers: Meow! Meow!
Tweety: Tweet! Tweet!

All animals moving:
Buddy: Running on four legs
Whiskers: Stalking silently
Tweety: Flying with wings
```

## Learning Objectives

- Practice basic inheritance with simple hierarchies
- Learn to override methods in child classes
- Understand polymorphism with different animal types
- Work with class-specific attributes and methods
- Create meaningful "is-a" relationships
- Implement method overriding for different behaviors
- Use inheritance to reduce code duplication