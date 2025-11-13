from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing_extensions import Self


class SignUp(BaseModel):
    username: str = Field(min_length=3, max_length=20, pattern=r"^\w+$")
    email: EmailStr
    password: str = Field(min_length=8, max_length=50)
    confirm_password: str = Field(exclude=True)

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.islower() for c in v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")
        if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in v):
            raise ValueError("Password must contain at least one special character")
        return v

    @model_validator(mode="after")
    def validate_passwords_match(self) -> Self:
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self


if __name__ == "__main__":
    sign_up = SignUp(
        username="john_doe",
        email="john@example.com",
        password="SecurePass123!",
        confirm_password="SecurePass123!",
    )
    print(f"Username: {sign_up.username}")
    print(f"Email: {sign_up.email}")
    print(f"Model dump: {sign_up.model_dump()}")
