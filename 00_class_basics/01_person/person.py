class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}")


if __name__ == "__main__":
    person1 = Person("Alice")
    person1.say_hello()
