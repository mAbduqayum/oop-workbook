import unittest

from person import Person


class TestPerson(unittest.TestCase):
    def test_person_name(self):
        person = Person("Alice")
        self.assertEqual(person.name, "Alice")

    def test_say_hello_exists(self):
        person = Person("Bob")
        person.say_hello()


if __name__ == "__main__":
    unittest.main()
