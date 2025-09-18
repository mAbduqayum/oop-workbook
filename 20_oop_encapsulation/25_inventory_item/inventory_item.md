# 📦 Python OOP Practice - Lesson 25: InventoryItem Class

## 📝 Exercise: Business Logic with Stock Management

Create an `InventoryItem` class that manages product inventory with stock tracking, pricing, and business rule validation. This demonstrates real-world business logic encapsulation.

**Instructions:**
Implement an inventory management system that tracks stock quantities, handles pricing, and enforces business rules.

The item should protect critical business data like stock levels and pricing from invalid modifications.

Stock operations should follow realistic business constraints and validation.

**Your Complete Task:**
1. Create an `InventoryItem` class with constructor parameters:
   - `name` (string): Product name
   - `price` (float): Unit price (must be positive)
   - `initial_stock` (int): Starting stock quantity (default 0)
2. Store stock quantity privately with underscore prefix (`_stock`)
3. Add `get_name()` method (read-only after creation)
4. Add `get_price()` and `set_price()` methods with validation for positive values
5. Add `get_stock()` method (read-only) that returns current stock level
6. Add `restock(quantity)` method that adds stock (quantity must be positive)
7. Add `sell(quantity)` method that removes stock if sufficient quantity available
8. Add `get_is_in_stock()` method that returns True if stock > 0
9. Add `is_low_stock(threshold=5)` method that returns True if stock <= threshold
10. Add `get_total_value()` method that returns stock × price
11. Add proper validation with `ValueError` for invalid operations
12. Add `__str__()` method that returns formatted item information

**What You'll Learn:**
- **Business Logic Encapsulation:** Protecting business rules and data integrity
- **Stock Management:** Real-world inventory operations and constraints
- **Method Validation:** Ensuring data remains valid through controlled access
- **Transaction Safety:** Preventing invalid business operations
- **Computed Methods:** Deriving values from encapsulated data

**Business Rules:**
- Price must always be positive (> 0)
- Stock cannot go negative
- Restock quantity must be positive
- Sell quantity must be positive and not exceed available stock

**Example Usage:**
```python
# Create inventory item
item = InventoryItem("Laptop", 999.99, 10)
print(item)  # "Laptop: $999.99, Stock: 10 units, Value: $9999.90"

# Check stock status
print(item.get_is_in_stock())      # True
print(item.is_low_stock())         # False (stock > 5)
print(item.is_low_stock(15))       # True (stock <= 15)

# Restock operations
item.restock(5)
print(item.get_stock())            # 15
print(item.get_total_value())      # 14999.85

# Sales operations
item.sell(3)
print(item.get_stock())            # 12

# Try to sell more than available
try:
    item.sell(20)                  # Should fail - not enough stock
except ValueError as e:
    print(e)  # "Cannot sell 20 units. Only 12 units in stock."

# Price validation
try:
    item.set_price(-50)            # Should fail - negative price
except ValueError as e:
    print(e)  # "Price must be positive"

# Invalid operations
try:
    item.restock(-5)               # Should fail - negative restock
except ValueError as e:
    print(e)  # "Restock quantity must be positive"

# Low stock scenario
phone = InventoryItem("Phone", 599.99, 3)
print(phone.is_low_stock())  # True (stock <= 5)

# Out of stock scenario
tablet = InventoryItem("Tablet", 299.99, 0)
print(tablet.get_is_in_stock())    # False
```

**Bonus Features:**
- Add `discount(percentage)` method that reduces price by percentage (0-100)
- Add `sell_all()` method that sells entire stock and returns total revenue
- Track sales history with `get_total_sold()` method