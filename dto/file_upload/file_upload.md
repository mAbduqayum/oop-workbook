# FileUpload - File Metadata Validation

## Exercise: FileUpload Model with Size and Type Validation

Create a `FileUpload` class using Pydantic's `BaseModel` with file metadata validation.

**Task:**

1. Create a `FileUpload` class using `BaseModel` with the following fields:
    - `filename: str` - Original filename (1-255 characters)
    - `size_bytes: int` - File size in bytes (must be > 0, max 10MB = 10,485,760 bytes)
    - `mime_type: str` - MIME type (must be one of: "image/jpeg", "image/png", "image/gif", "application/pdf", "
      text/plain")
    - `upload_date: datetime` - Upload timestamp
2. Add a `file_extension` property that extracts the extension from filename
3. Add a `size_mb` property that returns size in megabytes rounded to 2 decimals
4. Add a field validator for `filename` to ensure it contains an extension

**Example:**

```python
from datetime import datetime

upload = FileUpload(
    filename="document.pdf",
    size_bytes=1048576,
    mime_type="application/pdf",
    upload_date=datetime(2024, 1, 15, 10, 30, 0)
)

print(upload.filename)  # document.pdf
print(upload.file_extension)  # pdf
print(upload.size_mb)  # 1.0

image = FileUpload(
    filename="photo.jpg",
    size_bytes=2097152,
    mime_type="image/jpeg",
    upload_date=datetime(2024, 1, 15, 11, 0, 0)
)

print(image.file_extension)  # jpg
print(image.size_mb)  # 2.0

# File too large raises ValidationError
FileUpload(
    filename="huge.pdf",
    size_bytes=20000000,
    mime_type="application/pdf",
    upload_date=datetime.now()
)  # ValidationError

# Invalid MIME type raises ValidationError
FileUpload(
    filename="file.exe",
    size_bytes=1024,
    mime_type="application/x-msdownload",
    upload_date=datetime.now()
)  # ValidationError

# No extension raises ValidationError
FileUpload(
    filename="noextension",
    size_bytes=1024,
    mime_type="text/plain",
    upload_date=datetime.now()
)  # ValidationError
```
