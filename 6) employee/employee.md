# 👔 Python OOP Practice - Lesson 5: Employee Inheritance

## 📝 Exercise: Build a Company Employee System

Create an employee hierarchy using inheritance. This introduces class relationships where specialized classes inherit from a base class.

**Your Complete Task:**
1. Create a base `Employee` class with `name`, `salary`, and `department` attributes
2. Add a `get_info()` method that prints "Employee: [name], Department: [department], Salary: $[salary]"
3. Add a `get_annual_bonus()` method that returns `salary * 0.1` (10% bonus)
4. Create a `Manager` class that inherits from `Employee`
5. Override `get_annual_bonus()` in `Manager` to return `salary * 0.2` (20% bonus)
6. Add a `manage_team()` method to `Manager` that prints "[name] is managing the [department] team"
7. Create a `Developer` class that inherits from `Employee`
8. Override `get_annual_bonus()` in `Developer` to return `salary * 0.15` (15% bonus)
9. Add a `code_review()` method to `Developer` that prints "[name] is reviewing code"
10. Create one employee, one manager, and one developer. Show their info and bonuses

**What You'll Learn:**
- Inheritance: classes sharing common attributes and methods
- Method overriding: specialized behavior in subclasses
- The `super()` function for calling parent methods
- "Is-a" relationships (Manager IS-A Employee)
- Code reuse through inheritance

**Expected Output:**
```
Employee: John, Department: HR, Salary: $50000
John's annual bonus: $5000.0
Employee: Sarah, Department: Engineering, Salary: $80000
Sarah's annual bonus: $16000.0
Sarah is managing the Engineering team
Employee: Mike, Department: Engineering, Salary: $70000
Mike's annual bonus: $10500.0
Mike is reviewing code
```

**Success Criteria:**
- ✅ Employee base class with name, salary, department
- ✅ get_info() and get_annual_bonus() methods in base class
- ✅ Manager class inherits from Employee and overrides bonus calculation
- ✅ Developer class inherits from Employee and overrides bonus calculation
- ✅ Manager has manage_team() method, Developer has code_review() method
- ✅ All objects created and methods working correctly