# chat_models/huggingface_model.py
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

# Create local pipeline
pipe = pipeline(
    "text-generation",
    model="microsoft/DialoGPT-medium",
    tokenizer="microsoft/DialoGPT-medium"
)

# Create LangChain wrapper
llm = HuggingFacePipeline(pipeline=pipe)

result = llm.invoke("Hello, how are you?")
print(result)
