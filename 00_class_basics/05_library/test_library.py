import unittest

from library import Book, Library


class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("1984", "George Orwell", "123")
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "George Orwell")
        self.assertEqual(book.isbn, "123")

    def test_book_repr(self):
        book = Book("Dune", "Frank Herbert", "456")
        self.assertEqual(str(book), "Dune by Frank Herbert")


class TestLibrary(unittest.TestCase):
    def test_library_creation(self):
        library = Library("City Library")
        self.assertEqual(library.name, "City Library")
        self.assertEqual(library.books, [])

    def test_add_book(self):
        library = Library("Test Library")
        book = Book("Test Book", "Test Author", "789")
        library.add_book(book)
        self.assertEqual(len(library.books), 1)
        self.assertEqual(library.books[0], book)

    def test_find_book_exists(self):
        library = Library("Test Library")
        book = Book("Test Book", "Test Author", "789")
        library.add_book(book)
        found = library.find_book("Test Book")
        self.assertEqual(found, book)

    def test_find_book_not_exists(self):
        library = Library("Test Library")
        found = library.find_book("Nonexistent Book")
        self.assertIsNone(found)


if __name__ == "__main__":
    unittest.main()
