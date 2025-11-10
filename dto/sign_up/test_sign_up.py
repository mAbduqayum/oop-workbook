import pytest
from pydantic import ValidationError
from sign_up import SignUp


def test_valid_sign_up():
    sign_up = SignUp(
        username="john_doe",
        email="john@example.com",
        password="SecurePass123!",
        confirm_password="SecurePass123!",
    )
    assert sign_up.username == "john_doe"
    assert sign_up.email == "john@example.com"
    assert sign_up.password == "SecurePass123!"


def test_passwords_do_not_match():
    with pytest.raises(ValidationError) as exc_info:
        SignUp(
            username="john_doe",
            email="john@example.com",
            password="SecurePass123!",
            confirm_password="DifferentPass123!",
        )
    assert "Passwords do not match" in str(exc_info.value)


def test_password_missing_uppercase():
    with pytest.raises(ValidationError) as exc_info:
        SignUp(
            username="john_doe",
            email="john@example.com",
            password="securepass123!",
            confirm_password="securepass123!",
        )
    assert "uppercase letter" in str(exc_info.value)


def test_password_missing_lowercase():
    with pytest.raises(ValidationError) as exc_info:
        SignUp(
            username="john_doe",
            email="john@example.com",
            password="SECUREPASS123!",
            confirm_password="SECUREPASS123!",
        )
    assert "lowercase letter" in str(exc_info.value)


def test_password_missing_digit():
    with pytest.raises(ValidationError) as exc_info:
        SignUp(
            username="john_doe",
            email="john@example.com",
            password="SecurePass!",
            confirm_password="SecurePass!",
        )
    assert "digit" in str(exc_info.value)


def test_password_missing_special_char():
    with pytest.raises(ValidationError) as exc_info:
        SignUp(
            username="john_doe",
            email="john@example.com",
            password="SecurePass123",
            confirm_password="SecurePass123",
        )
    assert "special character" in str(exc_info.value)


def test_password_too_short():
    with pytest.raises(ValidationError):
        SignUp(
            username="john_doe",
            email="john@example.com",
            password="Sec1!",
            confirm_password="Sec1!",
        )


def test_invalid_username():
    with pytest.raises(ValidationError):
        SignUp(
            username="ab",
            email="john@example.com",
            password="SecurePass123!",
            confirm_password="SecurePass123!",
        )


def test_invalid_email():
    with pytest.raises(ValidationError):
        SignUp(
            username="john_doe",
            email="invalid-email",
            password="SecurePass123!",
            confirm_password="SecurePass123!",
        )


def test_confirm_password_excluded_from_dump():
    sign_up = SignUp(
        username="john_doe",
        email="john@example.com",
        password="SecurePass123!",
        confirm_password="SecurePass123!",
    )
    data = sign_up.model_dump()
    assert "confirm_password" not in data
    assert "password" in data
    assert "username" in data
    assert "email" in data


def test_json_serialization():
    sign_up = SignUp(
        username="john_doe",
        email="john@example.com",
        password="SecurePass123!",
        confirm_password="SecurePass123!",
    )
    json_str = sign_up.model_dump_json()
    assert "confirm_password" not in json_str


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
