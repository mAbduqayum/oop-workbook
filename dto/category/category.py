from __future__ import annotations

from pydantic import BaseModel, Field


class Category(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1, max_length=50)
    subcategories: list[Category] = Field(default_factory=list)


if __name__ == "__main__":
    electronics = Category(id=1, name="Electronics")
    print(electronics.name)
    print(electronics.subcategories)

    computers = Category(
        id=2,
        name="Computers",
        subcategories=[
            Category(id=3, name="Laptops"),
            Category(id=4, name="Desktops"),
        ],
    )
    print(len(computers.subcategories))

    root = Category(
        id=1,
        name="Electronics",
        subcategories=[
            Category(
                id=2,
                name="Computers",
                subcategories=[
                    Category(id=3, name="Laptops"),
                    Category(id=4, name="Desktops"),
                ],
            ),
            Category(id=5, name="Phones"),
        ],
    )

    data = root.model_dump()
    print(data["subcategories"][0]["name"])
    print(data["subcategories"][0]["subcategories"][0]["name"])
