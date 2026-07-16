import sys
from sqlalchemy import text
from app.core.database import engine, Base
# Import các model để SQLAlchemy nhận diện cấu trúc bảng
from app.models.cv import CV 
from app.models.cv_embedding import CVEmbedding

def init_database():
    print("Kích hoạt pgvector extension và khởi tạo bảng dữ liệu...")
    with engine.begin() as connection:
        # 🚀 BƯỚC CHỐT HẠ: Phải bật extension vector lên trước!
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
        
    # Tạo cấu trúc các bảng
    Base.metadata.create_all(bind=engine)
    print("Khởi tạo các bảng thành công!")

if __name__ == "__main__":
    init_database()