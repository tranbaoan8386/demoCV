import asyncio

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app.models.cv_embedding import CVEmbedding


class CVEmbeddingRepository:
    @staticmethod
    async def upsert_embedding(
        session: Session,
        cv_id: int,
        flattened_text: str,
        embedding_vector: list[float],
    ) -> None:
        stmt = insert(CVEmbedding).values(
            cv_id=cv_id,
            flattened_text=flattened_text,
            embedding=embedding_vector,
        )
        stmt = stmt.on_conflict_do_update(
            index_elements=[CVEmbedding.cv_id],
            set_={
                "flattened_text": stmt.excluded.flattened_text,
                "embedding": stmt.excluded.embedding,
            },
        )

        await asyncio.to_thread(session.execute, stmt)
        await asyncio.to_thread(session.commit)
