from library import Book, Library


class TestBook:
    def test_book_creation(self):
        book = Book("1984", "George Orwell", "123")
        assert book.title == "1984"
        assert book.author == "George Orwell"
        assert book.isbn == "123"

    def test_book_repr(self):
        book = Book("Dune", "Frank Herbert", "456")
        assert str(book) == "Dune by Frank Herbert"


class TestLibrary:
    def test_library_creation(self):
        library = Library("City Library")
        assert library.name == "City Library"
        assert library.books == []

    def test_add_book(self):
        library = Library("Test Library")
        book = Book("Test Book", "Test Author", "789")
        library.add_book(book)
        assert len(library.books) == 1
        assert library.books[0] == book

    def test_find_book_exists(self):
        library = Library("Test Library")
        book = Book("Test Book", "Test Author", "789")
        library.add_book(book)
        found = library.find_book("Test Book")
        assert found == book

    def test_find_book_not_exists(self):
        library = Library("Test Library")
        found = library.find_book("Nonexistent Book")
        assert found is None
