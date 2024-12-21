from fastapi import APIRouter
from models.request import EmbeddingRequest, QueryRequest
from models.response import EmbeddingResponse, QueryResponse
from services.embeddings import embed_text

router = APIRouter()

@router.post("/embed", response_model=EmbeddingResponse)
async def embed_text(request: EmbeddingRequest):
    return {"embeddings" : embed_text(request.text)}