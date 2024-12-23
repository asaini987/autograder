from fastapi import FastAPI
from .routes import embeddings

app = FastAPI()
app.include_router(embeddings.router, prefix="/api/embeddings")


# Run the server with this command from backend/: uvicorn app.main:app --reload
@app.get("/")
def read_root():
    return {"Hello": "World"}