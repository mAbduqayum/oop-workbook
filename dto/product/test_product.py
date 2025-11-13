from uuid import uuid4

import pytest
from pydantic import ValidationError

from dto.category.category import Category
from dto.product.product import Product


def test_valid_product():
    electronics = Category(id=1, name="Electronics")
    product = Product(
        id=uuid4(),
        name="Laptop",
        price=999.99,
        quantity=10,
        categories=[electronics],
    )
    assert product.name == "Laptop"
    assert product.price == 999.99
    assert product.quantity == 10
    assert len(product.categories) == 1
    assert product.categories[0].name == "Electronics"


def test_valid_product_with_multiple_categories():
    electronics = Category(id=1, name="Electronics")
    computers = Category(id=2, name="Computers")
    product = Product(
        id=uuid4(),
        name="Laptop",
        price=999.99,
        quantity=10,
        categories=[electronics, computers],
    )
    assert len(product.categories) == 2
    assert product.categories[0].name == "Electronics"
    assert product.categories[1].name == "Computers"


def test_valid_product_with_dict_categories():
    product = Product(
        id=uuid4(),
        name="Laptop",
        price=999.99,
        quantity=10,
        categories=[{"id": 1, "name": "Electronics"}],
    )
    assert len(product.categories) == 1
    assert product.categories[0].id == 1


def test_invalid_name_length():
    cat = Category(id=1, name="Electronics")
    with pytest.raises(ValidationError):
        Product(
            id=uuid4(),
            name="",
            price=999.99,
            quantity=10,
            categories=[cat],
        )
    with pytest.raises(ValidationError):
        Product(
            id=uuid4(),
            name="a" * 51,
            price=999.99,
            quantity=10,
            categories=[cat],
        )


def test_invalid_price():
    cat = Category(id=1, name="Electronics")
    with pytest.raises(ValidationError):
        Product(
            id=uuid4(),
            name="Laptop",
            price=0,
            quantity=10,
            categories=[cat],
        )
    with pytest.raises(ValidationError):
        Product(
            id=uuid4(),
            name="Laptop",
            price=-10,
            quantity=10,
            categories=[cat],
        )
    with pytest.raises(ValidationError):
        Product(
            id=uuid4(),
            name="Laptop",
            price=10.001,
            quantity=10,
            categories=[cat],
        )


def test_invalid_quantity():
    cat = Category(id=1, name="Electronics")
    with pytest.raises(ValidationError):
        Product(
            id=uuid4(),
            name="Laptop",
            price=999.99,
            quantity=-1,
            categories=[cat],
        )


def test_json_serialization():
    electronics = Category(id=1, name="Electronics")
    product = Product(
        id=uuid4(),
        name="Laptop",
        price=999.99,
        quantity=10,
        categories=[electronics],
    )
    json_str = product.model_dump_json()
    product2 = Product.model_validate_json(json_str)
    assert product == product2


def test_serialization_includes_categories():
    electronics = Category(id=1, name="Electronics")
    product = Product(
        id=uuid4(),
        name="Laptop",
        price=999.99,
        quantity=10,
        categories=[electronics],
    )
    data = product.model_dump()
    assert "categories" in data
    assert len(data["categories"]) == 1
    assert data["categories"][0]["name"] == "Electronics"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
