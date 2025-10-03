# Document similarity using embeddings
from langchain_huggingface import HuggingFaceEmbeddings
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Initialize embeddings model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Sample documents
doc1 = "Python is a programming language"
doc2 = "Java is used for software development" 
doc3 = "Cooking pasta requires boiling water"

# Generate embeddings
vec1 = embeddings.embed_query(doc1)
vec2 = embeddings.embed_query(doc2)
vec3 = embeddings.embed_query(doc3)

# Calculate similarity
sim_1_2 = cosine_similarity([vec1], [vec2])[0][0]
sim_1_3 = cosine_similarity([vec1], [vec3])[0][0]

print(f"Similarity between doc1 and doc2: {sim_1_2:.4f}")
print(f"Similarity between doc1 and doc3: {sim_1_3:.4f}")

# Output shows doc1 and doc2 are more similar (both about programming)
