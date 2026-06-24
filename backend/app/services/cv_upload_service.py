import uuid
from sqlalchemy.orm import Session

from app.models.cv import CV
from app.repositories.cv_repository import CVRepository
from app.storage.minio_storage import MinIOStorage
from app.services.pdf_parser_service import PDFParserService
from app.services.cv_parser_service import CVParserService


class CVUploadService:
    """Service for CV upload operations"""

    def __init__(self, storage: MinIOStorage, repository: CVRepository):
        """
        Initialize service with dependencies

        Args:
            storage: MinIO storage layer
            repository: CV repository layer
        """
        self.storage = storage
        self.repository = repository

    def upload_cv(
        self,
        db_session: Session,
        file_content: bytes,
        original_filename: str
    ) -> CV:
        """
        Upload CV file and save metadata

        Args:
            db_session: SQLAlchemy session
            file_content: PDF file bytes
            original_filename: Original filename from user

        Returns:
            CV: Created CV record with populated ID

        Raises:
            ValueError: If file validation fails
            Exception: If upload or database operations fail
        """
        # Step 1: Validate file
        self._validate_file(file_content, original_filename)

        # Step 2: Extract text from PDF
        raw_text = PDFParserService.extract_text(file_content)

        # Step 2.1: Parse CV data
        structured_data = CVParserService.parse(raw_text)

        print("========== STRUCTURED DATA ==========")
        print(structured_data)
        print("====================================")
        

        # Step 3: Generate unique object name
        object_name = self._generate_object_name(original_filename)

        # Step 4: Upload to MinIO
        try:
            self.storage.upload_file(file_content, object_name)
        except Exception as e:
            raise Exception(f"MinIO upload failed: {str(e)}")

        # Step 5: Save metadata to database
        try:
            cv = self.repository.create_cv(
                db_session,
                original_filename=original_filename,
                object_name=object_name,
                raw_text=raw_text,
                structured_data=structured_data,
                status="UPLOADED"
            )
            return cv
        except Exception as e:
            # In production, could attempt to delete file from MinIO here
            raise Exception(f"Database operation failed: {str(e)}")

    def _validate_file(self, file_content: bytes, filename: str) -> None:
        """
        Validate file type and size

        Args:
            file_content: File bytes
            filename: Original filename

        Raises:
            ValueError: If validation fails
        """
        # Check file extension
        if not filename.lower().endswith(".pdf"):
            raise ValueError("Only PDF files are allowed")

        # Check file size (10MB limit)
        max_size = 10 * 1024 * 1024  # 10MB
        if len(file_content) > max_size:
            raise ValueError(f"File size exceeds {max_size // (1024*1024)}MB limit")

        # Check file is not empty
        if len(file_content) == 0:
            raise ValueError("File is empty")

    def _generate_object_name(self, original_filename: str) -> str:
        """
        Generate unique object name for MinIO

        Args:
            original_filename: Original filename from user

        Returns:
            str: Unique object name (e.g., "cvs/uuid-filename.pdf")
        """
        # Generate UUID for uniqueness
        unique_id = str(uuid.uuid4())[:8]

        # Sanitize filename (keep only alphanumeric, dash, underscore, and extension)
        sanitized = "".join(
            c if c.isalnum() or c in "-_." else "_"
            for c in original_filename
        )

        # Construct object name
        object_name = f"cvs/{unique_id}-{sanitized}"

        return object_name
