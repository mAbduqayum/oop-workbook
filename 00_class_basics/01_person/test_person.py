from person import Person


class TestPerson:
    def test_person_name(self):
        person = Person("Alice")
        assert person.name == "Alice"

    def test_say_hello_exists(self):
        person = Person("Bob")
        person.say_hello()
