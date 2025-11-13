# Data Transfer Objects (DTOs)

## What Are DTOs?

Data Transfer Objects (DTOs) are objects designed to carry data between processes, layers, or services of an
application. They focus on data structure with minimal or no behavior.

**Key Characteristics:**

- Primarily hold state (data)
- Minimal or no business logic
- Used for data transfer between boundaries
- Often immutable

## Why Use DTOs?

1. **Decoupling**: Separate internal data representation from external APIs
2. **Data Shaping**: Control exactly what data is exposed
3. **Performance**: Minimize unnecessary data transfer
4. **Security**: Prevent exposing sensitive internal data
5. **Clear Contracts**: Define explicit boundaries between components

## Common Use Cases

- API request/response models
- Inter-service communication (microservices)
- Database to application layer data transfer
- Configuration management
- External data parsing (JSON, XML, etc.)

## Implementation Methods in Python

### 1. Dataclasses (Recommended for Internal Use)

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class UserDTO:
    id: int
    username: str
    email: str
```

**Advantages:**

- Built into Python (no dependencies)
- Clean, readable syntax
- Supports immutability with `frozen=True`
- Excellent performance

### 2. Pydantic (Recommended for API Boundaries)

```python
from pydantic import BaseModel, EmailStr, Field

class UserDTO(BaseModel):
    id: int
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
```

**Advantages:**

- Built-in validation
- Automatic type coercion
- JSON serialization/deserialization
- Perfect for untrusted external data

### 3. NamedTuples (For Simple Immutable DTOs)

```python
from typing import NamedTuple

class UserDTO(NamedTuple):
    id: int
    username: str
    email: str
```

**Advantages:**

- Guarantees immutability
- Memory efficient
- Lightweight and fast

## Best Practices

### 1. Keep DTOs Simple

```python
@dataclass(frozen=True)
class ProductDTO:
    id: int
    name: str
    price: float
```

### 2. Use Immutability

```python
@dataclass(frozen=True)
class OrderDTO:
    order_id: int
    user_id: int
    total: float
```

### 3. Clear Naming Conventions

```python
class UserCreateDTO(BaseModel):
    username: str
    email: str
    password: str

class UserResponseDTO(BaseModel):
    id: int
    username: str
    email: str
    created_at: str
```

### 4. Separate DTOs by Purpose

```python
class CreateProductDTO(BaseModel):
    name: str
    price: float
    description: str

class ProductResponseDTO(BaseModel):
    id: int
    name: str
    price: float
    created_at: str

class UpdateProductDTO(BaseModel):
    name: str | None = None
    price: float | None = None
    description: str | None = None
```

### 5. Use at Boundaries Only

```python
from pydantic import BaseModel
from dataclasses import dataclass

class UserCreateRequest(BaseModel):
    username: str
    email: str

@dataclass(frozen=True)
class User:
    id: int
    username: str
    email: str

def create_user(request: UserCreateRequest) -> User:
    return User(
        id=generate_id(),
        username=request.username,
        email=request.email
    )
```

## DTO vs DAO Pattern

### DTO (Data Transfer Object)

- Transfers data between layers
- No database logic
- Pure data structure

### DAO (Data Access Object)

- Abstracts database access
- Handles CRUD operations
- Contains database logic

```python
from dataclasses import dataclass
from typing import Protocol

@dataclass(frozen=True)
class UserDTO:
    id: int
    username: str
    email: str

class UserDAO(Protocol):
    def get_by_id(self, user_id: int) -> UserDTO | None: ...
    def save(self, user: UserDTO) -> None: ...
    def delete(self, user_id: int) -> None: ...

class UserRepository:
    def get_by_id(self, user_id: int) -> UserDTO | None:
        return UserDTO(id=user_id, username="alice", email="alice@example.com")

    def save(self, user: UserDTO) -> None:
        pass

    def delete(self, user_id: int) -> None:
        pass
```

## Real-World Example: FastAPI

```python
from pydantic import BaseModel, Field, EmailStr
from dataclasses import dataclass
from datetime import datetime

class CreateUserRequest(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8)

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    model_config = {"from_attributes": True}

@dataclass(frozen=True)
class User:
    id: int
    username: str
    email: str
    password_hash: str
    created_at: datetime

@app.post("/users", response_model=UserResponse)
async def create_user(request: CreateUserRequest):
    user = User(
        id=generate_id(),
        username=request.username,
        email=request.email,
        password_hash=hash_password(request.password),
        created_at=datetime.now()
    )
    save_user(user)
    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        created_at=user.created_at
    )
```

## Decision Guide

### Use Dataclasses When:

- Internal domain objects
- Trusted data
- Performance is critical
- No validation needed
- No external dependencies desired

### Use Pydantic When:

- API request/response models
- Untrusted external data
- Need validation and type coercion
- JSON serialization required
- Configuration parsing

### Use NamedTuples When:

- Simple, immutable data structures
- Need guaranteed immutability
- Maximum performance and minimal memory

## Anti-Patterns to Avoid

### Don't Add Business Logic

```python
@dataclass
class OrderDTO:
    items: list[str]
    total: float

    def calculate_tax(self):
        return self.total * 0.1
```

### Don't Include Sensitive Data

```python
class UserDTO(BaseModel):
    id: int
    username: str
    password: str
    api_key: str
```

### Don't Use DTOs Internally

```python
def process_order(order: OrderDTO) -> OrderDTO:
    pass
```

## Summary

- **DTOs** transfer data between layers/services
- Use **dataclasses** for internal, trusted data
- Use **Pydantic** for external, untrusted data
- Keep DTOs **simple and immutable**
- Apply DTOs only at **boundaries**
- Separate DTOs by **purpose** (create, update, response)
