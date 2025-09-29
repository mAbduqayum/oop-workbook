# Exercise: Library System

Create an inheritance hierarchy for a library system with proper encapsulation and polymorphism.

## Requirements

Design and implement the following class hierarchy:

### Base Class: `LibraryItem`
- **Attributes:**
  - `title` (string): Title of the item
  - `author` (string): Author/creator of the item
  - `item_id` (string): Unique identifier
  - `checkout_status` (boolean): Whether item is checked out
  - `checkout_date` (datetime or None): When item was checked out

- **Methods:**
  - `__init__(title, author, item_id)`: Constructor
  - `checkout()`: Mark item as checked out with current date
  - `return_item()`: Mark item as returned
  - `get_info()`: Return formatted string with item details (to be overridden)
  - `calculate_late_fee(return_date)`: Calculate late fee based on return date (to be overridden)
  - `is_overdue(current_date)`: Check if item is overdue (14 days limit)

### Derived Class: `Book`
- **Additional Attributes:**
  - `pages` (int): Number of pages
  - `genre` (string): Book genre

- **Override Methods:**
  - `get_info()`: Include book-specific details
  - `calculate_late_fee(return_date)`: $0.50 per day overdue

### Derived Class: `Magazine`
- **Additional Attributes:**
  - `issue_number` (int): Magazine issue number
  - `publication_date` (string): Publication date

- **Override Methods:**
  - `get_info()`: Include magazine-specific details
  - `calculate_late_fee(return_date)`: $0.25 per day overdue

### Derived Class: `DVD`
- **Additional Attributes:**
  - `duration` (int): Duration in minutes
  - `rating` (string): Movie rating (G, PG, PG-13, R)

- **Override Methods:**
  - `get_info()`: Include DVD-specific details
  - `calculate_late_fee(return_date)`: $1.00 per day overdue

## Example Usage

```python
from datetime import datetime, timedelta

# Create library items
book = Book("The Python Guide", "John Doe", "B001", 350, "Programming")
magazine = Magazine("Tech Today", "Jane Smith", "M001", 42, "2024-01-15")
dvd = DVD("Python Tutorial", "Tech Corp", "D001", 120, "G")

# Checkout items
book.checkout()
magazine.checkout()
dvd.checkout()

# Display information
print(book.get_info())
print(magazine.get_info())
print(dvd.get_info())

# Calculate late fees (assuming 20 days overdue)
return_date = datetime.now() + timedelta(days=20)
print(f"Book late fee: ${book.calculate_late_fee(return_date):.2f}")
print(f"Magazine late fee: ${magazine.calculate_late_fee(return_date):.2f}")
print(f"DVD late fee: ${dvd.calculate_late_fee(return_date):.2f}")
```

## Expected Output

```
Book: The Python Guide by John Doe (ID: B001)
Pages: 350, Genre: Programming
Status: Checked out on [current date]

Magazine: Tech Today by Jane Smith (ID: M001)
Issue: 42, Published: 2024-01-15
Status: Checked out on [current date]

DVD: Python Tutorial by Tech Corp (ID: D001)
Duration: 120 minutes, Rating: G
Status: Checked out on [current date]

Book late fee: $3.00
Magazine late fee: $1.50
DVD late fee: $6.00
```

## Learning Objectives

- Practice inheritance and method overriding
- Understand polymorphism in action
- Work with datetime calculations
- Implement proper class hierarchies
- Practice encapsulation principles