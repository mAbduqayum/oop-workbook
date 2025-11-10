import pytest
from category import Category
from pydantic import ValidationError


def test_simple_category():
    category = Category(id=1, name="Electronics")
    assert category.id == 1
    assert category.name == "Electronics"
    assert category.subcategories == []


def test_category_with_subcategories():
    category = Category(
        id=1,
        name="Electronics",
        subcategories=[
            Category(id=2, name="Computers"),
            Category(id=3, name="Phones"),
        ],
    )
    assert len(category.subcategories) == 2
    assert category.subcategories[0].name == "Computers"
    assert category.subcategories[1].name == "Phones"


def test_deeply_nested_categories():
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
    assert root.subcategories[0].subcategories[0].name == "Laptops"


def test_invalid_id():
    with pytest.raises(ValidationError):
        Category(id=0, name="Electronics")
    with pytest.raises(ValidationError):
        Category(id=-1, name="Electronics")


def test_invalid_name():
    with pytest.raises(ValidationError):
        Category(id=1, name="")
    with pytest.raises(ValidationError):
        Category(id=1, name="a" * 51)


def test_serialization():
    category = Category(
        id=1,
        name="Electronics",
        subcategories=[Category(id=2, name="Computers")],
    )
    data = category.model_dump()
    assert data["id"] == 1
    assert data["name"] == "Electronics"
    assert len(data["subcategories"]) == 1
    assert data["subcategories"][0]["name"] == "Computers"


def test_json_serialization():
    category = Category(
        id=1,
        name="Electronics",
        subcategories=[Category(id=2, name="Computers")],
    )
    json_str = category.model_dump_json()
    category2 = Category.model_validate_json(json_str)
    assert category == category2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
