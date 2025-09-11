# 💡 Quick Hints

1. `Employee` class: `__init__(self, name, salary, department)`, `get_info()`, `get_annual_bonus()`
2. `class Manager(Employee):` - inherits everything from Employee
3. Override bonus method: different calculation for Manager
4. Add `manage_team(self)` method to Manager only
5. Same pattern for `Developer(Employee)` with `code_review(self)`