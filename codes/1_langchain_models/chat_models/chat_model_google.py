# chat_models/chat_model_google.py
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-pro")
result = model.invoke("What are the benefits of renewable energy?")
print(result.content)
