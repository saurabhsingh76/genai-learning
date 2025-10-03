# llms/llm_demo.py
from langchain_openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create LLM object
llm = OpenAI(model="gpt-3.5-turbo-instruct")

# Simple string input → string output
result = llm.invoke("What is the capital of India?")
print(result)
# Output: "The capital of India is New Delhi."
