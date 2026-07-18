from typing import List

from pydantic import BaseModel, Field, ConfigDict


class SemanticSearchRequest(BaseModel):
    query: str = Field(..., min_length=1, description="Natural language query to search CVs")
    top_k: int = Field(default=5, ge=1, le=20)

    model_config = ConfigDict(extra="forbid")


class SemanticSearchResultItem(BaseModel):
    cv_id: int
    original_filename: str
    status: str
    distance: float

    model_config = ConfigDict(from_attributes=True)


class SemanticSearchResponse(BaseModel):
    results: List[SemanticSearchResultItem] = Field(default_factory=list)
