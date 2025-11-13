from __future__ import annotations

from math import ceil
from uuid import UUID

from pydantic import BaseModel, Field

from ..product.product import Product


class PaginatedResponse[T](BaseModel):
    items: list[T]
    total: int = Field(ge=0)
    page: int = Field(ge=1)
    page_size: int = Field(ge=1)

    @property
    def total_pages(self) -> int:
        """Calculate the total number of pages."""
        if self.total == 0:
            return 0
        return ceil(self.total / self.page_size)

    @property
    def has_next(self) -> bool:
        """Check if there's a next page."""
        return self.page < self.total_pages


if __name__ == "__main__":
    from uuid import uuid4

    from ..category.category import Category

    electronics = Category(id=1, name="Electronics")

    products = [
        Product(
            id=uuid4(),
            sku="LAP-1000",
            name="Laptop",
            price=999.99,
            quantity=10,
            categories=[electronics],
        ),
        Product(
            id=uuid4(),
            sku="MOU-2000",
            name="Mouse",
            price=29.99,
            quantity=50,
            categories=[electronics],
        ),
    ]

    response = PaginatedResponse[Product](items=products, total=10, page=1, page_size=2)

    print(f"Page {response.page} of {response.total_pages}")
    print(f"Has next page: {response.has_next}")
    print(f"Items: {len(response.items)}")

    for product in response.items:
        print(f"  - {product.name}: ${product.price}")
