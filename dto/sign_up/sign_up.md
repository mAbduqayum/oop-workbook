# SignUp - Pydantic Password Validation

## Exercise: SignUp Model with Password Confirmation

Create a `SignUp` class using Pydantic's `BaseModel` with password validation and confirmation matching.

**Task:**

1. Create a `SignUp` class using `BaseModel` with the following fields:
    - `username: str` - Username (3-20 chars, only alphanumeric and underscores)
    - `email: EmailStr` - Valid email address
    - `password: str` - Password (8-50 chars, must contain uppercase, lowercase, digit, and special char)
    - `confirm_password: str` - Password confirmation
2. Add a model validator to ensure `password` matches `confirm_password`
3. Exclude `confirm_password` from serialization by default

**Example:**

```python
sign_up = SignUp(
    username="john_doe",
    email="john@example.com",
    password="SecurePass123!",
    confirm_password="SecurePass123!"
)
print(sign_up.username)  # john_doe
print(sign_up.model_dump())  # confirm_password not included

# Mismatched passwords raise ValidationError
SignUp(
    username="john_doe",
    email="john@example.com",
    password="SecurePass123!",
    confirm_password="DifferentPass123!"
)  # ValidationError

# Weak password raises ValidationError
SignUp(
    username="john_doe",
    email="john@example.com",
    password="weak",
    confirm_password="weak"
)  # ValidationError
```
