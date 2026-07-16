import asyncio
import logging
from typing import Any

from app.core.database import SessionLocal
from app.repositories.cv_embedding_repository import CVEmbeddingRepository
from app.utils.data_formatter import flatten_cv_data
from app.services.llm_service import generate_embedding

logger = logging.getLogger(__name__)


class EmbeddingService:
    async def process_and_save_embedding(self, db_session: Any, cv_id: int, structured_data: dict) -> None:
        """
        Flatten structured_data, generate embedding via LLM, and persist to DB.
        Any Gemini/DB failure is logged and rolled back safely.
        """
        session = db_session if db_session is not None else SessionLocal()
        should_close_session = db_session is None

        try:
            flattened_text = flatten_cv_data(structured_data or {})
            if not flattened_text:
                logger.info("Embedding skipped for cv_id=%s because flattened text is empty", cv_id)
                return

            embedding_vector = await generate_embedding(flattened_text)

            if not isinstance(embedding_vector, list) or len(embedding_vector) != 768:
                raise ValueError(
                    f"Unexpected embedding shape for cv_id={cv_id}: "
                    f"type={type(embedding_vector).__name__}, len={len(embedding_vector) if isinstance(embedding_vector, list) else 'n/a'}"
                )

            await CVEmbeddingRepository.upsert_embedding(
                session=session,
                cv_id=cv_id,
                flattened_text=flattened_text,
                embedding_vector=embedding_vector,
            )

        except Exception as exc:
            logger.exception("Embedding pipeline failed for cv_id=%s", cv_id)
            try:
                await asyncio.to_thread(session.rollback)
            except Exception as rollback_exc:
                logger.exception("Rollback failed for cv_id=%s: %s", cv_id, rollback_exc)
        finally:
            if should_close_session:
                await asyncio.to_thread(session.close)
