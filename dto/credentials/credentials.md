# Credentials - Secure Data with SecretStr

## Exercise: Credentials Model with Sensitive Data

Create a `Credentials` class using Pydantic's `BaseModel` with `SecretStr` for handling sensitive data securely.

**Task:**

1. Create a `Credentials` class using `BaseModel` with the following fields:
    - `username: str` - Username (3-20 chars, alphanumeric and underscores)
    - `password: SecretStr` - Password (sensitive data)
    - `api_key: SecretStr` - API key (sensitive data)
2. Ensure that when serialized, sensitive fields are hidden by default
3. Access actual values using the `get_secret_value()` method provided by `SecretStr`

**Example:**

```python
from pydantic import SecretStr

creds = Credentials(
    username="admin",
    password="MySecurePassword123!",
    api_key="sk_test_1234567890abcdef"
)

print(creds.username)  # admin
print(creds.password)  # SecretStr('**********')
print(creds.api_key)  # SecretStr('**********')

# Access actual values
print(creds.password.get_secret_value())  # MySecurePassword123!
print(creds.api_key.get_secret_value())  # sk_test_1234567890abcdef

# Serialization hides secrets
data = creds.model_dump()
print(data['password'])  # **********
print(data['api_key'])  # **********

# JSON also hides secrets
json_str = creds.model_dump_json()
print(json_str)  # {"username":"admin","password":"**********","api_key":"**********"}
```

**Key Benefits:**

- `SecretStr` prevents accidental exposure in logs and error messages
- Secrets are masked in string representation and serialization
- Actual values accessible only through explicit method calls
