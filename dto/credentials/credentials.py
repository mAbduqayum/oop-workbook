from pydantic import BaseModel, Field, SecretStr


class Credentials(BaseModel):
    username: str = Field(min_length=3, max_length=20, pattern=r"^\w+$")
    password: SecretStr
    api_key: SecretStr
