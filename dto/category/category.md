# Category - Nested and Recursive Models

## Exercise: Hierarchical Category Structure

Create a `Category` class using Pydantic's `BaseModel` with nested subcategories to demonstrate recursive validation.

**Task:**
Create a `Category` class using `BaseModel` with the following fields:

- `id: int` - Category ID (must be positive)
- `name: str` - Category name (1-50 characters)
- `subcategories: list[Category]` - List of child categories (default: empty list)

**Example:**

```python
# Simple category
electronics = Category(id=1, name="Electronics")
print(electronics.name)  # Electronics
print(electronics.subcategories)  # []

# Nested categories
computers = Category(id=2, name="Computers", subcategories=[
    Category(id=3, name="Laptops"),
    Category(id=4, name="Desktops")
])
print(len(computers.subcategories))  # 2

# Deep nesting
root = Category(id=1, name="Electronics", subcategories=[
    Category(id=2, name="Computers", subcategories=[
        Category(id=3, name="Laptops"),
        Category(id=4, name="Desktops")
    ]),
    Category(id=5, name="Phones")
])

# Serialization includes nested structure
data = root.model_dump()
print(data['subcategories'][0]['name'])  # Computers
print(data['subcategories'][0]['subcategories'][0]['name'])  # Laptops

# Invalid data raises ValidationError
Category(id=-1, name="Invalid")  # ValidationError (negative ID)
Category(id=1, name="")  # ValidationError (empty name)
```
