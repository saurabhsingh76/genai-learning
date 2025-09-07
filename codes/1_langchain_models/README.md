## Setup and Installation

### Prerequisites
1. **Create Project Folder**
```bash
mkdir 1_langchain_models
cd 1_langchain_models
```

2. **Create Virtual Environment**
```bash
python -m venv langchain_env
# Windows
langchain_env\Scripts\activate
# macOS/Linux  
source langchain_env/bin/activate
```

3. **Install Dependencies**
Create `requirements.txt`

Install packages in virtual env:
```bash
pip install -r requirements.txt
```

### Environment Setup
Create `.env` file for API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

⚠️ **Note**: OpenAI requires paid credits (minimum $5 recommended) as they no longer offer free credits for new users.

---

## Practical Implementation

### Project Structure
```
1_langchain_models/
├── llms/
│   └── llm_demo.py
├── chat_models/
│   ├── chat_model_openai.py
│   ├── chat_model_anthropic.py
│   └── chat_model_google.py
├── embedding_models/
│   ├── openai_embeddings.py
│   └── huggingface_embeddings.py
├── requirements.txt
└── .env
```
