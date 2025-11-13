from pydantic import BaseModel, EmailStr, Field, HttpUrl


class Contact(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    email: EmailStr
    phone: str = Field(pattern=r"^(\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$")
    website: HttpUrl | None = None
    notes: str | None = None
