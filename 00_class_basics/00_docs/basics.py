# Class Template
class ClassName:
    def __init__(self, param1, param2) -> None:
        self.attribute1 = param1
        self.attribute2 = param2

    def method_name(self):
        # Method logic here
        pass


value1, value2 = 0, 0
# Object Creation
object_name = ClassName(value1, value2)

# Accessing attributes
print(object_name.attribute1)

# Calling methods
object_name.method_name()

# Multiple objects
obj1 = ClassName("data1", "data2")
obj2 = ClassName("other1", "other2")
