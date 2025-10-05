class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def list_books(self):
        for book in self.books:
            print(book)


if __name__ == "__main__":
    library = Library("City Library")
    book1 = Book("1984", "George Orwell", "123")
    book2 = Book("Dune", "Frank Herbert", "456")

    library.add_book(book1)
    library.add_book(book2)

    found = library.find_book("1984")
    print(found)

    library.list_books()
