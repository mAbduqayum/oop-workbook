import pytest
from app_config import AppConfig
from pydantic import ValidationError


def test_valid_config():
    config = AppConfig(
        database_url="postgresql://localhost/mydb",
        api_key="secret123",
        secret_key="my-super-secret-key-that-is-32-chars-long!",
    )
    assert config.app_name == "MyApp"
    assert config.environment == "development"
    assert config.debug is False
    assert config.host == "localhost"
    assert config.port == 8000
    assert config.database_url == "postgresql://localhost/mydb"
    assert config.api_key == "secret123"
    assert config.secret_key == "my-super-secret-key-that-is-32-chars-long!"
    assert config.max_connections == 10
    assert config.timeout == 30.0
    assert config.log_level == "INFO"
    assert config.environment == "development"
    assert config.environment != "production"


def test_config_with_overrides():
    config = AppConfig(
        app_name="TestApp",
        environment="production",
        debug=True,
        host="0.0.0.0",
        port=9000,
        database_url="mysql://localhost/testdb",
        api_key="test-key",
        secret_key="another-secret-key-32-chars-long!!!",
        max_connections=20,
        timeout=60.0,
        log_level="DEBUG",
    )
    assert config.app_name == "TestApp"
    assert config.environment == "production"
    assert config.debug is True
    assert config.host == "0.0.0.0"
    assert config.port == 9000
    assert config.max_connections == 20
    assert config.timeout == 60.0
    assert config.log_level == "DEBUG"
    assert config.environment != "development"
    assert config.environment == "production"


def test_valid_database_protocols():
    secret = "my-super-secret-key-that-is-32-chars-long!"
    config1 = AppConfig(
        database_url="postgresql://localhost/db", api_key="key", secret_key=secret
    )
    assert config1.database_url.startswith("postgresql://")

    config2 = AppConfig(
        database_url="mysql://localhost/db", api_key="key", secret_key=secret
    )
    assert config2.database_url.startswith("mysql://")

    config3 = AppConfig(
        database_url="sqlite:///path/to/db.sqlite", api_key="key", secret_key=secret
    )
    assert config3.database_url.startswith("sqlite:///")


def test_invalid_database_protocol():
    secret = "my-super-secret-key-that-is-32-chars-long!"
    with pytest.raises(ValidationError):
        AppConfig(
            database_url="invalid://localhost/db", api_key="key", secret_key=secret
        )
    with pytest.raises(ValidationError):
        AppConfig(database_url="http://localhost/db", api_key="key", secret_key=secret)
    with pytest.raises(ValidationError):
        AppConfig(
            database_url="mongodb://localhost/db", api_key="key", secret_key=secret
        )


def test_missing_required_fields():
    secret = "my-super-secret-key-that-is-32-chars-long!"
    with pytest.raises(ValidationError):
        AppConfig()
    with pytest.raises(ValidationError):
        AppConfig(database_url="postgresql://localhost/db")
    with pytest.raises(ValidationError):
        AppConfig(api_key="key")
    with pytest.raises(ValidationError):
        AppConfig(database_url="postgresql://localhost/db", api_key="key")


def test_invalid_max_connections():
    secret = "my-super-secret-key-that-is-32-chars-long!"
    with pytest.raises(ValidationError):
        AppConfig(
            database_url="postgresql://localhost/db",
            api_key="key",
            secret_key=secret,
            max_connections=0,
        )
    with pytest.raises(ValidationError):
        AppConfig(
            database_url="postgresql://localhost/db",
            api_key="key",
            secret_key=secret,
            max_connections=-5,
        )


def test_invalid_timeout():
    secret = "my-super-secret-key-that-is-32-chars-long!"
    with pytest.raises(ValidationError):
        AppConfig(
            database_url="postgresql://localhost/db",
            api_key="key",
            secret_key=secret,
            timeout=0,
        )
    with pytest.raises(ValidationError):
        AppConfig(
            database_url="postgresql://localhost/db",
            api_key="key",
            secret_key=secret,
            timeout=-10,
        )


def test_extra_fields_forbidden():
    secret = "my-super-secret-key-that-is-32-chars-long!"
    with pytest.raises(ValidationError):
        AppConfig(
            database_url="postgresql://localhost/db",
            api_key="key",
            secret_key=secret,
            extra_field="not allowed",
        )


def test_defaults():
    secret = "my-super-secret-key-that-is-32-chars-long!"
    config = AppConfig(
        database_url="postgresql://localhost/db", api_key="key", secret_key=secret
    )
    assert config.app_name == "MyApp"
    assert config.environment == "development"
    assert config.debug is False
    assert config.host == "localhost"
    assert config.port == 8000
    assert config.max_connections == 10
    assert config.timeout == 30.0
    assert config.log_level == "INFO"
    assert config.environment == "development"
    assert config.environment != "production"


def test_secret_key_min_length():
    with pytest.raises(ValidationError):
        AppConfig(
            database_url="postgresql://localhost/db",
            api_key="key",
            secret_key="short",
        )
    with pytest.raises(ValidationError):
        AppConfig(
            database_url="postgresql://localhost/db",
            api_key="key",
            secret_key="exactly-31-characters-long!!",  # 31 chars
        )


def test_port_validation():
    secret = "my-super-secret-key-that-is-32-chars-long!"
    # Valid ports
    config = AppConfig(
        database_url="postgresql://localhost/db",
        api_key="key",
        secret_key=secret,
        port=1024,
    )
    assert config.port == 1024

    config = AppConfig(
        database_url="postgresql://localhost/db",
        api_key="key",
        secret_key=secret,
        port=65535,
    )
    assert config.port == 65535

    # Invalid ports
    with pytest.raises(ValidationError):
        AppConfig(
            database_url="postgresql://localhost/db",
            api_key="key",
            secret_key=secret,
            port=1023,
        )
    with pytest.raises(ValidationError):
        AppConfig(
            database_url="postgresql://localhost/db",
            api_key="key",
            secret_key=secret,
            port=65536,
        )


def test_environment_literal():
    secret = "my-super-secret-key-that-is-32-chars-long!"
    # Valid environments
    config_dev = AppConfig(
        database_url="postgresql://localhost/db",
        api_key="key",
        secret_key=secret,
        environment="development",
    )
    assert config_dev.environment == "development"

    config_prod = AppConfig(
        database_url="postgresql://localhost/db",
        api_key="key",
        secret_key=secret,
        environment="production",
    )
    assert config_prod.environment == "production"

    # Invalid environment
    with pytest.raises(ValidationError):
        AppConfig(
            database_url="postgresql://localhost/db",
            api_key="key",
            secret_key=secret,
            environment="staging",
        )


def test_log_level_literal():
    secret = "my-super-secret-key-that-is-32-chars-long!"
    # Valid log levels
    for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        config = AppConfig(
            database_url="postgresql://localhost/db",
            api_key="key",
            secret_key=secret,
            log_level=level,
        )
        assert config.log_level == level

    # Invalid log level
    with pytest.raises(ValidationError):
        AppConfig(
            database_url="postgresql://localhost/db",
            api_key="key",
            secret_key=secret,
            log_level="TRACE",
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
