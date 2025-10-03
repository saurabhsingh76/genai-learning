# chat_models/chat_model_anthropic.py
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-3-sonnet-20240229")
result = model.invoke("Explain quantum computing in simple terms")
print(result.content)
