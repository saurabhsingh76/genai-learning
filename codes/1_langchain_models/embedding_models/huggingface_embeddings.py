# embedding_models/huggingface_embeddings.py
from langchain_huggingface import HuggingFaceEmbeddings

# Load free embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "Machine learning is fascinating"
vector = embeddings.embed_query(text)

print(f"Vector dimensions: {len(vector)}")
