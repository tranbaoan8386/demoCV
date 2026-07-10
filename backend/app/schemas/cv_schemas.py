from datetime import datetime
from typing import Any

from pydantic import BaseModel


class CVUploadResponse(BaseModel):
    """Response schema for CV upload endpoint"""

    id: int
    original_filename: str
    object_name: str
    status: str
    created_at: datetime
    structured_data: dict[str, Any] | None = None

    class Config:
        from_attributes = True
