from pydantic import BaseModel
from typing import List, Optional

class QueryResult(BaseModel):
    document_id: str
    content: str
    similarity_score: Optional[float] = None
    """A single retrieved document and its metadata."""

class QueryResponse(BaseModel):
    query: str
    results: List[QueryResult]
    """Response for query requests, including matched documents."""

class EmbeddingResponse(BaseModel):
    embeddings: List[float]
    """The vector representation of the input text."""