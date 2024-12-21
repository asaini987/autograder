from pydantic import BaseModel

class EmbedRubricRequest(BaseModel):
    user_id: str
    """The user ID of the namespace in which to embed the document"""
class QueryRequest(BaseModel):
    query: str
    user_id: str
    """Search query for retrieving relevant documents."""