from sqlalchemy.orm import Session

from app.models.cv import CV


class CVRepository:
    """Repository for CV database operations"""

    @staticmethod
    def create_cv(
        session: Session,
        original_filename: str,
        object_name: str,
        status: str = "UPLOADED"
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
            status=status
        )
        session.add(cv)
        session.commit()
        session.refresh(cv)
        return cv

    @staticmethod
    def get_cv(session: Session, cv_id: int) -> CV | None:
        """Get CV by ID"""
        return session.query(CV).filter(CV.id == cv_id).first()
