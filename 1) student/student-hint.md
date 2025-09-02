# 💡 Hints for Person Class Exercise

## Class Structure
- Start with `class Person:`
- Don't forget the colon after the class name

## Constructor Tips
- The special method `__init__` runs when creating objects
- First parameter is always `self`
- Store the name: `self.name = parameter_name`

## Method Creation
- Methods look like functions but inside the class
- Always include `self` as first parameter
- Access stored data with `self.attribute_name`

## String Formatting
- Use f-strings: `f"Hello, my name is {self.name}"`
- Or use `.format()`: `"Hello, my name is {}".format(self.name)`

## Creating Objects
- Call the class like a function: `Person("Alice")`
- Each object is separate - they don't share data

## Printing Attributes
- Access attributes directly: `person.name`
- Or create a method to print formatted info

## Stuck? Try This Order:
1. Write the class header
2. Add the `__init__` method
3. Add the `say_hello` method
4. Create your three people
5. Test everything works