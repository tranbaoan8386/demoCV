import types

import pytest

from app.services.cv_upload_service import CVUploadService


class DummyStorage:
    def upload_file(self, file_content: bytes, object_name: str) -> str:
        return object_name


class DummyRepository:
    @staticmethod
    def create_cv(
        session,
        original_filename: str,
        object_name: str,
        raw_text=None,
        structured_data=None,
        status: str = "PENDING",
    ):
        return types.SimpleNamespace(
            id=123,
            original_filename=original_filename,
            object_name=object_name,
            status=status,
            created_at=None,
            structured_data=structured_data,
        )


@pytest.mark.anyio
async def test_cv_upload_service_exposes_background_methods():
    service = CVUploadService(DummyStorage(), DummyRepository())

    assert hasattr(service, "init_cv_record")
    assert hasattr(service, "process_cv_background")

    cv_id = await service.init_cv_record(
        db_session=None,
        file_content=b"%PDF-1.4 test",
        original_filename="test.pdf",
    )

    assert cv_id == 123
