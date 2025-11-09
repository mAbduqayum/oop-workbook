# Pydantic: Simplifying Data Validation in Python

## Table of Contents

- [What Is Pydantic?](#what-is-pydantic)
- [Installation](#installation)
- [Working With BaseModel](#working-with-basemodel)
  - [Creating Your First Model](#creating-your-first-model)
  - [Validation Errors](#validation-errors)
- [Serialization and Deserialization](#serialization-and-deserialization)
  - [From/To Dictionaries](#creating-models-from-dictionaries)
  - [From/To JSON](#creating-models-from-json)
  - [JSON Schema Generation](#json-schema-generation)
- [Using Fields for Customization](#using-fields-for-customization)
  - [Field Parameters](#enhanced-employee-model)
  - [Common Constraints](#common-field-constraints)
- [Custom Validators](#custom-validators)
  - [Field Validators](#field-validators)
  - [Model Validators](#model-validators)
  - [Validation Modes](#validation-modes)
- [Validating Function Arguments](#validating-function-arguments)
- [Model Configuration](#model-configuration)
- [Advanced Features](#advanced-features)
  - [Nested Models](#nested-models)
  - [Computed Fields](#computed-fields)
  - [Generic Models](#generic-models)
  - [Union Types](#union-types)
- [Settings Management](#managing-settings-with-pydantic-settings)
- [Real-World Use Cases](#real-world-use-cases)
- [Pydantic vs Dataclasses](#pydantic-vs-dataclasses)
- [Best Practices](#best-practices)
- [Common Pitfalls](#common-pitfalls)
- [Performance Considerations](#performance-considerations)
- [Summary](#summary)

---

## What Is Pydantic?

Pydantic is a powerful data validation and settings management library for Python. It's the most widely used data validation library for Python, leveraging type hints to validate and serialize data schemas.

**Why use Pydantic?** Python's dynamic typing is great for rapid development, but real-world applications need robust type checking and data validation.

**Key Features:**

- **Validation**: Automatic data validation with detailed error messages
- **Type Coercion**: Flexible type conversion (e.g., `"123"` → `123`)
- **Serialization**: Seamless JSON/dict conversion
- **Performance**: Core written in Rust (5-50x faster in V2)
- **Ecosystem**: Powers FastAPI, LangChain, Polars, and more

## Installation

Install Pydantic using uv:

```bash
uv add pydantic
# With optional dependencies
uv add pydantic[email]
# For settings management
uv add pydantic-settings
```

## Working With BaseModel

Pydantic's primary way of defining data schemas is through models. A Pydantic model is an object, similar to a Python dataclass, that defines and stores data about an entity with annotated fields. Unlike dataclasses, Pydantic's focus is centered around **automatic data parsing, validation, and serialization**.

### Creating Your First Model

Let's build a model for managing employee information in an HR system:

```python
from datetime import date
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr

class Department(Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"

class Employee(BaseModel):
    employee_id: UUID = uuid4()
    name: str
    email: EmailStr
    date_of_birth: date
    salary: float
    department: Department
    elected_benefits: bool
```

**Key points:**
- `employee_id`: Auto-generates UUID, validated format
- `email`: Uses `EmailStr` for automatic email validation
- `date_of_birth`: Auto-converts string dates to `date` objects
- `department`: Enum ensures only valid departments

### Instantiating Models

```python
employee = Employee(
    name="Chris DeTuma",
    email="cdetuma@example.com",
    date_of_birth="1998-04-02",  # Auto-converted to date
    salary=123_000.00,
    department="IT",  # Auto-converted to Department.IT
    elected_benefits=True,
)
```

Pydantic automatically converts types and validates data.

### Validation Errors

Invalid data raises `ValidationError` with detailed messages:

```python
try:
    Employee(
        employee_id="123",  # Invalid UUID
        email="invalid",  # Missing @
        salary="high",  # Cannot parse
        department="INVALID",  # Not in enum
    )
except ValidationError as e:
    print(e)
    # 7 validation errors with field name, expected type, and docs link
```

## Serialization and Deserialization

### Creating Models From Dictionaries

```python
data = {"name": "Chris", "email": "chris@example.com", "date_of_birth": "1998-04-02", ...}
employee = Employee.model_validate(data)  # Validates and creates model
```

### Creating Models From JSON

```python
json_str = '{"name": "Eric", "email": "eric@example.com", ...}'
employee = Employee.model_validate_json(json_str)  # Parses and validates JSON
```

### Serializing to Dict/JSON

```python
# To dictionary
employee.model_dump()  # All fields
employee.model_dump(exclude={'salary'})  # Exclude specific
employee.model_dump(include={'name', 'email'})  # Include only
employee.model_dump(exclude_unset=True)  # Only set fields

# To JSON
employee.model_dump_json()  # Compact JSON
employee.model_dump_json(indent=2)  # Pretty print
```

### JSON Schema Generation

```python
schema = Employee.model_json_schema()
# Generates OpenAPI-compatible JSON schema for documentation
```

## Using Fields for Customization

### Enhanced Employee Model

```python
from pydantic import BaseModel, EmailStr, Field

class Employee(BaseModel):
    employee_id: UUID = Field(default_factory=uuid4, frozen=True)
    name: str = Field(min_length=1, frozen=True)
    email: EmailStr = Field(pattern=r".+@example\.com$")
    date_of_birth: date = Field(alias="birth_date", repr=False)
    salary: float = Field(alias="compensation", gt=0, repr=False)
    department: Department
    elected_benefits: bool
```

**Common Field Parameters:**
- `default_factory`: Callable for default values
- `frozen`: Immutable after creation
- `min_length` / `max_length`: String/list length
- `pattern`: Regex validation
- `alias`: Alternative field name
- `gt` / `ge` / `lt` / `le`: Numeric constraints
- `repr`: Show in representation
- `description`: Documentation

### Using Aliases and Frozen Fields

```python
# Accept 'birth_date' or 'compensation' as input
data = {"birth_date": "2000-06-12", "compensation": 100_000, ...}
employee = Employee.model_validate(data)

# Frozen fields cannot be changed
employee.department = "HR"  # OK
employee.name = "New Name"  # Error: Field is frozen
```

### Common Constraints & Special Types

```python
class Product(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0, multiple_of=0.01)
    sku: str = Field(pattern=r'^[A-Z]{3}-\d{4}$')
    
class Contact(BaseModel):
    email: EmailStr  # Auto-validates email
    website: HttpUrl  # Auto-validates URL
    created_at: datetime  # Parses datetime strings
    score: PositiveFloat  # Must be > 0
```

## Custom Validators

### Field Validators

```python
from pydantic import field_validator

class Employee(BaseModel):
    date_of_birth: date

    @field_validator('date_of_birth')
    @classmethod
    def check_valid_age(cls, v: date) -> date:
        """Ensure employee is at least 18 years old."""
        today = date.today()
        eighteen_years_ago = date(today.year - 18, today.month, today.day)
        if v > eighteen_years_ago:
            raise ValueError('Employees must be at least 18 years old.')
        return v
```

**Validation modes:**
- `mode='before'`: Run before Pydantic's validation
- `mode='after'`: Run after Pydantic's validation (default)
- `mode='wrap'`: Wrap around Pydantic's validation

### Model Validators

Validate across multiple fields:

```python
from pydantic import model_validator
from typing import Self

class Employee(BaseModel):
    department: Department
    elected_benefits: bool

    @model_validator(mode='after')
    def check_it_benefits(self) -> Self:
        """IT employees are contractors and don't qualify for benefits."""
        if self.department == Department.IT and self.elected_benefits:
            raise ValueError("IT employees don't qualify for benefits")
        return self
```

## Validating Function Arguments

Use `@validate_call` to validate function arguments:

```python
from pydantic import validate_call, EmailStr, PositiveFloat

@validate_call
def send_invoice(
    client_name: str,
    client_email: EmailStr,
    amount_owed: PositiveFloat,
) -> str:
    return f"Invoice sent to {client_email} for ${amount_owed}"

# Automatic validation
send_invoice("John", "john@example.com", 100.0)  # OK
send_invoice("", "invalid", -10)  # ValidationError
```

## Model Configuration

```python
from pydantic import ConfigDict

class StrictUser(BaseModel):
    model_config = ConfigDict(
        frozen=True,  # Immutable
        extra='forbid',  # No extra fields
        validate_assignment=True,  # Validate on updates
        str_strip_whitespace=True,  # Clean strings
    )
    id: int
    name: str
```

**Common options:** `strict`, `extra`, `frozen`, `validate_assignment`, `from_attributes`, `populate_by_name`

## Custom Serialization

```python
from pydantic import field_serializer

class Student(BaseModel):
    courses: set[str]

    @field_serializer('courses')
    def serialize_courses(self, courses: set[str], _info):
        return sorted(courses)  # Sort when serializing
```

## Working With ORM Objects

```python
class UserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str

# Works with SQLAlchemy, Django ORM, etc.
orm_user = SQLAlchemyUser(id=1, username="alice")
user = UserModel.model_validate(orm_user)
```

## Advanced Features

### Nested Models

```python
class Address(BaseModel):
    street: str
    city: str

class Company(BaseModel):
    name: str
    address: Address  # Nested model
    
company = Company(
    name="Tech Corp",
    address={"street": "123 Main St", "city": "NYC"}  # Dict auto-converted
)
```

### Computed Fields

```python
from pydantic import computed_field

class Rectangle(BaseModel):
    width: float
    height: float

    @computed_field
    @property
    def area(self) -> float:
        return self.width * self.height

rect = Rectangle(width=5.0, height=3.0)
print(rect.area)  # 15.0
print(rect.model_dump())  # Includes area
```

### Generic Models

```python
class Response[T](BaseModel):
    data: T
    success: bool = True

response = Response[list[User]](
    data=[User(id=1, name="Alice")]
)
```

### Union Types

```python
class Pet(BaseModel):
    animal: Cat | Dog  # Accept either type
    
# With discriminator for better performance
class Pet(BaseModel):
    animal: Cat | Dog = Field(discriminator='type')
```

## Managing Settings With pydantic-settings

`BaseSettings` reads configuration from environment variables:

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="forbid"
    )
    
    database_url: str
    api_key: str
    debug: bool = False

# Reads from environment variables or .env file
config = AppConfig()
```

**Benefits:** Type validation, `.env` file support, automatic parsing

## Real-World Use Cases

### FastAPI Integration

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class CreateUserRequest(BaseModel):
    username: str = Field(min_length=3)
    email: EmailStr

@app.post("/users")
async def create_user(user: CreateUserRequest):
    # Auto-validates request, generates OpenAPI docs
    return {"id": 1, "username": user.username}
```

### Data Pipeline Validation

```python
class InputData(BaseModel):
    raw_text: str
    timestamp: datetime

class ProcessedData(BaseModel):
    text: str
    word_count: int

def process(raw: InputData) -> ProcessedData:
    cleaned = raw.raw_text.strip()
    return ProcessedData(text=cleaned, word_count=len(cleaned.split()))
```

## Pydantic vs Dataclasses

| Feature | Pydantic | Dataclasses |
|---------|----------|-------------|
| **Validation** | Automatic | None |
| **Type Coercion** | Yes | No |
| **JSON Support** | Built-in | Manual |
| **Performance** | Slower | ~6x faster |
| **Use Case** | API boundaries, external data | Internal objects |

### When to Use Each

**Use Pydantic for:**
- API requests/responses
- External data validation
- Configuration management
- JSON schema generation

**Use Dataclasses for:**
- Internal domain objects
- Performance-critical code
- Already-validated data

### Hybrid Approach (Best Practice)

```python
from dataclasses import dataclass
from pydantic import BaseModel, EmailStr


# Pydantic at API boundary
class UserInput(BaseModel):
    username: str
    email: EmailStr


# Dataclass internally
@dataclass(frozen=True)
class User:
    id: int
    username: str
    email: str


def create_user(input: UserInput) -> User:
    return User(id=generate_id(), username=input.username, email=input.email)
```

## Best Practices

1. **Validate at boundaries** - Use Pydantic at API/external boundaries, dataclasses internally
2. **Use Field constraints** - Prefer `Field(min_length=3)` over custom validators
3. **Descriptive names** - Use `CreateUserRequest`, `UserResponse` not just `User`
4. **Configure appropriately** - Set `frozen=True`, `extra='forbid'` as needed
5. **Document models** - Add docstrings and field descriptions
6. **Handle errors** - Always catch and handle `ValidationError`

```python
# Good example combining best practices
class CreateUserRequest(BaseModel):
    """Request to create a new user."""
    model_config = ConfigDict(frozen=True, extra='forbid')
    
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(ge=18, le=150)
```

## Common Pitfalls

**❌ Over-validation** - Don't use Pydantic for internal objects
```python
# Bad: BaseModel for internal objects
# Good: Use dataclasses internally
```

**❌ Missing constraints** - Don't rely on type hints alone
```python
# Bad: email: str
# Good: email: EmailStr
```

**❌ Mutable defaults** - Use `default_factory`
```python
# Bad: items: list[str] = []
# Good: items: list[str] = Field(default_factory=list)
```

**❌ Ignoring errors** - Always handle `ValidationError`
```python
try:
    user = User(**data)
except ValidationError as e:
    logger.error(f"Validation failed: {e}")
```

## Performance Tips

1. **Use strict mode** - Disable type coercion with `ConfigDict(strict=True)`
2. **Validate at boundaries only** - Don't re-validate internal data
3. **Batch operations** - Validate collections efficiently
4. **Profile first** - Measure before optimizing

## Summary

**Key Takeaways:**

- Automatic validation and type coercion using type hints
- Use at API boundaries for external data
- V2 core in Rust (5-50x faster)
- Powers FastAPI and many major libraries
- Combine with dataclasses for best results

**The Pydantic Philosophy:**

1. **Validate early** - Catch errors at boundaries
2. **Fail fast** - Clear, actionable error messages
3. **Trust internally** - Validated data flows freely
4. **Serialize easily** - Seamless JSON conversion

**Resources:**

- [Official Pydantic Documentation](https://docs.pydantic.dev/)
- [Pydantic with FastAPI](https://fastapi.tiangolo.com/)
- [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [Real Python Tutorial](https://realpython.com/python-pydantic/)
