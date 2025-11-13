from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str = Field(min_length=1, max_length=100)
    city: str = Field(min_length=1, max_length=50)
    state: str = Field(pattern=r"^[A-Z]{2}$")
    zip_code: str = Field(pattern=r"^\d{5}(-\d{4})?$")
    country: str = Field(default="US", pattern=r"^[A-Z]{2}$")
    apartment: str | None = None

    @property
    def full_address(self) -> str:
        parts = [self.street]
        if self.apartment:
            parts.append(self.apartment)
        parts.append(f"{self.city}, {self.state} {self.zip_code}, {self.country}")
        return " ".join(parts)
