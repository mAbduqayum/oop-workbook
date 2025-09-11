# 🐾 Python OOP Practice - Lesson: Animal Class

## 📝 Exercise: Build an Animal Zoo

Create an `Animal` class system that can represent different animals in a zoo. Your class should handle multiple attributes and behaviors.

**Your Complete Task:**
1. Create an `Animal` class that takes `name` and `species` in the constructor
2. Add a `make_sound()` method that prints "[name] makes a sound!"
3. Create a mini zoo with 3 different animals (dog named "Buddy", cat named "Whiskers", bird named "Tweety")
4. Print each animal's name and species
5. Make each animal make their sound

**What You'll Learn:**
- Working with multiple attributes in a single class
- Creating methods that use multiple pieces of object data
- Managing multiple objects from the same class
- Understanding that each object stores its own unique data

**Example Usage:**
```python
# Create a mini zoo with 3 different animals
dog = Animal("Buddy", "Dog")
cat = Animal("Whiskers", "Cat")
bird = Animal("Tweety", "Bird")

# Print each animal's information
print(f"Name: {dog.name}, Species: {dog.species}")     # Name: Buddy, Species: Dog
print(f"Name: {cat.name}, Species: {cat.species}")     # Name: Whiskers, Species: Cat
print(f"Name: {bird.name}, Species: {bird.species}")   # Name: Tweety, Species: Bird

# Make each animal make their sound
dog.make_sound()   # Buddy makes a sound!
cat.make_sound()   # Whiskers makes a sound!
bird.make_sound()  # Tweety makes a sound!
```

**Success Criteria:**
- ✅ Animal class with name and species attributes
- ✅ make_sound() method uses the animal's name
- ✅ Three animals created with correct data
- ✅ All information printed as expected
