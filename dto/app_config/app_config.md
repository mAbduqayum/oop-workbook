# AppConfig - Pydantic Settings Management

## Exercise: Application Configuration with BaseSettings

Create an `AppConfig` class using Pydantic's `BaseSettings` to manage application configuration from environment
variables and `.env` files.

**Task:**

1. Create a `.env` file in the same directory as `app_config.py` with the following content:
   ```
   DATABASE_URL=postgresql://localhost/mydb
   API_KEY=secret123
   SECRET_KEY=my-super-secret-key-that-is-32-chars-long!
   DEBUG=true
   ```
   > **Note:** Use UPPERCASE for environment variable names - this is the standard convention.

2. Create an `AppConfig` class using `BaseSettings` with the following fields:
    - `app_name: str` - Application name (default: "MyApp")
    - `environment: ["development", "production"]` - Environment (default: "development")
    - `debug: bool` - Debug mode (default: False)
    - `host: str` - Server host (default: "localhost")
    - `port: int` - Server port (1024-65535, default: 8000)
    - `database_url: str` - Database connection string (required)
    - `api_key: str` - Some API key for external services (required)
    - `secret_key: str` - Secret key for encryption (min 32 chars, required)
    - `max_connections: int` - Maximum database connections (must be > 0, default: 10)
    - `timeout: float` - Request timeout in seconds (must be > 0, default: 30.0)
    - `log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]` - Logging level (default: "INFO")
3. Configure the model to:
    - Read from `.env` file
    - Be case-insensitive for environment variable names (allows uppercase convention)
    - Forbid extra fields
4. Add a field validator for `database_url` to ensure it starts with a valid protocol (postgresql://, mysql://, or
   sqlite:///)

**Example:**

```python
# Create .env file in the same directory:
# DATABASE_URL=postgresql://localhost/mydb
# API_KEY=secret123
# SECRET_KEY=my-super-secret-key-that-is-32-chars-long!
# DEBUG=true

config = AppConfig()
print(config.app_name)  # MyApp
print(config.debug)  # True
print(config.database_url)  # postgresql://localhost/mydb
print(config.environment == "development")  # True
print(config.environment == "production")  # False

# Can override with constructor
config2 = AppConfig(
    database_url="mysql://localhost/testdb",
    api_key="test-key",
    secret_key="another-secret-key-32-chars-long!!!",
    debug=False,
    environment="production"
)
print(config2.environment == "production")  # True
```

**Environment Variables:**
Settings are loaded in priority order:

1. Constructor arguments (highest priority)
2. Environment variables
3. `.env` file variables
4. Default values (lowest priority)

**Important Notes:**

> **Note:** The `.env` file is optional. `BaseSettings` will use this priority order:
> 1. Constructor arguments (highest priority)
> 2. Environment variables
> 3. `.env` file variables
> 4. Default values (lowest priority)

> **Note:** With `case_sensitive=False`, environment variables are case-insensitive. However, the **convention** is to
> use UPPERCASE for environment variables (e.g., `DATABASE_URL`, `API_KEY`) while keeping Python field names in
> lowercase/snake_case (e.g., `database_url`, `api_key`).

> **Note:** The `.env` file must be in the **directory where the script is executed from**, not necessarily where the
> Python file is located.

> **Note:** Use Pydantic's `Field()` for validation constraints (e.g., `Field(gt=0)`, `Field(min_length=32)`,
`Field(ge=1024, le=65535)`) instead of custom validators when possible.
