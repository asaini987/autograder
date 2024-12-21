from pydantic import BaseModel
from fastapi import UploadFile


class QueryRequest(BaseModel):
    query: str
    """Search query for retrieving relevant documents."""