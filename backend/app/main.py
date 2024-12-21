from fastapi import FastAPI
from app.routes import embeddings

app = FastAPI()
app.include_router(embeddings.router, prefix="/api/embeddings")

# Run the server with: fastapi dev main.py
@app.get("/")
def read_root():
    return {"Hello": "World"}