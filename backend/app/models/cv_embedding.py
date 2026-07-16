from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text

from pgvector.sqlalchemy import Vector

from app.core.database import Base


class CVEmbedding(Base):
    __tablename__ = "cv_embeddings"

    id = Column(Integer, primary_key=True)
    cv_id = Column(
        Integer,
        ForeignKey("cvs.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )
    flattened_text = Column(Text, nullable=False)
    embedding = Column(Vector(768), nullable=False)
