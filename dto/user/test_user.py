from uuid import uuid4

import pytest
from pydantic import ValidationError
from user import User


def test_valid_user():
    user_id = uuid4()
    user = User(id=user_id, username="john_doe", email="john@example.com", age=25)
    assert user.id == user_id
    assert user.username == "john_doe"
    assert user.email == "john@example.com"
    assert user.age == 25
    assert user.is_active is True


def test_default_is_active():
    user = User(id=uuid4(), username="alice", email="alice@example.com", age=30)
    assert user.is_active is True


def test_invalid_username_length():
    with pytest.raises(ValidationError):
        User(id=uuid4(), username="ab", email="john@example.com", age=25)
    with pytest.raises(ValidationError):
        User(id=uuid4(), username="a" * 21, email="john@example.com", age=25)


def test_invalid_username_characters():
    with pytest.raises(ValidationError):
        User(id=uuid4(), username="john@doe", email="john@example.com", age=25)
    with pytest.raises(ValidationError):
        User(id=uuid4(), username="john-doe", email="john@example.com", age=25)
    with pytest.raises(ValidationError):
        User(id=uuid4(), username="john.doe", email="john@example.com", age=25)


def test_invalid_email():
    with pytest.raises(ValidationError):
        User(id=uuid4(), username="john_doe", email="invalid", age=25)
    with pytest.raises(ValidationError):
        User(id=uuid4(), username="john_doe", email="john@", age=25)


def test_invalid_age():
    with pytest.raises(ValidationError):
        User(id=uuid4(), username="john_doe", email="john@example.com", age=17)
    with pytest.raises(ValidationError):
        User(id=uuid4(), username="john_doe", email="john@example.com", age=-1)


def test_serialization():
    user_id = uuid4()
    user = User(id=user_id, username="john_doe", email="john@example.com", age=25)
    data = user.model_dump()
    assert data["id"] == user_id
    assert data["username"] == "john_doe"
    assert data["email"] == "john@example.com"
    assert data["age"] == 25
    assert data["is_active"] is True


def test_json_serialization():
    user = User(id=uuid4(), username="john_doe", email="john@example.com", age=25)
    json_str = user.model_dump_json()
    user2 = User.model_validate_json(json_str)
    assert user == user2


def test_model_validate():
    user_id = uuid4()
    data = {"id": str(user_id), "username": "john_doe", "email": "john@example.com", "age": 25}
    user = User.model_validate(data)
    assert user.id == user_id
    assert user.username == "john_doe"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
