from fastapi import APIRouter, UploadFile, File
from models.request import QueryRequest
from models.response import QueryResponse
from services.embeddings import extract_text_from_pdf, embed_doc
from db.pinecone_client import pc

router = APIRouter()

@router.post("/embeddoc")
async def embed_doc(file: UploadFile = File(...)):
    file_bytes = await file.read()
    extracted_text = extract_text_from_pdf(file_bytes)
    doc_embeddings = embed_doc(extracted_text)
    pc.upsert_vectors(doc_embeddings, "12345") # TODO: GET USER ID
