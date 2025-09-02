# 💡 Hints for Animal Class Exercise

## Class with Multiple Attributes
- Your `__init__` method needs TWO parameters (plus self)
- Store both: `self.name = name` and `self.species = species`

## Constructor Example Structure
```python
def __init__(self, first_param, second_param):
    self.attribute1 = first_param
    self.attribute2 = second_param
```

## Method Using Attributes
- The `make_sound()` method should use `self.name`
- Format string: `f"{self.name} makes a sound!"`

## Creating Objects with Multiple Arguments
- Pass both values: `Animal("Buddy", "Dog")`
- Order matters - name first, then species

## Printing Multiple Attributes
- Access each attribute: `animal.name`, `animal.species`
- Format: `f"Name: {animal.name}, Species: {animal.species}"`

## Your Three Animals
- Dog: name="Buddy", species="Dog"
- Cat: name="Whiskers", species="Cat"  
- Bird: name="Tweety", species="Bird"

## Step-by-Step Approach
1. Define class with `__init__` taking name and species
2. Add `make_sound()` method
3. Create three animal objects
4. Print their info
5. Make them all make sounds