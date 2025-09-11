# 📚 Python OOP Practice - Lesson: Library System

## 📝 Exercise: Build a Library Management System

Create a library system using **composition** - where one class contains objects of another class. This teaches how objects work together.

**Your Complete Task:**
1. Create a `Book` class with `title`, `author`, and `isbn` attributes
2. Add a `get_info()` method to `Book` that returns "[title] by [author] (ISBN: [isbn])"
3. Create a `Library` class with a `name` attribute and an empty `books` list
4. Add an `add_book(book)` method that adds a Book object to the library and prints "Added: [book info]"
5. Add a `remove_book(isbn)` method that removes a book by ISBN and prints "Removed: [book info]" or "Book not found"
6. Add a `find_book(title)` method that searches for a book by title and returns the Book object or None
7. Add a `list_books()` method that prints all books in the library
8. Create a library, add 3 books, list them, find one book, and remove one book

**What You'll Learn:**
- **Composition**: Classes containing other objects (Library HAS Books)
- Managing collections of objects with lists
- Object interactions: one object calling methods on another
- Searching and filtering object collections
- "Has-a" relationships vs "is-a" relationships

**Example Usage:**
```python
# Create a library and some books
library = Library("City Library")
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4")
book3 = Book("1984", "George Orwell", "978-0-452-28423-4")

# Add books and list them
library.add_book(book1)   # Added: The Great Gatsby by F. Scott Fitzgerald (ISBN: 978-0-7432-7356-5)
library.add_book(book2)   # Added: To Kill a Mockingbird by Harper Lee (ISBN: 978-0-06-112008-4)
library.add_book(book3)   # Added: 1984 by George Orwell (ISBN: 978-0-452-28423-4)

library.list_books()      # Books in City Library: [lists all books]

# Find and remove books
found = library.find_book("The Great Gatsby")
print(f"Found book: {found.get_info()}")  # Found book: The Great Gatsby by...

library.remove_book("978-0-452-28423-4")  # Removed: 1984 by George Orwell...
library.list_books()                       # Books in City Library: [updated list]
```

