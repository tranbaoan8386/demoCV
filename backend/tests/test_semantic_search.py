import asyncio

from app.schemas.semantic_search_schemas import SemanticSearchRequest, SemanticSearchResponse
from app.services.semantic_search_service import SemanticSearchService


class FakeRepository:
    def __init__(self):
        self.calls = []

    async def search_by_embedding(self, session, query_embedding, top_k):
        self.calls.append((session, query_embedding, top_k))
        return [
            {
                "cv_id": 1,
                "original_filename": "candidate.pdf",
                "status": "COMPLETED",
                "distance": 0.12,
            }
        ]


def test_semantic_search_service_returns_mapped_results(monkeypatch):
    repository = FakeRepository()
    service = SemanticSearchService(repository=repository)

    async def fake_generate_embedding(text: str):
        return [0.1] * 768

    monkeypatch.setattr(
        "app.services.semantic_search_service.generate_embedding",
        fake_generate_embedding,
    )

    request = SemanticSearchRequest(query="Python backend developer", top_k=3)
    response = asyncio.run(service.search_cvs(request=request, db_session=None))

    assert isinstance(response, SemanticSearchResponse)
    assert response.results[0].cv_id == 1
    assert response.results[0].original_filename == "candidate.pdf"
    assert response.results[0].distance == 0.12
    assert repository.calls[0][2] == 3
