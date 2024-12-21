from fastapi import FastAPI
from app.routes import embeddings
from db.pinecone_client import PineconeClient

app = FastAPI()
app.include_router(embeddings.router, prefix="/api/embeddings")

pc = PineconeClient()
# Run the server with: fastapi dev main.py
@app.get("/")
def read_root():
    return {"Hello": "World"}