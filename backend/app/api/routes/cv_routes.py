from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.cv_schemas import CVUploadAcceptedResponse
from app.schemas.semantic_search_schemas import SemanticSearchRequest, SemanticSearchResponse
from app.services.cv_upload_service import CVUploadService
from app.repositories.cv_repository import CVRepository
from app.storage.minio_storage import MinIOStorage
from app.services.semantic_search_service import SemanticSearchService


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


def get_semantic_search_service() -> SemanticSearchService:
    """Dependency: Get semantic search service."""
    return SemanticSearchService()


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


@router.post("/semantic-search", response_model=SemanticSearchResponse)
async def semantic_search_cv(
    request: SemanticSearchRequest,
    db: Session = Depends(get_db),
    service: SemanticSearchService = Depends(get_semantic_search_service),
) -> SemanticSearchResponse:
    """Search completed CVs by semantic similarity using vector embeddings."""
    try:
        return await service.search_cvs(request=request, db_session=db)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"System Error: {str(exc)}") from exc