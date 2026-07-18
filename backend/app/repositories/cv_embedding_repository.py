import asyncio
from typing import Any

from sqlalchemy import and_, cast
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from pgvector.sqlalchemy import Vector

from app.models.cv import CV
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

    async def search_by_embedding(
        self,
        session: Session,
        query_embedding: list[float],
        top_k: int,
    ) -> list[dict[str, Any]]:
        stmt = (
            select(
                CV.id.label("cv_id"),
                CV.original_filename,
                CV.status,
                (CVEmbedding.embedding.cosine_distance(query_embedding)).label("distance"),
            )
            .join(CVEmbedding, CVEmbedding.cv_id == CV.id)
            .where(CV.status == "COMPLETED")
            .order_by(CVEmbedding.embedding.cosine_distance(query_embedding))
            .limit(top_k)
        )

        result = await asyncio.to_thread(session.execute, stmt)
        rows = result.fetchall()
        return [
            {
                "cv_id": row.cv_id,
                "original_filename": row.original_filename,
                "status": row.status,
                "distance": row.distance,
            }
            for row in rows
        ]
