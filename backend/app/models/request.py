from pydantic import BaseModel

class EmbeddingRequest(BaseModel):
    text: str
    """Text to embed."""

class QueryRequest(BaseModel):
    query: str
    """Search query for retrieving relevant documents."""