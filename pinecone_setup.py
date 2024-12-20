from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os
import time

load_dotenv()

API_KEY = os.getenv("PINECONE_API_KEY")

pc = Pinecone(api_key=API_KEY)

index_name = "rubric_embeddings"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384, # Dimension of all-MiniLM-L6-v2 SentenceTransformer model vector embeddings
        metric="cosine",
        spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
        ) 
    )
    # Wait for index to be ready
    while not pc.describe_index(index_name).status['ready']:
        time.sleep(1)