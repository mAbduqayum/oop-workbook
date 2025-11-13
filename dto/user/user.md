# User - Pydantic Data Validation

## Exercise: User Model with Validation

Create a `User` class using Pydantic's `BaseModel` with automatic validation for email, age constraints, and custom
field validation.

**Task:**

1. Create a `User` class using `BaseModel` with the following fields:
    - `id: UUID` - User ID (UUID v4)
    - `username: str` - Username (3-20 chars, only alphanumeric and underscores)
    - `email: EmailStr` - Valid email address
    - `age: int` - User age (must be >= 18)
    - `is_active: bool` - Account status (default: True)

**Example:**

```python
from uuid import uuid4

user = User(id=uuid4(), username="john_doe", email="john@example.com", age=25)
print(user.username)  # john_doe
print(user.model_dump())  # Dictionary with all fields

# Serialization
json_str = user.model_dump_json()
user2 = User.model_validate_json(json_str)

# Invalid data raises ValidationError
User(id=uuid4(), username="ab", email="invalid", age=15)  # ValidationError
User(id=uuid4(), username="john@doe", email="john@example.com", age=25)  # ValidationError (invalid username)
```
