# 💡 Quick Hints

## Book Class
1. `__init__(self, title, author, isbn)` - store all three
2. `get_info(self)` - `return` formatted string (don't print)

## Library Class  
1. `__init__(self, name)` - set `self.books = []`
2. `add_book(self, book)` - use `self.books.append(book)`
3. `find_book(self, title)` - loop through books, compare `book.title`
4. `remove_book(self, isbn)` - loop, find by ISBN, use `self.books.remove(book)`