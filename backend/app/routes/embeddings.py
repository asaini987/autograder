from fastapi import APIRouter, UploadFile, File
from ..models.request import EmbedRubricRequest, QueryRequest
from ..models.response import QueryResponse
from ..services.embeddings import extract_text_from_pdf, embed_doc, retrieve_top_vectors, ask_llm
from ..db.pinecone_client import pc

router = APIRouter()

@router.post("/upload-rubric")
async def upload_and_store_doc(request: EmbedRubricRequest, file: UploadFile = File(...)):
    file_bytes = await file.read() # TODO: Store file on S3, filename on some DB
    extracted_text = extract_text_from_pdf(file_bytes)
    doc_embeddings = embed_doc(extracted_text, file.filename)
    pc.upsert_vectors(doc_embeddings, request.user_id)
    return {"message" : "Rubric uploaded successfully"}

@router.post("/grade-answer")
async def grade_answer(request: QueryRequest):
    query_response = retrieve_top_vectors(request.user_id, request.question)
    top_vectors = query_response["matches"]
    texts = [vector["metadata"]["text"] for vector in top_vectors]
    context = "\n".join(texts)
    answer = ask_llm(request.question, request.student_response, context)
    return {"response" : answer}