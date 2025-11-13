from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="forbid",
    )

    app_name: str = "MyApp"
    environment: Literal["development", "production"] = "development"
    debug: bool = False
    host: str = "localhost"
    port: int = Field(ge=1024, le=65535, default=8000)
    database_url: str
    api_key: str
    secret_key: str = Field(min_length=32)
    max_connections: int = Field(gt=0, default=10)
    timeout: float = Field(gt=0, default=30.0)
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"

    @field_validator("database_url")
    @classmethod
    def validate_database_url(cls, v: str) -> str:
        valid_protocols = ["postgresql://", "mysql://", "sqlite:///"]
        if not any(v.startswith(protocol) for protocol in valid_protocols):
            raise ValueError(
                "database_url must start with postgresql://, mysql://, or sqlite:///"
            )
        return v


if __name__ == "__main__":
    config = AppConfig()
    print(config.app_name)
    print(config.debug)
    print(config.database_url)
    print(config.environment == "development")
    print(config.environment == "production")
