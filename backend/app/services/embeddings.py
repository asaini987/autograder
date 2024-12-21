from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
from io import BytesIO

model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text_from_pdf(file_bytes):
    pdf_reader = PdfReader(BytesIO(file_bytes))
    return "".join(page.extract_text() for page in pdf_reader.pages)

def embed_doc(doc_text, doc_name):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,  # Adjust based on LLM or embedding model limits
        chunk_overlap=50,  # Small overlap for context continuity
        length_function=len,
    )
    chunks = text_splitter.split_text(doc_text)

    embeddings = []
    for idx, chunk in enumerate(chunks):
        embedding = model.encode(chunk)
        embeddings.append({
            "embedding": embedding,
            "metadata": {
                "chunk_index": idx,
                "text": chunk,
                "source_file": doc_name
            }
        })

    return embeddings