from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

async def embed_text(text):
    return model.encode(text, show_progress_bar=True)