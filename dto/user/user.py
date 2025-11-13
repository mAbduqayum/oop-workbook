from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: UUID
    username: str = Field(min_length=3, max_length=20, pattern=r"^\w+$")
    email: EmailStr
    age: int = Field(ge=18)
    is_active: bool = True


if __name__ == "__main__":
    from uuid import uuid4

    user = User(id=uuid4(), username="john_doe", email="john@example.com", age=25)
    print(user.username)
    print(user.model_dump())

    json_str = user.model_dump_json()
    user2 = User.model_validate_json(json_str)
    print(user2)
