from datetime import datetime

from pydantic import BaseModel


class CVUploadResponse(BaseModel):
    """Response schema for CV upload endpoint"""

    id: int
    original_filename: str
    object_name: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
