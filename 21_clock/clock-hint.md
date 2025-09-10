# 💡 Quick Hints

1. `__str__(self)` - return `f"{self.hour:02d}:{self.minute:02d}"`
2. `__repr__(self)` - return `f"Clock({self.hour}, {self.minute})"`
3. `__eq__(self, other)` - use `isinstance()` then compare attributes
4. Normalize time: handle minutes >= 60 and hours >= 24
5. Add/subtract methods should call normalize after changing time