from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from app.core.database import Base


class CV(Base):
    __tablename__ = "cvs"

    id = Column(Integer, primary_key=True)
    original_filename = Column(String, nullable=False)
    object_name = Column(String, nullable=False)
    status = Column(String, nullable=False, default="UPLOADED")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)