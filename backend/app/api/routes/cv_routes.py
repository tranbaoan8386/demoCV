from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.cv_schemas import CVUploadResponse
from app.services.cv_upload_service import CVUploadService
from app.repositories.cv_repository import CVRepository
from app.storage.minio_storage import MinIOStorage


router = APIRouter(prefix="/cvs", tags=["cvs"])


def get_db():
    """Dependency: Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_cv_service() -> CVUploadService:
    """Dependency: Get CV upload service"""
    storage = MinIOStorage()
    repository = CVRepository()
    return CVUploadService(storage, repository)


@router.post("/upload", response_model=CVUploadResponse)
def upload_cv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    service: CVUploadService = Depends(get_cv_service)
) -> CVUploadResponse:
    """
    Upload a CV file

    - **file**: PDF file to upload (required)
    - Returns: CV metadata with ID and storage location
    """
    try:
        # Read file content
        content = file.file.read()

        # Call service to handle upload
        cv = service.upload_cv(
            db_session=db,
            file_content=content,
            original_filename=file.filename
        )

        # Convert model to response schema
        return CVUploadResponse(
            id=cv.id,
            original_filename=cv.original_filename,
            object_name=cv.object_name,
            status=cv.status,
            created_at=cv.created_at
        )

    except ValueError as e:
        # File validation errors
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Unexpected errors
        raise HTTPException(status_code=500, detail="Failed to upload CV file")
