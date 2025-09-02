# 📚 Python OOP Practice - Lesson 5: Library System

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

**Expected Output:**
```
Books in City Library:
The Great Gatsby by F. Scott Fitzgerald (ISBN: 978-0-7432-7356-5)
To Kill a Mockingbird by Harper Lee (ISBN: 978-0-06-112008-4)
1984 by George Orwell (ISBN: 978-0-452-28423-4)

Found book: The Great Gatsby by F. Scott Fitzgerald (ISBN: 978-0-7432-7356-5)
Removed: 1984 by George Orwell (ISBN: 978-0-452-28423-4)

Books in City Library:
The Great Gatsby by F. Scott Fitzgerald (ISBN: 978-0-7432-7356-5)
To Kill a Mockingbird by Harper Lee (ISBN: 978-0-06-112008-4)
```

**Success Criteria:**
- ✅ Book class with title, author, isbn attributes and get_info() method
- ✅ Library class with name and books list attributes
- ✅ add_book() method successfully adds Book objects to collection
- ✅ remove_book() method finds and removes books by ISBN
- ✅ find_book() method searches and returns Book objects
- ✅ list_books() method displays all books in collection
- ✅ Demonstration of adding, listing, finding, and removing books