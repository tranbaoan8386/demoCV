from datetime import datetime

from pydantic import BaseModel


class CVUploadResponse(BaseModel):
    """Response schema for CV upload endpoint"""

    id: int
    original_filename: str
    object_name: str
    status: str
    created_at: datetime
    cleaned_text: str | None = None

    class Config:
        from_attributes = True
