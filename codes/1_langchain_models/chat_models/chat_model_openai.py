# chat_models/chat_model_openai.py
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Create Chat Model object
model = ChatOpenAI(model="gpt-4")

# Invoke with string input
result = model.invoke("What is the capital of India?")

# Print full response (includes metadata)
print(result)

# Print only content
print(result.content)
# Output: "The capital of India is New Delhi."
