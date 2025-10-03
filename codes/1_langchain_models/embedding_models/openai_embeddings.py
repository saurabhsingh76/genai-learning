# embedding_models/openai_embeddings.py
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# Convert text to vectors
text = "What is the capital of India?"
vector = embeddings.embed_query(text)

print(f"Vector length: {len(vector)}")
print(f"First 10 dimensions: {vector[:10]}")
