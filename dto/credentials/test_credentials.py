import pytest
from credentials import Credentials
from pydantic import SecretStr, ValidationError


def test_credentials_basic():
    creds = Credentials(
        username="admin",
        password="MySecurePassword123!",
        api_key="sk_test_1234567890abcdef",
    )
    assert creds.username == "admin"
    assert isinstance(creds.password, SecretStr)
    assert isinstance(creds.api_key, SecretStr)


def test_get_password():
    creds = Credentials(
        username="admin",
        password="MySecurePassword123!",
        api_key="sk_test_1234567890abcdef",
    )
    assert creds.password.get_secret_value() == "MySecurePassword123!"


def test_get_api_key():
    creds = Credentials(
        username="admin",
        password="MySecurePassword123!",
        api_key="sk_test_1234567890abcdef",
    )
    assert creds.api_key.get_secret_value() == "sk_test_1234567890abcdef"


def test_password_repr_hidden():
    creds = Credentials(
        username="admin",
        password="MySecurePassword123!",
        api_key="sk_test_1234567890abcdef",
    )
    password_repr = repr(creds.password)
    assert "**********" in password_repr or "SecretStr" in password_repr
    assert "MySecurePassword123!" not in password_repr


def test_api_key_repr_hidden():
    creds = Credentials(
        username="admin",
        password="MySecurePassword123!",
        api_key="sk_test_1234567890abcdef",
    )
    api_key_repr = repr(creds.api_key)
    assert "**********" in api_key_repr or "SecretStr" in api_key_repr
    assert "sk_test_1234567890abcdef" not in api_key_repr


def test_serialization_hides_password():
    creds = Credentials(
        username="admin",
        password="MySecurePassword123!",
        api_key="sk_test_1234567890abcdef",
    )
    data = creds.model_dump(mode="json")
    assert data["username"] == "admin"
    assert data["password"] == "**********"
    assert data["api_key"] == "**********"


def test_json_serialization_hides_secrets():
    creds = Credentials(
        username="admin",
        password="MySecurePassword123!",
        api_key="sk_test_1234567890abcdef",
    )
    json_str = creds.model_dump_json()
    assert "admin" in json_str
    assert "**********" in json_str
    assert "MySecurePassword123!" not in json_str
    assert "sk_test_1234567890abcdef" not in json_str


def test_invalid_username_too_short():
    with pytest.raises(ValidationError):
        Credentials(
            username="ab",
            password="MySecurePassword123!",
            api_key="sk_test_1234567890abcdef",
        )


def test_invalid_username_too_long():
    with pytest.raises(ValidationError):
        Credentials(
            username="a" * 21,
            password="MySecurePassword123!",
            api_key="sk_test_1234567890abcdef",
        )


def test_invalid_username_special_chars():
    with pytest.raises(ValidationError):
        Credentials(
            username="user@name",
            password="MySecurePassword123!",
            api_key="sk_test_1234567890abcdef",
        )


def test_valid_username_with_underscore():
    creds = Credentials(
        username="user_name",
        password="MySecurePassword123!",
        api_key="sk_test_1234567890abcdef",
    )
    assert creds.username == "user_name"


def test_valid_username_with_numbers():
    creds = Credentials(
        username="user123",
        password="MySecurePassword123!",
        api_key="sk_test_1234567890abcdef",
    )
    assert creds.username == "user123"
