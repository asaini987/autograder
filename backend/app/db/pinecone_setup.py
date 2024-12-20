from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os
import time

load_dotenv("../.env")

API_KEY = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=API_KEY)
INDEX_NAME = "rubric_embeddings"

def create_index_if_not_exist():
    """
    Creates a Pinecone index for rubric embeddings if it does not already exist
    """
    if INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=INDEX_NAME,
            dimension=384, # Dimension of all-MiniLM-L6-v2 SentenceTransformer model vector embeddings
            metric="cosine",
            spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
            ) 
        )
        # Wait for index to be ready
        while not pc.describe_index(INDEX_NAME).status['ready']:
            time.sleep(1)

def upsert_vectors(vectors):
    """
    Upserts (Update and Insert) vectors into the Pinecone rubric embeddings index.

    Args:
        vectors (list): List of tuples (id: str, embedding: List[float], metadata: Dict[Any : Any]) to upsert.
    """
    index = pc.Index(INDEX_NAME)
    index.upsert(vectors)
