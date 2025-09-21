## Exercise: Animal Class

Create an `Animal` class that demonstrates the `__repr__` dunder method.

### Your Task:
1. Create an `Animal` class that takes `name` and `species` in the constructor
2. Add a `make_sound()` method that prints `f"{name} makes a sound!"`
3. Add a `__repr__()` method that returns `f"Animal(name='{name}', species='{species}')"`

### What You'll Learn:
- Working with multiple attributes in a single class
- Using the `__repr__` dunder method for object representation
- Creating methods that use multiple pieces of object data

### Example Usage:
```python
dog = Animal("Buddy", "Dog")
print(dog)          # Animal(name='Buddy', species='Dog')
dog.make_sound()    # Buddy makes a sound!
```

