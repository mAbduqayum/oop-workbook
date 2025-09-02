# 💡 Hints for Employee Inheritance Exercise

## Understanding Inheritance
- Inheritance means one class gets features from another class
- Child classes "inherit" attributes and methods from parent classes
- Use parentheses to show inheritance: `class Manager(Employee):`

## Creating the Base Class
- Start with `Employee` class like any normal class
- Add `__init__` with name, salary, department parameters
- Create `get_info()` and `get_annual_bonus()` methods
- This will be your "parent" or "base" class

## Inheritance Syntax
```python
class ChildClass(ParentClass):
    # Child class code here
```
- Put parent class name in parentheses
- Child automatically gets all parent methods and attributes

## Method Overriding
- Child classes can have their own version of parent methods
- Just define the same method name in the child class
- Python will use the child's version instead of the parent's

## Child Class Construction
- Child classes inherit the parent's `__init__` automatically
- If you don't write `__init__` in child, parent's `__init__` is used
- For this exercise, you DON'T need to write `__init__` in Manager/Developer

## Adding New Methods
- Child classes can have methods the parent doesn't have
- `Manager` gets `manage_team()`, `Developer` gets `code_review()`
- Only objects of that type can use these methods

## Testing Inheritance
- Create objects: `manager = Manager("Sarah", 80000, "Engineering")`
- Manager object has ALL Employee methods PLUS its own methods
- Call inherited methods: `manager.get_info()` (from Employee)
- Call overridden methods: `manager.get_annual_bonus()` (Manager's version)
- Call new methods: `manager.manage_team()` (only Manager has this)

## Method Override Examples
```python
# In Employee class
def get_annual_bonus(self):
    return self.salary * 0.1

# In Manager class  
def get_annual_bonus(self):
    return self.salary * 0.2  # Different calculation!
```

## Step-by-Step Approach
1. Write complete `Employee` class first
2. Test it works by creating an employee object
3. Create `Manager` class with inheritance syntax
4. Override the bonus method
5. Add manage_team method
6. Test manager object
7. Repeat for `Developer` class
8. Create all three types and test their methods

## Common Inheritance Gotchas
- Don't forget parentheses in class definition: `class Manager(Employee):`
- Child classes automatically inherit parent `__init__` - don't rewrite it
- Method names must match exactly to override (spelling matters!)
- Each class type has access to different methods