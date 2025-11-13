# Address - Optional Fields and String Formatting

## Exercise: Address Model with Optional Fields

Create an `Address` class using Pydantic's `BaseModel` with optional fields and validation for postal codes.

**Task:**

1. Create an `Address` class using `BaseModel` with the following fields:
    - `street: str` - Street address (1-100 characters)
    - `city: str` - City name (1-50 characters)
    - `state: str` - State/province abbreviation (2 uppercase letters)
    - `zip_code: str` - Postal code (5 digits or 5+4 format: "12345" or "12345-6789")
    - `country: str` - Country code (default: "US", 2 uppercase letters)
    - `apartment: str | None` - Optional apartment/unit number (default: None)
2. Add a `full_address` property that returns the formatted complete address
3. Add a field validator for `zip_code` to ensure it matches US zip code format

**Example:**

```python
address = Address(
    street="123 Main St",
    city="Springfield",
    state="IL",
    zip_code="62701"
)
print(address.full_address)  # 123 Main St, Springfield, IL 62701, US

address_with_apt = Address(
    street="456 Oak Ave",
    apartment="Apt 3B",
    city="Chicago",
    state="IL",
    zip_code="60601-1234"
)
print(address_with_apt.full_address)  # 456 Oak Ave Apt 3B, Chicago, IL 60601-1234, US

# Invalid state raises ValidationError
Address(street="123 Main", city="Springfield", state="Illinois", zip_code="62701")  # ValidationError

# Invalid zip code raises ValidationError
Address(street="123 Main", city="Springfield", state="IL", zip_code="1234")  # ValidationError
```
