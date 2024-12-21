from fastapi import APIRouter, UploadFile, File
from models.request import EmbedRubricRequest, QueryRequest
from models.response import QueryResponse
from services.embeddings import extract_text_from_pdf, embed_doc
from db.pinecone_client import pc

router = APIRouter()

@router.post("/upload-rubric")
async def upload_and_store_doc(request: EmbedRubricRequest, file: UploadFile = File(...)):
    file_bytes = await file.read()
    extracted_text = extract_text_from_pdf(file_bytes)
    doc_embeddings = embed_doc(extracted_text, file.filename)
    pc.upsert_vectors(doc_embeddings, request.user_id)
    return {"message" : "Rubric uploaded successfully"}