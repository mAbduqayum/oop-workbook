from uuid import UUID

from pydantic import BaseModel, Field

from ..category.category import Category


class Product(BaseModel):
    id: UUID
    name: str = Field(min_length=1, max_length=50)
    price: float = Field(gt=0, multiple_of=0.01)
    quantity: int = Field(ge=0)
    categories: list[Category]


if __name__ == "__main__":
    from uuid import uuid4

    electronics = Category(id=1, name="Electronics")
    computers = Category(id=2, name="Computers")

    product = Product(
        id=uuid4(),
        name="Laptop",
        price=999.99,
        quantity=10,
        categories=[electronics, computers],
    )
    print(product.name)
    print(product.categories[0].name)
    print(len(product.categories))

    product2 = Product(
        id=uuid4(),
        name="Mouse",
        price=29.99,
        quantity=5,
        categories=[{"id": 3, "name": "Accessories"}],
    )
    print(product2.name)
    print(product2.categories[0].id)

    data = product.model_dump()
    print(data["categories"][0]["name"])
