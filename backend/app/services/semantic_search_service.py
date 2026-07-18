from __future__ import annotations

from typing import Any

from app.repositories.cv_embedding_repository import CVEmbeddingRepository
from app.schemas.semantic_search_schemas import (
    SemanticSearchRequest,
    SemanticSearchResponse,
    SemanticSearchResultItem,
)
from app.services.llm_service import generate_embedding


class SemanticSearchService:
    def __init__(self, repository: CVEmbeddingRepository | None = None) -> None:
        self.repository = repository or CVEmbeddingRepository()

    async def search_cvs(
        self,
        *,
        request: SemanticSearchRequest,
        db_session: Any,
    ) -> SemanticSearchResponse:
        query_embedding = await generate_embedding(request.query)
        raw_results = await self.repository.search_by_embedding(
            session=db_session,
            query_embedding=query_embedding,
            top_k=request.top_k,
        )

        results = [
            SemanticSearchResultItem(
                cv_id=item["cv_id"],
                original_filename=item["original_filename"],
                status=item["status"],
                distance=float(item["distance"]),
            )
            for item in raw_results
        ]

        return SemanticSearchResponse(results=results)
