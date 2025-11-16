# Pydantic: Simplifying Data Validation in Python

## Table of Contents

- [What Is Pydantic?](#what-is-pydantic)
- [Installation](#installation)
- [Quick Start: Why Use Pydantic?](#quick-start-why-use-pydantic)
    - [The Problem: Manual Validation is Tedious](#the-problem-manual-validation-is-tedious)
    - [The Solution: Pydantic Does It All](#the-solution-pydantic-does-it-all)
    - [Basic Types Reference](#basic-types-reference)
- [Working With BaseModel](#working-with-basemodel)
    - [The Problem: Unstructured Data is Hard to Work With](#the-problem-unstructured-data-is-hard-to-work-with)
    - [The Solution: Start with Simple Models](#the-solution-start-with-simple-models)
    - [Building a More Complete Model](#building-a-more-complete-model)
    - [Validation Errors](#validation-errors)
    - [BaseModel Core Methods](#basemodel-core-methods)
- [Serialization and Deserialization](#serialization-and-deserialization)
    - [The Problem: Manual Dict/JSON Conversion is Tedious](#the-problem-manual-dictjson-conversion-is-tedious)
    - [The Solution: Automatic Serialization](#the-solution-automatic-serialization)
    - [Serialization Methods Reference](#serialization-methods-reference)
- [Using Fields for Customization](#using-fields-for-customization)
    - [The Problem: Basic Type Annotations Aren't Enough](#the-problem-basic-type-annotations-arent-enough)
    - [The Solution: Use Field() for Fine-Grained Control](#the-solution-use-field-for-fine-grained-control)
    - [Field Parameters & Constraints Reference](#field-parameters--constraints-reference)
- [Special Types for Common Validations](#special-types-for-common-validations)
    - [The Problem: Repetitive Validation Logic](#the-problem-repetitive-validation-logic)
    - [The Solution: Use Pydantic's Special Types](#the-solution-use-pydantics-special-types)
    - [Special Types Reference](#special-types-reference)
- [Custom Validators](#custom-validators)
    - [The Problem: Business Logic Validation Needs](#the-problem-business-logic-validation-needs)
    - [The Solution: Custom Validators](#the-solution-custom-validators)
    - [Validator Modes & Decorators Reference](#validator-modes--decorators-reference)
- [Model Configuration](#model-configuration)
    - [The Problem: Default Behavior Doesn't Fit All Use Cases](#the-problem-default-behavior-doesnt-fit-all-use-cases)
    - [The Solution: Configure Model Behavior](#the-solution-configure-model-behavior)
    - [Configuration Options Reference](#configuration-options-reference)
- [Custom Serialization](#custom-serialization)
- [Working With ORM Objects](#working-with-orm-objects)
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

Pydantic is a powerful data validation and settings management library for Python. It's the most widely used data
validation library for Python, leveraging type hints to validate and serialize data schemas.

**Why use Pydantic?** Python's dynamic typing is great for rapid development, but real-world applications need robust
type checking and data validation.

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

## Quick Start: Why Use Pydantic?

Let's see Pydantic in action with three common scenarios that every Python developer faces.

### The Problem: Manual Validation is Tedious

**Scenario 1: User Registration**

Without Pydantic, validating user input requires lots of manual checks:

```python
def create_user(data: dict):
    # Manual validation - error-prone and verbose
    if not isinstance(data.get('name'), str) or len(data['name']) < 1:
        raise ValueError("Name must be a non-empty string")

    if not isinstance(data.get('age'), int) or data['age'] < 18:
        raise ValueError("Age must be an integer >= 18")

    email = data.get('email', '')
    if '@' not in email or '.' not in email:
        raise ValueError("Invalid email format")

    return data


# Error messages are vague, type conversion is manual
create_user({"name": "Alice", "age": "25", "email": "alice@example.com"})  # Fails! Age is string
```

**Scenario 2: API Data Parsing**

When consuming external APIs, you get raw dictionaries that need validation:

```python
# API returns this
api_response = {
    "product_id": "12345",  # Should be int
    "price": "29.99",  # Should be float
    "in_stock": "true"  # Should be bool
}

# Manual conversion and validation
try:
    product_id = int(api_response['product_id'])
    price = float(api_response['price'])
    in_stock = api_response['in_stock'].lower() == 'true'
except (KeyError, ValueError, AttributeError) as e:
    # Generic error handling
    print(f"Failed to parse API response: {e}")
```

**Scenario 3: Configuration Loading**

Loading application settings without validation leads to runtime errors:

```python
import os

# No validation until you try to use it
DATABASE_URL = os.getenv('DATABASE_URL')  # Might be None!
DEBUG = os.getenv('DEBUG')  # String "false" is truthy!
MAX_CONNECTIONS = os.getenv('MAX_CONN')  # String, not int

# Errors appear later in the application
if DEBUG:  # BUG: Even "false" is truthy!
    print("Debug mode enabled")
```

### The Solution: Pydantic Does It All

Now let's solve the same problems with Pydantic:

**Scenario 1: User Registration** ✨

```python
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    age: int
    email: EmailStr  # Auto-validates email format


# Automatic type conversion and validation
user = User(name="Alice", age="25", email="alice@example.com")  # ✓ Works!
print(user.age)  # 25 (converted to int)

# Clear error messages
try:
    User(name="", age=15, email="invalid")
except ValidationError as e:
    print(e)
    # 3 validation errors for User
    # name: String should have at least 1 character
    # age: Input should be greater than or equal to 18
    # email: value is not a valid email address
```

**Scenario 2: API Data Parsing** ✨

```python
class Product(BaseModel):
    product_id: int
    price: float
    in_stock: bool


# Automatic type conversion from API response
product = Product(**api_response)
print(product.product_id)  # 12345 (int)
print(product.price)  # 29.99 (float)
print(product.in_stock)  # True (bool)
```

**Scenario 3: Configuration Loading** ✨

```python
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    database_url: str
    debug: bool = False
    max_connections: int = 10


# Reads from environment variables, validates types
config = AppConfig()  # Raises error if DATABASE_URL missing!
print(config.debug)  # False (properly converted from "false" string)
```

### What Just Happened?

Pydantic automatically:

- ✅ **Validates** data types and formats
- ✅ **Converts** types ("25" → 25, "true" → True)
- ✅ **Provides** clear error messages with field names
- ✅ **Enforces** constraints (email format, minimum age)
- ✅ **Handles** missing/extra fields gracefully

### Basic Types Reference

Here are the fundamental types you'll use with Pydantic:

| Python Type   | What It Accepts / Does                                 | Example                        |
|---------------|--------------------------------------------------------|--------------------------------|
| `str`         | String or coercible types → converts to string         | `name: str`                    |
| `int`         | Integer or coercible types → converts to int           | `age: int`                     |
| `float`       | Float or coercible types → converts to float           | `price: float`                 |
| `bool`        | Boolean or coercible types ("true"→True, 1→True, etc.) | `active: bool`                 |
| `list`        | List or sequence → converts iterables to list          | `tags: list[str]`              |
| `dict`        | Dictionary or mapping → validates structure            | `metadata: dict[str, str]`     |
| `set`         | Set or iterable → converts to set (removes duplicates) | `unique_ids: set[int]`         |
| `tuple`       | Tuple or sequence → converts to tuple                  | `coords: tuple[float, float]`  |
| `datetime`    | datetime object or ISO string → parses strings         | `created: datetime`            |
| `date`        | date object or ISO string → parses strings             | `birth_date: date`             |
| `Path`        | Path or string → converts to pathlib.Path              | `file_path: Path`              |
| `UUID`        | UUID or valid UUID string → validates format           | `id: UUID`                     |
| `Literal`     | Only specific allowed values → validates exact match   | `status: Literal['on', 'off']` |
| `Optional[T]` | Type T or None → allows None values                    | `middle_name: Optional[str]`   |
| `list[T]`     | List with specific item type → validates each item     | `scores: list[int]`            |
| `dict[K, V]`  | Dict with key/value types → validates keys and values  | `prices: dict[str, float]`     |

**Type Coercion Examples:**

```python
from pydantic import BaseModel


class Example(BaseModel):
    count: int
    price: float
    active: bool


# All of these work due to type coercion
ex = Example(count="42", price="19.99", active="yes")
print(ex.count)  # 42 (int)
print(ex.price)  # 19.99 (float)
print(ex.active)  # True (bool)
```

## Working With BaseModel

Pydantic's primary way of defining data schemas is through models. A Pydantic model is an object, similar to a Python
dataclass, that defines and stores data about an entity with annotated fields. Unlike dataclasses, Pydantic's focus is
centered around **automatic data parsing, validation, and serialization**.

### The Problem: Unstructured Data is Hard to Work With

Working with raw dictionaries leads to errors and unclear contracts:

```python
# What fields does this have? What types? No one knows!
user_data = {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25
}


def send_email(user):
    # Is 'email' definitely present? Is it a valid email? Who knows!
    email_address = user['email']  # KeyError if missing!
    # ... rest of function
```

**Problems:**

- No clear schema or contract
- Typos in keys cause runtime errors (`user['emial']`)
- No type checking
- Can't use IDE autocomplete

### The Solution: Start with Simple Models

BaseModel gives you a clear, validated schema. Let's start simple:

```python
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    age: int


# Create an instance - validation happens automatically
user = User(name="Alice", email="alice@example.com", age=25)

# Access fields with autocomplete and type checking
print(user.name)  # Alice
print(user.email)  # alice@example.com
print(user.age)  # 25

# Type conversion works automatically
user2 = User(name="Bob", email="bob@example.com", age="30")  # age="30" → 30
print(user2.age)  # 30 (int)
```

**Benefits:**

- ✅ Clear schema - you know exactly what fields exist
- ✅ Type validation - catches errors early
- ✅ IDE autocomplete - `.name`, `.email`, `.age` all work
- ✅ Type conversion - `"30"` becomes `30` automatically

### Building a More Complete Model

Now let's build a more realistic model for managing employee information in an HR system:

```python
from datetime import date
from enum import StrEnum
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, Field


class Department(StrEnum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"


class Employee(BaseModel):
    employee_id: UUID = Field(default_factory=uuid4)
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

### BaseModel Core Methods

Here are the essential methods you'll use when working with BaseModel:

| Method                   | Purpose                          | Example                                        | Returns |
|--------------------------|----------------------------------|------------------------------------------------|---------|
| `Model(**data)`          | Create instance                  | `User(name="Alice", age=25)`                   | Model   |
| `model_validate(data)`   | Create from dict with validation | `User.model_validate({"name": "Alice"})`       | Model   |
| `model_validate_json(s)` | Create from JSON string          | `User.model_validate_json('{"name":"Alice"}')` | Model   |
| `model_dump()`           | Convert to dictionary            | `user.model_dump()`                            | `dict`  |
| `model_dump_json()`      | Convert to JSON string           | `user.model_dump_json(indent=2)`               | `str`   |
| `model_fields`           | Get field definitions            | `User.model_fields`                            | `dict`  |
| `model_json_schema()`    | Generate JSON schema             | `User.model_json_schema()`                     | `dict`  |
| `model_copy()`           | Create a copy                    | `user2 = user.model_copy()`                    | Model   |
| `model_copy(update=...)` | Copy with field updates          | `user.model_copy(update={'age': 26})`          | Model   |

**Common Usage Patterns:**

```python
# Creating instances
user = User(name="Alice", age=25)  # Direct creation
user = User.model_validate({"name": "Alice", "age": 25})  # From dict
user = User.model_validate_json('{"name":"Alice","age":25}')  # From JSON

# Exporting data
data = user.model_dump()  # {'name': 'Alice', 'age': 25}
json_str = user.model_dump_json()  # '{"name":"Alice","age":25}'

# Copying with modifications
updated_user = user.model_copy(update={'age': 26})
```

## Serialization and Deserialization

### The Problem: Manual Dict/JSON Conversion is Tedious

Converting between Python objects, dictionaries, and JSON requires lots of boilerplate:

```python
import json
from datetime import date

# Without Pydantic - manual conversion
employee_dict = {
    "name": "Chris",
    "email": "chris@example.com",
    "date_of_birth": "1998-04-02"
}

# Manual parsing
name = employee_dict['name']
email = employee_dict['email']
date_of_birth = date.fromisoformat(employee_dict['date_of_birth'])  # Manual parsing!


# Serializing back to JSON - need to handle dates manually
def default_serializer(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


json_str = json.dumps(employee_dict, default=default_serializer)
```

**Problems:**

- Manual type conversion for dates, UUIDs, etc.
- Custom serializers for non-JSON types
- No validation during deserialization
- Error-prone key access

### The Solution: Automatic Serialization

Pydantic handles all serialization/deserialization automatically:

**Creating Models From Dictionaries**

```python
from datetime import date
from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    email: str
    date_of_birth: date


# Automatic validation and type conversion
data = {"name": "Chris", "email": "chris@example.com", "date_of_birth": "1998-04-02"}
employee = Employee.model_validate(data)  # Validates and creates model
print(employee.date_of_birth)  # date(1998, 4, 2) - automatically parsed!
```

**Creating Models From JSON**

```python
json_str = '{"name": "Eric", "email": "eric@example.com", "date_of_birth": "2000-01-15"}'
employee = Employee.model_validate_json(json_str)  # Parses and validates JSON
print(type(employee.date_of_birth))  # <class 'datetime.date'>
```

**Serializing to Dict/JSON**

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

**JSON Schema Generation**

```python
# Generate OpenAPI-compatible schema for documentation
schema = Employee.model_json_schema()
```

### Serialization Methods Reference

| Method                  | Returns | Common Parameters                             | Use Case                         |
|-------------------------|---------|-----------------------------------------------|----------------------------------|
| `model_dump()`          | `dict`  | `exclude`, `include`, `exclude_unset`, `mode` | Python dict for internal use     |
| `model_dump_json()`     | `str`   | `exclude`, `include`, `indent`                | JSON string for APIs             |
| `model_validate()`      | Model   | -                                             | Create from dict with validation |
| `model_validate_json()` | Model   | -                                             | Create from JSON string          |
| `model_json_schema()`   | `dict`  | `mode`, `ref_template`                        | Generate JSON schema for docs    |

## Using Fields for Customization

### The Problem: Basic Type Annotations Aren't Enough

Type hints alone can't express all validation requirements:

```python
class Employee(BaseModel):
    name: str  # What if name is empty string ""?
    salary: float  # What if salary is negative?
    email: str  # What if it's not a valid email?
    age: int  # What if age is 500?


# These all pass validation, but shouldn't!
bad_employee = Employee(
    name="",  # Empty name allowed
    salary=-5000,  # Negative salary allowed
    email="not-email",  # Invalid email allowed
    age=999  # Unrealistic age allowed
)
```

**Problems:**

- No way to enforce constraints (min/max values, string length)
- Can't make fields immutable
- No way to use alternative field names (aliases)
- Can't control serialization behavior

### The Solution: Use Field() for Fine-Grained Control

The `Field()` function lets you add validation constraints and metadata:

```python
from pydantic import BaseModel, Field


class Employee(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    salary: float = Field(gt=0, description="Annual salary in USD")
    email: str = Field(pattern=r".+@.+\..+")
    age: int = Field(ge=18, le=100)


# Now validation is enforced!
Employee(name="", salary=-5000, email="bad", age=999)
# ValidationError: 4 validation errors
```

**Advanced Field Usage**

```python
from uuid import UUID, uuid4
from pydantic import Field


class Employee(BaseModel):
    employee_id: UUID = Field(default_factory=uuid4, frozen=True)
    name: str = Field(min_length=1, frozen=True)
    date_of_birth: date = Field(alias="birth_date", repr=False)
    salary: float = Field(alias="compensation", gt=0, repr=False)
```

**Using Aliases and Frozen Fields:**

```python
# Accept 'birth_date' or 'compensation' as input
data = {"birth_date": "2000-06-12", "compensation": 100_000, ...}
employee = Employee.model_validate(data)

# Frozen fields cannot be changed
employee.department = "HR"  # OK
employee.name = "New Name"  # Error: Field is frozen
```

**Common Constraint Examples:**

```python
class Product(BaseModel):
    sku: str = Field(pattern=r'^[A-Z]{3}-\d{4}$')
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0, multiple_of=0.01)
    quantity: int = Field(ge=0, description="Items in stock")
```

### Field Parameters & Constraints Reference

| Parameter/Constraint    | Applies To     | Description                         | Example                                |
|-------------------------|----------------|-------------------------------------|----------------------------------------|
| **Configuration**       |                |                                     |                                        |
| `default`               | All            | Default value                       | `Field(default=0)`                     |
| `default_factory`       | All            | Callable for default values         | `Field(default_factory=list)`          |
| `alias`                 | All            | Alternative field name for input    | `Field(alias='birth_date')`            |
| `frozen`                | All            | Immutable after creation            | `Field(frozen=True)`                   |
| `exclude`               | All            | Exclude from serialization          | `Field(exclude=True)`                  |
| `repr`                  | All            | Show in string representation       | `Field(repr=False)`                    |
| `strict`                | All            | Disable type coercion               | `Field(strict=True)`                   |
| **Documentation**       |                |                                     |                                        |
| `description`           | All            | Documentation for field             | `Field(description='User email')`      |
| `examples`              | All            | Example values for docs             | `Field(examples=['user@example.com'])` |
| `title`                 | All            | Field title for schema              | `Field(title='Email Address')`         |
| **Numeric Constraints** |                |                                     |                                        |
| `gt`                    | Numbers        | Greater than                        | `Field(gt=0)`                          |
| `ge`                    | Numbers        | Greater than or equal               | `Field(ge=0)`                          |
| `lt`                    | Numbers        | Less than                           | `Field(lt=100)`                        |
| `le`                    | Numbers        | Less than or equal                  | `Field(le=100)`                        |
| `multiple_of`           | Numbers        | Must be multiple of value           | `Field(multiple_of=0.01)`              |
| `allow_inf_nan`         | Floats         | Allow infinity/NaN                  | `Field(allow_inf_nan=True)`            |
| **String/List**         |                |                                     |                                        |
| `min_length`            | Strings, Lists | Minimum length                      | `Field(min_length=1)`                  |
| `max_length`            | Strings, Lists | Maximum length                      | `Field(max_length=100)`                |
| `pattern`               | Strings        | Regex pattern match                 | `Field(pattern=r'^[A-Z]{3}$')`         |
| **Decimal Constraints** |                |                                     |                                        |
| `max_digits`            | Decimals       | Maximum total digits                | `Field(max_digits=5)`                  |
| `decimal_places`        | Decimals       | Maximum decimal places              | `Field(decimal_places=2)`              |
| **Advanced**            |                |                                     |                                        |
| `discriminator`         | Unions         | Field for union type discrimination | `Field(discriminator='type')`          |
| `json_schema_extra`     | All            | Additional JSON schema metadata     | `Field(json_schema_extra={...})`       |

## Special Types for Common Validations

### The Problem: Repetitive Validation Logic

Certain validations are so common that writing them manually every time is tedious:

```python
from pydantic import BaseModel, Field
import re


class Contact(BaseModel):
    email: str = Field(pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    website: str = Field(pattern=r'^https?://.*')
    # ... complex regex patterns everywhere!

# Validating emails, URLs, UUIDs, etc. requires complex regex or custom code
```

**Problems:**

- Writing regex patterns for emails, URLs, UUIDs is error-prone
- Repeating the same validation logic across multiple models
- Easy to make mistakes in validation patterns
- No built-in validation for paths, IP addresses, etc.

### The Solution: Use Pydantic's Special Types

Pydantic provides pre-built types for common validations:

```python
from pydantic import BaseModel, EmailStr, HttpUrl, IPvAnyAddress, PositiveFloat
from uuid import UUID
from pathlib import Path


class Contact(BaseModel):
    email: EmailStr  # Auto-validates email format
    website: HttpUrl  # Auto-validates URL
    user_id: UUID  # Auto-validates UUID format
    ip_address: IPvAnyAddress  # Auto-validates IPv4/IPv6
    score: PositiveFloat  # Must be > 0


# All validation happens automatically!
contact = Contact(
    email="user@example.com",
    website="https://example.com",
    user_id="123e4567-e89b-12d3-a456-426614174000",
    ip_address="192.168.1.1",
    score=95.5
)
```

**More Examples:**

```python
from pydantic import (
    BaseModel, EmailStr, HttpUrl, FilePath, DirectoryPath,
    PositiveInt, NegativeInt, PositiveFloat, SecretStr
)


class AppConfig(BaseModel):
    # URLs and emails
    api_endpoint: HttpUrl
    admin_email: EmailStr

    # File system
    config_file: FilePath  # Must exist
    data_dir: DirectoryPath  # Must exist and be a directory

    # Numeric constraints
    max_connections: PositiveInt  # > 0
    temperature_offset: NegativeInt  # < 0
    price: PositiveFloat  # > 0.0

    # Security
    api_key: SecretStr  # Hidden in repr and logs
```

### Special Types Reference

| Type               | Validates                | Example Usage                |
|--------------------|--------------------------|------------------------------|
| **String Types**   |                          |                              |
| `EmailStr`         | Valid email format       | `email: EmailStr`            |
| `AnyUrl`           | Any valid URL            | `link: AnyUrl`               |
| `HttpUrl`          | Valid HTTP/HTTPS URL     | `website: HttpUrl`           |
| `AnyHttpUrl`       | Any HTTP URL scheme      | `endpoint: AnyHttpUrl`       |
| `FileUrl`          | File:// URL              | `local: FileUrl`             |
| `SecretStr`        | String hidden in repr    | `password: SecretStr`        |
| `SecretBytes`      | Bytes hidden in repr     | `token: SecretBytes`         |
| **Numeric Types**  |                          |                              |
| `PositiveInt`      | Integer > 0              | `count: PositiveInt`         |
| `NegativeInt`      | Integer < 0              | `deficit: NegativeInt`       |
| `NonNegativeInt`   | Integer >= 0             | `quantity: NonNegativeInt`   |
| `NonPositiveInt`   | Integer <= 0             | `loss: NonPositiveInt`       |
| `PositiveFloat`    | Float > 0                | `price: PositiveFloat`       |
| `NegativeFloat`    | Float < 0                | `temp: NegativeFloat`        |
| `NonNegativeFloat` | Float >= 0               | `amount: NonNegativeFloat`   |
| `NonPositiveFloat` | Float <= 0               | `offset: NonPositiveFloat`   |
| **File System**    |                          |                              |
| `FilePath`         | Existing file path       | `config: FilePath`           |
| `DirectoryPath`    | Existing directory       | `data_dir: DirectoryPath`    |
| `NewPath`          | Path that doesn't exist  | `output: NewPath`            |
| **Network**        |                          |                              |
| `IPvAnyAddress`    | IPv4 or IPv6 address     | `ip: IPvAnyAddress`          |
| `IPvAnyInterface`  | IPv4/IPv6 interface      | `interface: IPvAnyInterface` |
| `IPvAnyNetwork`    | IPv4/IPv6 network        | `network: IPvAnyNetwork`     |
| **Other**          |                          |                              |
| `UUID`             | Valid UUID (any version) | `id: UUID`                   |
| `UUID1`            | UUID version 1           | `id: UUID1`                  |
| `UUID3`            | UUID version 3           | `id: UUID3`                  |
| `UUID4`            | UUID version 4           | `id: UUID4`                  |
| `UUID5`            | UUID version 5           | `id: UUID5`                  |
| `Json`             | JSON-encoded string      | `data: Json`                 |
| `Base64Str`        | Base64-encoded string    | `encoded: Base64Str`         |
| `Base64Bytes`      | Base64-encoded bytes     | `encoded: Base64Bytes`       |

**Note:** `EmailStr` requires additional dependencies. Install with: `uv add pydantic[email]`

## Custom Validators

### The Problem: Business Logic Validation Needs

Field constraints can't express complex business rules:

```python
class Employee(BaseModel):
    date_of_birth: date
    salary: float
    department: str
    elected_benefits: bool


# Field constraints can't validate:
# - Is the employee at least 18 years old?
# - Does salary match department standards?
# - Are benefits eligibility rules followed?

# These pass validation but violate business rules:
Employee(
    date_of_birth=date(2020, 1, 1),  # 4 years old!
    salary=20_000,
    department="IT",
    elected_benefits=True  # IT contractors shouldn't have benefits
)
```

**Problems:**

- Field constraints can't express cross-field logic
- No way to validate relationships between fields
- Business rules often require complex calculations
- Standard validators can't handle context-dependent validation

### The Solution: Custom Validators

Pydantic provides decorators for custom validation logic:

**Field Validators** - Validate individual fields:

```python
from pydantic import BaseModel, field_validator
from datetime import date


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


# Now business rules are enforced!
Employee(date_of_birth=date(2020, 1, 1))  # ValidationError: must be 18+
```

**Model Validators** - Validate across multiple fields:

```python
from pydantic import model_validator
from typing import Self


class Employee(BaseModel):
    department: str
    elected_benefits: bool
    salary: float

    @model_validator(mode='after')
    def check_business_rules(self) -> Self:
        """Validate business rules across fields."""
        # IT contractors don't get benefits
        if self.department == "IT" and self.elected_benefits:
            raise ValueError("IT employees don't qualify for benefits")

        # Minimum salary by department
        min_salary = {"HR": 50_000, "IT": 70_000, "SALES": 45_000}
        if self.salary < min_salary.get(self.department, 40_000):
            raise ValueError(f"{self.department} salary must be >= {min_salary[self.department]}")

        return self
```

**Validating Function Arguments:**

```python
from pydantic import validate_call, EmailStr, PositiveFloat


@validate_call
def send_invoice(
        client_name: str,
        client_email: EmailStr,
        amount_owed: PositiveFloat,
) -> str:
    return f"Invoice sent to {client_email} for ${amount_owed}"


# Automatic validation on function calls
send_invoice("John", "john@example.com", 100.0)  # ✓ OK
send_invoice("", "invalid", -10)  # ✗ ValidationError
```

### Validator Modes & Decorators Reference

| Decorator           | Scope           | When to Use                            | Example                           |
|---------------------|-----------------|----------------------------------------|-----------------------------------|
| `@field_validator`  | Single field(s) | Validate one or more fields            | `@field_validator('email')`       |
| `@model_validator`  | Entire model    | Cross-field validation, business logic | `@model_validator(mode='after')`  |
| `@validate_call`    | Function args   | Validate function arguments            | `@validate_call`                  |
| `@field_serializer` | Single field    | Custom serialization for a field       | `@field_serializer('created_at')` |

**Validation Modes:**

| Mode       | Timing                                | Input Type              | Use Case                                   |
|------------|---------------------------------------|-------------------------|--------------------------------------------|
| `'before'` | Before Pydantic's validation          | Raw input (any type)    | Pre-process data, normalize inputs         |
| `'after'`  | After Pydantic's validation (default) | Parsed type (e.g. date) | Validate parsed data, business logic       |
| `'wrap'`   | Wraps Pydantic's validation           | Validator + handler     | Control validation flow, conditional logic |

**Multiple Field Validation:**

```python
class User(BaseModel):
    password: str
    password_confirm: str

    @field_validator('password', 'password_confirm')
    @classmethod
    def passwords_match(cls, v: str, info) -> str:
        # Validate both password fields
        if 'password' in info.data and v != info.data['password']:
            raise ValueError('Passwords must match')
        return v
```

## Model Configuration

### The Problem: Default Behavior Doesn't Fit All Use Cases

Pydantic's defaults are permissive, which isn't always what you want:

```python
class User(BaseModel):
    id: int
    name: str


# Default behavior allows:
user = User(id=1, name="Alice", extra_field="ignored")  # Extra fields silently ignored
user.name = "   Bob   "  # Whitespace not stripped
user.id = "invalid"  # Type coercion might allow unexpected values
```

**Problems:**

- Extra fields are silently ignored (can hide typos)
- Type coercion can be too permissive
- Models are mutable by default
- No validation when updating fields after creation
- Whitespace in strings isn't handled

### The Solution: Configure Model Behavior

Use `model_config` with `ConfigDict` to control validation behavior:

```python
from pydantic import BaseModel, ConfigDict


class StrictUser(BaseModel):
    model_config = ConfigDict(
        frozen=True,  # Immutable after creation
        extra='forbid',  # Raise error on extra fields
        validate_assignment=True,  # Validate when updating fields
        str_strip_whitespace=True,  # Auto-strip whitespace
        strict=True,  # Disable type coercion
    )
    id: int
    name: str


# Now strict validation is enforced
user = StrictUser(id=1, name="  Alice  ")  # name becomes "Alice"
user.name = "Bob"  # Error: model is frozen
StrictUser(id=1, name="Alice", typo="oops")  # Error: extra field not allowed
```

**Common Configuration Patterns:**

```python
# API request models - strict validation
class CreateUserRequest(BaseModel):
    model_config = ConfigDict(
        extra='forbid',  # No extra fields
        str_strip_whitespace=True  # Clean input
    )


# Internal domain models - immutable
class User(BaseModel):
    model_config = ConfigDict(
        frozen=True,  # Immutable
        validate_assignment=True  # Validate updates (if unfrozen)
    )


# ORM integration - read from database objects
class UserResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True  # Read from ORM objects
    )
```

### Configuration Options Reference

| Option                 | Description                      | Values                            | Default    |
|------------------------|----------------------------------|-----------------------------------|------------|
| `strict`               | Disable type coercion            | `True` / `False`                  | `False`    |
| `extra`                | Handle extra fields              | `'allow'`, `'forbid'`, `'ignore'` | `'ignore'` |
| `frozen`               | Make model immutable             | `True` / `False`                  | `False`    |
| `validate_assignment`  | Validate on field updates        | `True` / `False`                  | `False`    |
| `from_attributes`      | Enable ORM mode                  | `True` / `False`                  | `False`    |
| `populate_by_name`     | Accept alias or field name       | `True` / `False`                  | `False`    |
| `str_strip_whitespace` | Strip strings                    | `True` / `False`                  | `False`    |
| `str_to_lower`         | Convert strings to lowercase     | `True` / `False`                  | `False`    |
| `str_to_upper`         | Convert strings to uppercase     | `True` / `False`                  | `False`    |
| `use_enum_values`      | Use enum values in serialization | `True` / `False`                  | `False`    |

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

Pydantic supports advanced patterns for complex applications. Here are the key features for building sophisticated data
models.

### Nested Models

**Problem:** Real-world data is hierarchical, not flat.

**Solution:** Nest Pydantic models inside each other:

```python
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class Company(BaseModel):
    name: str
    address: Address  # Nested model
    employees: list[Employee]  # List of nested models


# Dicts are automatically converted to nested models
company = Company(
    name="Tech Corp",
    address={"street": "123 Main St", "city": "NYC", "zip_code": "10001"},
    employees=[{"name": "Alice", ...}, {"name": "Bob", ...}]
)

# Access nested fields naturally
print(company.address.city)  # NYC
```

### Computed Fields

**Problem:** Some fields are derived from others and shouldn't be set directly.

**Solution:** Use `@computed_field` for calculated values:

```python
from pydantic import BaseModel, computed_field


class Rectangle(BaseModel):
    width: float
    height: float

    @computed_field
    @property
    def area(self) -> float:
        return self.width * self.height

    @computed_field
    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


rect = Rectangle(width=5.0, height=3.0)
print(rect.area)  # 15.0 (computed)
print(rect.perimeter)  # 16.0 (computed)

# Computed fields are included in serialization
print(rect.model_dump())  # {'width': 5.0, 'height': 3.0, 'area': 15.0, 'perimeter': 16.0}
```

### Generic Models

**Problem:** Need reusable response models for different data types.

**Solution:** Use generic models with type parameters:

```python
from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar('T')


class Response(BaseModel, Generic[T]):
    data: T
    success: bool = True
    message: str = ""


# Type-safe responses for different data
user_response = Response[User](data=User(id=1, name="Alice"))
users_response = Response[list[User]](data=[User(id=1, name="Alice")])
```

### Union Types

**Problem:** A field can accept multiple different types.

**Solution:** Use union types with optional discriminators:

```python
from pydantic import BaseModel, Field
from typing import Literal


class Cat(BaseModel):
    type: Literal['cat']
    meow_volume: int


class Dog(BaseModel):
    type: Literal['dog']
    bark_volume: int


# Without discriminator - slower, tries each type
class Pet(BaseModel):
    animal: Cat | Dog


# With discriminator - faster, uses 'type' field to choose
class Pet(BaseModel):
    animal: Cat | Dog = Field(discriminator='type')


pet = Pet(animal={"type": "cat", "meow_volume": 5})  # Validated as Cat
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

| Feature           | Pydantic                      | Dataclasses      |
|-------------------|-------------------------------|------------------|
| **Validation**    | Automatic                     | None             |
| **Type Coercion** | Yes                           | No               |
| **JSON Support**  | Built-in                      | Manual           |
| **Performance**   | Slower                        | ~6x faster       |
| **Use Case**      | API boundaries, external data | Internal objects |

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
