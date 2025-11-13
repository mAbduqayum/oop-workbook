from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class FileUpload(BaseModel):
    filename: str = Field(min_length=1, max_length=255, pattern=r"^.+\..+$")
    size_bytes: int = Field(gt=0, le=10485760)
    mime_type: Literal[
        "image/jpeg",
        "image/png",
        "image/gif",
        "application/pdf",
        "text/plain",
    ]
    upload_date: datetime

    @property
    def file_extension(self) -> str:
        return self.filename.rsplit(".", 1)[1]

    @property
    def size_mb(self) -> float:
        return round(self.size_bytes / (1024 * 1024), 2)
