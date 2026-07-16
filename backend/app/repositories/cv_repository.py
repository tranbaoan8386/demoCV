from sqlalchemy.orm import Session

from app.models.cv import CV


class CVRepository:
    """Repository for CV database operations"""

    @staticmethod
    def create_cv(
        session: Session,
        original_filename: str,
        object_name: str,
        raw_text=None,
        structured_data=None,
        status: str = "PENDING"
    ) -> CV:
        """
        Create a new CV record in the database

        Args:
            session: SQLAlchemy session
            original_filename: User's uploaded filename
            object_name: MinIO storage path
            status: Upload status (default: "UPLOADED")

        Returns:
            CV: Created CV instance with auto-generated ID
        """
        cv = CV(
            original_filename=original_filename,
            object_name=object_name,
            status=status,
            raw_text=raw_text,
            structured_data=structured_data
        )
        session.add(cv)
        session.commit()
        session.refresh(cv)
        return cv

    @staticmethod
    def get_cv(session: Session, cv_id: int) -> CV | None:
        """Get CV by ID"""
        return session.query(CV).filter(CV.id == cv_id).first()

    @staticmethod
    def update_cv(
        session: Session,
        cv_id: int,
        *,
        raw_text=None,
        structured_data=None,
        status: str | None = None
    ) -> CV:
        """Update CV record fields and persist them."""
        cv = session.query(CV).filter(CV.id == cv_id).first()
        if cv is None:
            raise ValueError(f"CV with id={cv_id} was not found")

        if raw_text is not None:
            cv.raw_text = raw_text
        if structured_data is not None:
            cv.structured_data = structured_data
        if status is not None:
            cv.status = status

        session.add(cv)
        session.commit()
        session.refresh(cv)
        return cv
