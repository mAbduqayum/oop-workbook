# 🔐 Python OOP Practice - Lesson 23: Password Class

## 📝 Exercise: Secure Password Management with Validation

Create a `Password` class that securely manages passwords with strength validation and requirement checking. This demonstrates security-related encapsulation and data protection.

**Instructions:**
Implement a password manager that validates password strength and enforces security requirements.

The password should be stored securely and only accessible through controlled methods.

Password strength should be automatically calculated based on multiple criteria.

**Your Complete Task:**
1. Create a `Password` class that takes a password string in the constructor
2. Store the password privately with underscore prefix (`_password`)
3. Add validation for minimum requirements:
   - At least 8 characters long
   - Contains at least one uppercase letter
   - Contains at least one lowercase letter
   - Contains at least one digit
   - Contains at least one special character (!@#$%^&*)
4. Add a `strength` property that returns "Weak", "Medium", or "Strong" based on criteria
5. Add a `check_password(input_password)` method that returns True if input matches stored password
6. Add a `change_password(old_password, new_password)` method that validates old password before changing
7. Raise `ValueError` for invalid passwords with descriptive messages
8. Never expose the actual password - only provide validation methods

**What You'll Learn:**
- **Security Encapsulation:** Protecting sensitive data from direct access
- **Input Validation:** Comprehensive password requirement checking
- **Property Decorators:** Computing values based on private data
- **Error Handling:** Using exceptions for invalid input
- **Authentication Patterns:** Secure password verification methods

**Strength Criteria:**
- **Medium:** Meets minimum requirements (8-11 chars with all character types)
- **Strong:** Length ≥ 12 with all character types

**Example Usage:**
```python
# Valid password creation
password = Password("MyP@ssw0rd123")
print(password.strength)  # "Strong"

# Check password
print(password.check_password("MyP@ssw0rd123"))  # True
print(password.check_password("wrong"))          # False

# Change password
password.change_password("MyP@ssw0rd123", "NewP@ss2024!")
print(password.check_password("NewP@ss2024!"))   # True

# Invalid password (should raise ValueError)
try:
    weak_password = Password("123")  # Too short, no letters/special chars
except ValueError as e:
    print(e)  # "Password must be at least 8 characters long"

# Strength examples
medium = Password("Passw0rd!")      # "Medium" - 9 chars with all types
strong = Password("MyStr0ng!Pass") # "Strong" - 12+ chars with all character types
```

**Security Note:**
In real applications, passwords should be hashed, not stored as plain text. This exercise focuses on encapsulation concepts rather than production security practices.