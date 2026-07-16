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


class CVUploadAcceptedResponse(BaseModel):
    """Response schema for the asynchronous upload acceptance flow."""

    cv_id: int
    status: str = "PENDING"
    message: str = "CV upload accepted and is being processed in the background"
