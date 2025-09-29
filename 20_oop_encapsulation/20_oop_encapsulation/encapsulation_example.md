# Python Encapsulation: Underscore Conventions

In Python, underscores have different conventional meanings:

## No underscore (`public`)
```python
self.attribute = value
```
- Fully public, intended for external use
- No access restrictions

## Single underscore (`_protected`)
```python
self._attribute = value
```
- **Convention only** - indicates "internal use"
- Still accessible from outside: `obj._attribute`
- Meant for subclasses and internal implementation
- Not imported with `from module import *`

## Double underscore (`__private`)
```python
self.__attribute = value
```
- **Name mangling** - Python changes the name to `_ClassName__attribute`
- Harder to access from outside (but still possible)
- Prevents accidental access and inheritance conflicts

## Example:
```python
class Base:
    def __init__(self):
        self.public = "anyone can use"
        self._protected = "subclasses should use"
        self.__private = "only this class should use"

class Child(Base):
    def test(self):
        print(self.public)     # ✓ Works
        print(self._protected) # ✓ Works (intended)
        print(self.__private)  # ✗ AttributeError

obj = Child()
print(obj.public)           # ✓ Works
print(obj._protected)       # ✓ Works (but shouldn't)
print(obj._Child__private)  # ✓ Works (name mangling)
```

## Key Point
Single underscore is just a convention - Python doesn't enforce it. Double underscore actually changes the attribute name.