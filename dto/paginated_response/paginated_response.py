from __future__ import annotations

from math import ceil

from pydantic import BaseModel, Field


class PaginatedResponse[T](BaseModel):
    items: list[T]
    total: int = Field(ge=0)
    page: int = Field(ge=1)
    page_size: int = Field(ge=1)

    @property
    def total_pages(self) -> int:
        if self.total == 0:
            return 0
        return ceil(self.total / self.page_size)

    @property
    def has_next(self) -> bool:
        return self.page < self.total_pages


if __name__ == "__main__":
    from pydantic import BaseModel

    class Product(BaseModel):
        id: int
        name: str
        price: float

    products = [
        Product(id=1, name="Laptop", price=999.99),
        Product(id=2, name="Mouse", price=29.99),
    ]

    response = PaginatedResponse[Product](items=products, total=10, page=1, page_size=2)

    print(response.total_pages)  # 5
    print(response.has_next)  # True
