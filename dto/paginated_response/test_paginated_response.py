from uuid import uuid4

import pytest
from pydantic import BaseModel, ValidationError

from dto.category.category import Category
from dto.paginated_response.paginated_response import PaginatedResponse
from dto.product.product import Product


class User(BaseModel):
    id: int
    name: str


def test_valid_paginated_response():
    cat = Category(id=1, name="Electronics")
    products = [
        Product(
            id=uuid4(),
            name="Laptop",
            price=999.99,
            quantity=10,
            categories=[cat],
        ),
        Product(
            id=uuid4(),
            name="Mouse",
            price=29.99,
            quantity=50,
            categories=[cat],
        ),
    ]
    response = PaginatedResponse[Product](items=products, total=10, page=1, page_size=2)

    assert len(response.items) == 2
    assert response.total == 10
    assert response.page == 1
    assert response.page_size == 2


def test_total_pages_calculation():
    response = PaginatedResponse[Product](items=[], total=10, page=1, page_size=3)
    assert response.total_pages == 4

    response = PaginatedResponse[Product](items=[], total=10, page=1, page_size=2)
    assert response.total_pages == 5

    response = PaginatedResponse[Product](items=[], total=10, page=1, page_size=10)
    assert response.total_pages == 1


def test_total_pages_empty():
    response = PaginatedResponse[Product](items=[], total=0, page=1, page_size=10)
    assert response.total_pages == 0


def test_has_next_property():
    response = PaginatedResponse[Product](items=[], total=10, page=1, page_size=5)
    assert response.has_next is True

    response = PaginatedResponse[Product](items=[], total=10, page=2, page_size=5)
    assert response.has_next is False

    response = PaginatedResponse[Product](items=[], total=0, page=1, page_size=10)
    assert response.has_next is False


def test_invalid_total():
    with pytest.raises(ValidationError):
        PaginatedResponse[Product](items=[], total=-1, page=1, page_size=10)


def test_invalid_page():
    with pytest.raises(ValidationError):
        PaginatedResponse[Product](items=[], total=10, page=0, page_size=10)

    with pytest.raises(ValidationError):
        PaginatedResponse[Product](items=[], total=10, page=-1, page_size=10)


def test_invalid_page_size():
    with pytest.raises(ValidationError):
        PaginatedResponse[Product](items=[], total=10, page=1, page_size=0)

    with pytest.raises(ValidationError):
        PaginatedResponse[Product](items=[], total=10, page=1, page_size=-1)


def test_generic_with_different_types():
    users = [User(id=1, name="Alice"), User(id=2, name="Bob")]
    response = PaginatedResponse[User](items=users, total=20, page=1, page_size=2)

    assert len(response.items) == 2
    assert response.items[0].name == "Alice"
    assert response.total_pages == 10


def test_serialization():
    cat = Category(id=1, name="Electronics")
    products = [
        Product(
            id=uuid4(),
            name="Laptop",
            price=999.99,
            quantity=10,
            categories=[cat],
        )
    ]
    response = PaginatedResponse[Product](items=products, total=10, page=1, page_size=2)

    data = response.model_dump()
    assert data["items"][0]["name"] == "Laptop"
    assert data["total"] == 10
    assert data["page"] == 1
    assert data["page_size"] == 2


def test_json_serialization():
    cat = Category(id=1, name="Electronics")
    products = [
        Product(id=uuid4(), name="Laptop", price=999.99, quantity=10, categories=[cat])
    ]
    response = PaginatedResponse[Product](items=products, total=10, page=1, page_size=2)

    json_str = response.model_dump_json()
    response2 = PaginatedResponse[Product].model_validate_json(json_str)

    assert response == response2


def test_empty_items_list():
    response = PaginatedResponse[Product](items=[], total=0, page=1, page_size=10)
    assert len(response.items) == 0
    assert response.total == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
