class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} makes a sound!")

    def __repr__(self):
        return f"Animal(name='{self.name}', species='{self.species}')"


if __name__ == "__main__":
    dog = Animal("Buddy", "Dog")
    print(dog)
    dog.make_sound()
