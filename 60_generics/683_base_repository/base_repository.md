# Generic Base Repository

## Exercise: Implement a Generic Repository Pattern with Three Type Parameters

Implement a generic `BaseRepository[T, TCreate, TUpdate]` class that provides CRUD (Create, Read, Update, Delete) operations for database entities. This pattern uses three type parameters: `T` for the full entity, `TCreate` for creation data transfer objects, and `TUpdate` for update data transfer objects.

**Why This Matters:**

The Repository pattern is fundamental in modern web applications and API design. It separates data access logic from business logic, providing a clean abstraction over database operations. By using three distinct type parameters, you model real-world API constraints: creation often requires different fields than updates (no ID during creation), and updates might only include changed fields (partial updates).

This pattern appears everywhere: FastAPI applications with Pydantic models, Django REST Framework serializers, GraphQL resolvers, and microservice architectures. The generic base repository lets you write the CRUD logic once and reuse it for Users, Products, Orders, or any entity—maintaining type safety throughout. Your IDE will autocomplete the correct fields, and the type checker will catch mistakes like passing a `UserCreate` to `ProductsRepository`.

Real-world applications include e-commerce systems managing products and customers, content management systems handling articles and authors, social platforms managing users and posts, and any application with persistent data storage.

**Example Usage:**

```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str
    age: int

@dataclass
class UserCreate:
    name: str
    email: str
    age: int

@dataclass
class UserUpdate:
    name: str | None = None
    email: str | None = None
    age: int | None = None

# Create users repository
users_repo = BaseRepository[User, UserCreate, UserUpdate]()

# Create new user (no ID required)
new_user_data = UserCreate(name="Alice", email="alice@example.com", age=30)
alice = users_repo.create(new_user_data)
print(alice)  # User(id=1, name="Alice", email="alice@example.com", age=30)

# Create another user
bob_data = UserCreate(name="Bob", email="bob@example.com", age=25)
bob = users_repo.create(bob_data)

# Get user by ID
retrieved = users_repo.get(1)
print(retrieved)  # Alice's user object

# Get all users
all_users = users_repo.get_all()
print(len(all_users))  # 2

# Update user (partial update)
update_data = UserUpdate(age=31)  # Only updating age
updated = users_repo.update(1, update_data)
print(updated.age)  # 31
print(updated.name)  # "Alice" (unchanged)

# Delete user
deleted = users_repo.delete(1)
print(deleted)  # True

# Try to get deleted user
missing = users_repo.get(1)
print(missing)  # None
```

**Advanced Example with Multiple Repositories:**

```python
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int
    category: str

@dataclass
class ProductCreate:
    name: str
    price: float
    stock: int
    category: str

@dataclass
class ProductUpdate:
    name: str | None = None
    price: float | None = None
    stock: int | None = None
    category: str | None = None

@dataclass
class Order:
    id: int
    user_id: int
    product_id: int
    quantity: int
    total: float

@dataclass
class OrderCreate:
    user_id: int
    product_id: int
    quantity: int
    total: float

@dataclass
class OrderUpdate:
    quantity: int | None = None
    total: float | None = None

# Products repository
products_repo = BaseRepository[Product, ProductCreate, ProductUpdate]()
laptop = products_repo.create(
    ProductCreate(name="Laptop", price=999.99, stock=50, category="Electronics")
)
phone = products_repo.create(
    ProductCreate(name="Phone", price=699.99, stock=100, category="Electronics")
)

# Orders repository (different entity, same pattern!)
orders_repo = BaseRepository[Order, OrderCreate, OrderUpdate]()
order1 = orders_repo.create(
    OrderCreate(user_id=1, product_id=1, quantity=1, total=999.99)
)

# Update product stock after order
stock_update = ProductUpdate(stock=49)
products_repo.update(laptop.id, stock_update)

# Update order quantity
quantity_update = OrderUpdate(quantity=2, total=1999.98)
orders_repo.update(order1.id, quantity_update)

# Get all products in category
all_products = products_repo.get_all()
electronics = [p for p in all_products if p.category == "Electronics"]
print(f"Electronics count: {len(electronics)}")

# Delete an order
orders_repo.delete(order1.id)
remaining_orders = orders_repo.get_all()
print(f"Remaining orders: {len(remaining_orders)}")  # 0
```

**Testing Requirements:**

Your implementation should pass tests that verify:
- `create()` accepts a `TCreate` object and returns a new `T` object with an auto-generated ID
- IDs are auto-incremented starting from 1
- `get()` returns the entity if found, `None` if not found
- `get_all()` returns a list of all entities
- `update()` accepts a `TUpdate` object and only updates non-None fields
- `update()` returns the updated entity or `None` if the entity doesn't exist
- `delete()` removes the entity and returns `True`, or returns `False` if not found
- The repository maintains type safety with three distinct type parameters
- Multiple repositories can coexist independently (separate storage)
- Empty repository returns empty list for `get_all()`
- Updating with all `None` fields leaves the entity unchanged
- Deleted entities don't appear in `get()` or `get_all()` results
- The pattern works with different entity types (User, Product, Order, etc.)

**Implementation Hints:**

- Store entities in a dictionary using their ID as the key
- Use a counter to auto-generate IDs for new entities
- For updates, iterate through the `TUpdate` object's fields and only apply non-None values
- Use `dataclasses.fields()` or `vars()` to inspect object attributes
- Each repository instance should have its own storage and ID counter
