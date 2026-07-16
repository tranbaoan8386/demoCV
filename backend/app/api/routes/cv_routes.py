from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.cv_schemas import CVUploadAcceptedResponse
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


@router.post("/upload", response_model=CVUploadAcceptedResponse, status_code=202)
async def upload_cv(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    service: CVUploadService = Depends(get_cv_service),
) -> CVUploadAcceptedResponse:
    """
    Upload a CV file asynchronously.

    - **file**: PDF file to upload (required)
    - Returns: Accepted response with CV ID and pending status
    """
    try:
        content = await file.read()

        cv_id = await service.init_cv_record(
            db_session=db,
            file_content=content,
            original_filename=file.filename
        )

        background_tasks.add_task(service.process_cv_background, cv_id, background_tasks)

        return CVUploadAcceptedResponse(
            cv_id=cv_id,
            status="PENDING",
            message="CV upload accepted and is being processed in the background"
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"System Error: {str(e)}")