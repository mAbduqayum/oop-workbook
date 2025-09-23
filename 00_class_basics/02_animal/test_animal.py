from animal import Animal


class TestAnimal:
    def test_animal_attributes(self):
        dog = Animal("Buddy", "Dog")
        assert dog.name == "Buddy"
        assert dog.species == "Dog"

    def test_repr_method(self):
        cat = Animal("Whiskers", "Cat")
        assert repr(cat) == "Animal(name='Whiskers', species='Cat')"

    def test_make_sound_exists(self):
        bird = Animal("Tweety", "Bird")
        bird.make_sound()
