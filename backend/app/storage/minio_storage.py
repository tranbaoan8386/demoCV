import os
from io import BytesIO

from minio import Minio
from minio.error import S3Error


class MinIOStorage:
    """MinIO storage layer for file operations"""

    def __init__(self):
        """Initialize MinIO client from environment variables"""
        self.endpoint = os.getenv("MINIO_ENDPOINT")
        self.access_key = os.getenv("MINIO_ACCESS_KEY", "admin")
        self.secret_key = os.getenv("MINIO_SECRET_KEY", "password123")
        self.bucket_name = "cvbucket"

        self.client = Minio(
            self.endpoint,
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=False
        )

        # Ensure bucket exists
        self._ensure_bucket_exists()

    def _ensure_bucket_exists(self) -> None:
        """Create bucket if it doesn't exist"""
        try:
            if not self.client.bucket_exists(self.bucket_name):
                self.client.make_bucket(self.bucket_name)
        except S3Error as e:
            raise Exception(f"Failed to initialize MinIO bucket: {str(e)}")

    def upload_file(self, file_content: bytes, object_name: str) -> str:
        """
        Upload file to MinIO

        Args:
            file_content: File bytes
            object_name: Path in MinIO (e.g., "cvs/uuid-filename.pdf")

        Returns:
            str: Object name if successful

        Raises:
            Exception: If upload fails
        """
        try:
            file_io = BytesIO(file_content)
            self.client.put_object(
                self.bucket_name,
                object_name,
                file_io,
                length=len(file_content),
                content_type="application/pdf"
            )
            return object_name
        except S3Error as e:
            raise Exception(f"Failed to upload file to MinIO: {str(e)}")

    def download_file(self, object_name: str) -> bytes:
        """
        Download file from MinIO by object name.

        Args:
            object_name: Path in MinIO

        Returns:
            bytes: File content
        """
        try:
            with self.client.get_object(self.bucket_name, object_name) as response:
                return response.read()
        except S3Error as e:
            raise Exception(f"Failed to download file from MinIO: {str(e)}")
