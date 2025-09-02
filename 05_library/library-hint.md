# 💡 Hints for Library System Exercise

## Understanding Composition
- Composition means one object contains other objects
- Library HAS books (not Library IS-A book)
- The Library class will have a list that stores Book objects
- This is called a "has-a" relationship

## Creating the Book Class First
- Start with the simpler class: `Book`
- Three attributes: `title`, `author`, `isbn`
- `get_info()` method should `return` a formatted string (not print!)
- Use f-string: `f"{self.title} by {self.author} (ISBN: {self.isbn})"`

## Library Class Setup
- Library needs `name` attribute and `books` attribute
- Initialize books as empty list: `self.books = []`
- This list will store Book objects, not strings

## Adding Objects to Collections
- `add_book()` takes a Book object as parameter
- Use `.append()` to add to the list: `self.books.append(book)`
- Call the book's `get_info()` method to display it

## Searching Through Object Collections
- Use a `for` loop to iterate through `self.books`
- Compare object attributes: `if book.title == title:`
- Return the actual Book object when found
- Return `None` if not found (Python default for missing items)

## Removing Objects from Collections
- Loop through books to find the one with matching ISBN
- Use `self.books.remove(book)` to remove it
- Remember to `return` after removing to stop the loop
- Print error message if not found

## Working with Object Methods
- When you have a Book object, call its methods: `book.get_info()`
- The Library doesn't need to know Book's internal details
- Each Book is responsible for displaying its own information

## List Management Patterns
```python
# Adding to list
self.books.append(book_object)

# Searching in list
for book in self.books:
    if book.attribute == search_value:
        return book

# Removing from list  
for book in self.books:
    if book.attribute == search_value:
        self.books.remove(book)
        return
```

## Testing Object Interactions
1. Create Book objects first
2. Create Library object
3. Add books to library (pass Book objects, not strings)
4. Test each method to make sure objects interact correctly
5. Verify that removing/adding changes the collection

## Key Concept: Objects Calling Objects
- Library calls Book methods: `book.get_info()`
- Book doesn't know about Library
- Library manages the collection, Book manages its own data
- This separation makes code cleaner and more maintainable

## Common Composition Mistakes
- Don't store strings in books list - store Book objects
- Don't forget to call `book.get_info()` when displaying
- Remember `return` vs `print` - get_info() returns, others print
- Don't modify Book attributes directly from Library - use Book methods