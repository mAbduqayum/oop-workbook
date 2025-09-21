## Exercise: Library System

Create a library system using composition - where one class contains objects of another class.

### Your Task:
1. Create a `Book` class with `title`, `author`, and `isbn` attributes
2. Add a `__repr__()` method to `Book` that returns `f"{title} by {author}"`
3. Create a `Library` class with a `name` attribute and an empty `books` list
4. Add an `add_book(book)` method that adds a Book object to the library and prints `f"Added: {book}"`
5. Add a `find_book(title)` method that searches for a book by title and returns the Book object or None
6. Add a `list_books()` method that prints each book on a new line

### Example Usage:
```python
library = Library("City Library")
book1 = Book("1984", "George Orwell", "123")
book2 = Book("Dune", "Frank Herbert", "456")

library.add_book(book1)   # Added: 1984 by George Orwell
library.add_book(book2)   # Added: Dune by Frank Herbert

found = library.find_book("1984")
print(found)              # 1984 by George Orwell

library.list_books()      # Lists all books
```

