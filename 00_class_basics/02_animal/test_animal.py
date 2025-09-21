import unittest
from animal import Animal


class TestAnimal(unittest.TestCase):

    def test_animal_attributes(self):
        dog = Animal("Buddy", "Dog")
        self.assertEqual(dog.name, "Buddy")
        self.assertEqual(dog.species, "Dog")

    def test_repr_method(self):
        cat = Animal("Whiskers", "Cat")
        self.assertEqual(repr(cat), "Animal(name='Whiskers', species='Cat')")

    def test_make_sound_exists(self):
        bird = Animal("Tweety", "Bird")
        bird.make_sound()


if __name__ == '__main__':
    unittest.main()