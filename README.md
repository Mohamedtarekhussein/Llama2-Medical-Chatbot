# Medical Chatbot - AI-Powered Healthcare Assistant

## Overview
This Medical Chatbot is an AI-powered assistant designed to answer healthcare-related questions using LangChain, Llama 2, and FAISS vector search. It processes medical PDFs, converts them into embeddings, and retrieves relevant answers using a Retrieval-Augmented Generation (RAG) approach.

## Key Features:
- PDF Ingestion – Load and process medical documents.
- Vector Embeddings – Convert text into embeddings using Hugging Face.
- FAISS Vector Store – Efficient similarity search for fast retrieval.
- Llama 2 LLM – Generate accurate, context-aware responses.
- Chainlit UI – Interactive chat interface for users.

## Installation & Setup

### Prerequisites
- Python 3.9+
- Git
- Hugging Face Account (for embeddings)
- Llama 2 Model (GGML)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/medical-chatbot.git
cd medical-chatbot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Download Llama 2 Model
Place the model (`llama-2-7b-chat.ggmlv3.q8_0.bin`) in the project root or specify its path in `config.py`.

### 4. Add Medical PDFs
Place your PDF files in `data/pdfs/`.

## Configuration
Edit `config.py` to customize paths and model settings:
```python
DATA_PATH = "data/pdfs/"        # Path to PDFs
DB_FAISS_PATH = "models/db_faiss"  # FAISS vector store
MODEL_PATH = "llama-2-7b-chat.ggmlv3.q8_0.bin"  # Llama 2 model path
```

## Usage

### 1. Ingest PDFs & Create Vector DB
Run the data ingestion script:
```bash
python src/data_ingestion.py
```
This will:
- Load PDFs
- Split text into chunks
- Generate embeddings
- Save FAISS vector store

### 2. Run the Chatbot
Start the Chainlit interface:
```bash
chainlit run src/chatbot.py
```
The chatbot will launch at `http://localhost:8000`.

### 3. Ask Medical Questions
Example queries:
- "What are the symptoms of diabetes?"
- "How is hypertension treated?"

## Project Structure
```
medical-chatbot/
├── src/
│   ├── data_ingestion.py   # PDF processing & embeddings
│   ├── chatbot.py          # LLM & QA logic
│   ├── config.py           # Project settings
│   └── utils.py            # Helper functions
├── models/
│   └── db_faiss/           # FAISS vector store
├── data/
│   └── pdfs/               # Medical PDFs
├── tests/                  # Unit & integration tests
├── docs/                   # Documentation
├── requirements.txt        # Dependencies
├── README.md               # This file
└── .env.example            # Environment variables
```

## Tech Stack

| Component  | Technology                    |
|------------|--------------------------------|
| LLM        | Llama 2 (7B-Chat)              |
| Embeddings | Hugging Face all-MiniLM-L6-v2  |
| Vector DB  | FAISS                          |
| Framework  | LangChain                      |
| UI         | Chainlit                        |
| Language   | Python                         |

## License
This project is licensed under the MIT License.

## Contact & Support
For questions or improvements, open an issue or contact:
- Email: mohammed.hussein7800@gmail.com

## Future Improvements
- Fine-tune Llama 2 on medical datasets.
- Add HIPAA compliance for secure data handling.
- Deploy as a web app using FastAPI + Streamlit.

## References
- [LangChain Documentation](https://python.langchain.com)
- [Llama 2 on Hugging Face](https://huggingface.co)
- [FAISS GitHub](https://github.com/facebookresearch/faiss)
