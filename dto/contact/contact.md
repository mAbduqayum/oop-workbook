# Contact - Phone and URL Validation

## Exercise: Contact Model with Multiple Validators

Create a `Contact` class using Pydantic's `BaseModel` with phone number and URL validation.

**Task:**

1. Create a `Contact` class using `BaseModel` with the following fields:
    - `name: str` - Contact name (1-50 characters)
    - `email: EmailStr` - Valid email address
    - `phone: str` - Phone number (format: XXX-XXX-XXXX or (XXX) XXX-XXXX)
    - `website: HttpUrl | None` - Optional website URL (default: None)
    - `notes: str | None` - Optional notes (default: None)
2. Add a field validator for `phone` to ensure it matches US phone format

**Example:**

```python
from pydantic import EmailStr, HttpUrl

contact = Contact(
    name="John Doe",
    email="john@example.com",
    phone="555-123-4567"
)
print(contact.name)  # John Doe
print(contact.phone)  # 555-123-4567

contact_with_website = Contact(
    name="Jane Smith",
    email="jane@example.com",
    phone="(555) 987-6543",
    website="https://example.com",
    notes="Met at conference"
)
print(contact_with_website.website)  # https://example.com/

# Invalid phone format raises ValidationError
Contact(
    name="Bob",
    email="bob@example.com",
    phone="555.123.4567"
)  # ValidationError

# Invalid email raises ValidationError
Contact(
    name="Bob",
    email="not-an-email",
    phone="555-123-4567"
)  # ValidationError
```
