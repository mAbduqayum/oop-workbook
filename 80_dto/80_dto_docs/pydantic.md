# Pydantic V2

## What Is Pydantic?

Pydantic is the most widely used data validation library for Python. It provides runtime type checking, data validation, and serialization using Python type annotations.

**Key Features:**
- Automatic data validation
- Type coercion
- Clear error messages
- JSON serialization/deserialization
- JSON Schema generation
- FastAPI integration

## Why Use Pydantic?

1. **Runtime Validation**: Catches errors at runtime
2. **Type Safety**: Ensures data matches expected types
3. **Developer Experience**: Clear, detailed error messages
4. **Performance**: V2 core rewritten in Rust (5-50x faster)
5. **Ecosystem**: Native FastAPI support

## Installation

```bash
uv add pydantic
uv add pydantic[email]
```

## Core Concepts

### BaseModel Basics

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True

user = User(id=1, name="Alice", email="alice@example.com")
print(user.id)
print(user.model_dump())
```

### Automatic Type Coercion

```python
class Product(BaseModel):
    id: int
    price: float
    quantity: int

product = Product(id="123", price="19.99", quantity="5")
print(product.id)
print(type(product.id))
print(product.price)
print(type(product.price))
```

### Validation Errors

```python
from pydantic import ValidationError

class User(BaseModel):
    id: int
    name: str

try:
    User(id="invalid", name="Alice")
except ValidationError as e:
    print(e)
    print(e.errors())
```

## Field Validation

### Field Constraints

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(gt=0, description="User ID must be positive")
    username: str = Field(min_length=3, max_length=50)
    age: int = Field(ge=0, le=150)
    score: float = Field(ge=0.0, le=100.0)
    tags: list[str] = Field(max_length=10)
```

### Common Field Constraints

```python
from pydantic import Field

class Product(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0, multiple_of=0.01)
    stock: int = Field(ge=0)
    sku: str = Field(pattern=r'^[A-Z]{3}-\d{4}$')
```

**Available Constraints:**
- `gt`, `ge`, `lt`, `le`: Numeric comparisons
- `min_length`, `max_length`: String/list length
- `pattern`: Regex pattern matching
- `multiple_of`: Value must be multiple of
- `strict`: Disable type coercion

### Special Field Types

```python
from pydantic import BaseModel, EmailStr, HttpUrl, UUID4
from datetime import datetime

class Contact(BaseModel):
    email: EmailStr
    website: HttpUrl
    user_id: UUID4
    created_at: datetime
```

## Custom Validators

### Field Validators

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str
    email: str

    @field_validator('username')
    @classmethod
    def username_alphanumeric(cls, v: str) -> str:
        if not v.isalnum():
            raise ValueError('must be alphanumeric')
        return v

    @field_validator('email')
    @classmethod
    def email_lowercase(cls, v: str) -> str:
        return v.lower()
```

### Multiple Field Validation

```python
class Product(BaseModel):
    name: str
    price: float

    @field_validator('name', 'price')
    @classmethod
    def not_empty(cls, v):
        if not v:
            raise ValueError('field cannot be empty')
        return v
```

### Validation Modes

```python
class User(BaseModel):
    username: str

    @field_validator('username', mode='before')
    @classmethod
    def strip_whitespace(cls, v):
        if isinstance(v, str):
            return v.strip()
        return v

    @field_validator('username', mode='after')
    @classmethod
    def validate_length(cls, v: str) -> str:
        if len(v) < 3:
            raise ValueError('must be at least 3 characters')
        return v
```

### Model Validators

```python
from pydantic import BaseModel, model_validator

class UserRegistration(BaseModel):
    password: str
    password_confirm: str

    @model_validator(mode='after')
    def check_passwords_match(self):
        if self.password != self.password_confirm:
            raise ValueError('passwords do not match')
        return self
```

### Wrap Validators

```python
from pydantic import field_validator

class Model(BaseModel):
    value: int

    @field_validator('value', mode='wrap')
    @classmethod
    def validate_value(cls, v, handler):
        try:
            result = handler(v)
            if result < 0:
                return 0
            return result
        except ValueError:
            return 0
```

## Configuration

### ConfigDict

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        extra='forbid',
        str_strip_whitespace=True,
        validate_assignment=True,
        from_attributes=True,
    )

    id: int
    name: str
```

### Common Configuration Options

```python
class StrictModel(BaseModel):
    model_config = ConfigDict(
        strict=True,
        extra='forbid',
        frozen=True,
        validate_assignment=True,
        str_strip_whitespace=True,
        str_to_lower=True,
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )
```

**Configuration Options:**
- `strict`: Disable type coercion
- `extra`: 'forbid', 'allow', or 'ignore' extra fields
- `frozen`: Make model immutable
- `validate_assignment`: Validate on attribute changes
- `str_strip_whitespace`: Strip whitespace from strings
- `str_to_lower`: Convert strings to lowercase
- `from_attributes`: Allow creation from ORM objects
- `populate_by_name`: Allow field name and alias

## Serialization

### Model to Dict

```python
from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    name: str
    timestamp: datetime
    priority: int

event = Event(name="Launch", timestamp=datetime.now(), priority=1)

print(event.model_dump())

print(event.model_dump(exclude={'priority'}))

print(event.model_dump(include={'name', 'timestamp'}))

print(event.model_dump(exclude_unset=True))
```

### Model to JSON

```python
class User(BaseModel):
    id: int
    name: str
    created_at: datetime

user = User(id=1, name="Alice", created_at=datetime.now())
print(user.model_dump_json())
print(user.model_dump_json(indent=2))
```

### Custom Serialization

```python
from pydantic import BaseModel, field_serializer

class Student(BaseModel):
    name: str
    courses: set[str]

    @field_serializer('courses')
    def serialize_courses(self, courses: set[str], _info):
        return sorted(courses)

student = Student(name="Alice", courses={'Math', 'Physics', 'Chemistry'})
print(student.model_dump_json())
```

### Serialization Aliases

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(serialization_alias='userId')
    email: str = Field(serialization_alias='emailAddress')

user = User(id=1, email="alice@example.com")
print(user.model_dump(by_alias=True))
```

## Deserialization

### From Dictionary

```python
class User(BaseModel):
    id: int
    name: str
    email: str

data = {"id": 1, "name": "Alice", "email": "alice@example.com"}
user = User(**data)

user = User.model_validate(data)
```

### From JSON

```python
json_str = '{"id": 1, "name": "Alice", "email": "alice@example.com"}'
user = User.model_validate_json(json_str)
```

### From ORM Objects

```python
from pydantic import BaseModel, ConfigDict

class UserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str

class SQLAlchemyUser:
    def __init__(self, id: int, username: str):
        self.id = id
        self.username = username

orm_user = SQLAlchemyUser(id=1, username="alice")
user = UserModel.model_validate(orm_user)
```

## Advanced Features

### Nested Models

```python
class Address(BaseModel):
    street: str
    city: str
    country: str

class Company(BaseModel):
    name: str
    address: Address
    employees: list[str]

company = Company(
    name="Tech Corp",
    address={"street": "123 Main St", "city": "NYC", "country": "USA"},
    employees=["Alice", "Bob"]
)
```

### Computed Fields

```python
from pydantic import BaseModel, computed_field

class Rectangle(BaseModel):
    width: float
    height: float

    @computed_field
    @property
    def area(self) -> float:
        return self.width * self.height

rect = Rectangle(width=5.0, height=3.0)
print(rect.area)
print(rect.model_dump())
```

### Field Aliases

```python
from pydantic import BaseModel, Field, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(alias='userId')
    email: str = Field(alias='emailAddress')

user1 = User(userId=1, emailAddress="alice@example.com")
user2 = User(id=1, email="alice@example.com")
```

### Validation Aliases

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(validation_alias='user_id')
    name: str

data = {"user_id": 1, "name": "Alice"}
user = User.model_validate(data)
print(user.model_dump())
```

### Generic Models

```python
from pydantic import BaseModel

class Response[T](BaseModel):
    data: T
    error: str = ""
    success: bool = True

class User(BaseModel):
    id: int
    name: str

response = Response[list[User]](
    data=[User(id=1, name="Alice"), User(id=2, name="Bob")]
)
```

### Union Types

```python
class Cat(BaseModel):
    pet_type: str = "cat"
    meow: str

class Dog(BaseModel):
    pet_type: str = "dog"
    bark: str

class Pet(BaseModel):
    animal: Cat | Dog

cat_data = {"animal": {"pet_type": "cat", "meow": "loud"}}
dog_data = {"animal": {"pet_type": "dog", "bark": "quiet"}}

cat = Pet.model_validate(cat_data)
dog = Pet.model_validate(dog_data)
```

### Discriminated Unions

```python
from pydantic import BaseModel, Field

class Cat(BaseModel):
    type: str = Field(default="cat", frozen=True)
    meow: str

class Dog(BaseModel):
    type: str = Field(default="dog", frozen=True)
    bark: str

class Pet(BaseModel):
    animal: Cat | Dog = Field(discriminator='type')

pet = Pet.model_validate({"animal": {"type": "cat", "meow": "loud"}})
```

## Real-World Use Cases

### FastAPI Integration

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class CreateUserRequest(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8)

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

@app.post("/users", response_model=UserResponse)
async def create_user(user: CreateUserRequest):
    return UserResponse(id=1, username=user.username, email=user.email)
```

### Configuration Management

```python
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = "MyApp"
    database_url: str
    api_key: str = Field(validation_alias="API_KEY")
    debug: bool = False
    max_connections: int = 10

    model_config = {"env_file": ".env"}

settings = Settings()
```

### Data Processing Pipeline

```python
from pydantic import BaseModel, field_validator
from datetime import datetime

class InputData(BaseModel):
    raw_text: str
    timestamp: datetime
    source: str

class ProcessedData(BaseModel):
    text: str
    word_count: int
    source: str

    @field_validator('text')
    @classmethod
    def text_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('text cannot be empty')
        return v

def process(raw: InputData) -> ProcessedData:
    cleaned = raw.raw_text.strip()
    return ProcessedData(
        text=cleaned,
        word_count=len(cleaned.split()),
        source=raw.source
    )
```

### JSON Schema Generation

```python
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    tags: list[str]

schema = Product.model_json_schema()
print(schema)
```

## Comparison with Dataclasses

| Feature | Pydantic | Dataclasses |
|---------|----------|-------------|
| **Performance** | Slower (validation) | 6x faster |
| **Validation** | Built-in | None |
| **Type Coercion** | Automatic | None |
| **JSON Support** | Excellent | Manual |
| **Dependencies** | External | Built-in |
| **Use Case** | API boundaries | Internal objects |
| **Error Messages** | Detailed | Basic |
| **Schema Generation** | Yes | No |

## When to Use Pydantic

### Use Pydantic When:
- Validating external/untrusted data
- Building REST APIs (especially FastAPI)
- Parsing configuration files
- Working with JSON data
- Need automatic type coercion
- Need JSON schema generation
- Handling user input
- Environment variable parsing

### Use Dataclasses When:
- Internal domain objects
- Performance is critical
- No validation needed
- Want lightweight solution
- No external dependencies desired

## Best Practices

### 1. Validate at Boundaries

```python
class UserInput(BaseModel):
    username: str
    email: EmailStr

@dataclass(frozen=True)
class User:
    id: int
    username: str
    email: str

def create_user(input: UserInput) -> User:
    return User(id=generate_id(), username=input.username, email=input.email)
```

### 2. Use Field Constraints

```python
class User(BaseModel):
    username: str = Field(min_length=3, max_length=50, pattern=r'^[a-zA-Z0-9_]+$')
    email: EmailStr
    age: int = Field(ge=0, le=150)
```

### 3. Clear Model Names

```python
class CreateUserRequest(BaseModel):
    username: str
    email: str

class UpdateUserRequest(BaseModel):
    username: str | None = None
    email: str | None = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
```

### 4. Use ConfigDict

```python
class User(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        extra='forbid',
        validate_assignment=True,
    )
```

### 5. Reusable Validators

```python
from pydantic import field_validator

class BaseModel(BaseModel):
    @field_validator('*', mode='before')
    @classmethod
    def strip_strings(cls, v):
        if isinstance(v, str):
            return v.strip()
        return v
```

## Common Pitfalls

### Over-Validation

```python
@dataclass
class InternalObject:
    pass
```

### No Constraints

```python
class User(BaseModel):
    email: str

class BetterUser(BaseModel):
    email: EmailStr
```

### Mutable Defaults

```python
class Bad(BaseModel):
    items: list[str] = []

class Good(BaseModel):
    items: list[str] = Field(default_factory=list)
```

## Performance Tips

1. **Use Strict Mode**: Disable coercion when not needed
2. **Avoid Over-Validation**: Only validate at boundaries
3. **Reuse Models**: Create model instances once
4. **Use Slots**: Combine with `__slots__` for memory savings
5. **Profile**: Measure before optimizing

## Summary

- Pydantic provides **automatic validation** and **type coercion**
- Use at **API boundaries** and for **untrusted data**
- V2 core is **rewritten in Rust** for better performance
- **Field constraints** provide powerful validation
- **Custom validators** handle complex logic
- **ConfigDict** controls model behavior
- Perfect for **FastAPI** and **configuration management**
- Use **dataclasses** for internal domain objects
