# 💼 FinAI Analyst

A Generative AI-powered **Financial Analyst RAG pipeline** to parse PDFs, summarise content, derive business insights, and answer user queries using OpenAI or Google Gemini LLMs.

---

## 🚀 **Features**

✅ PDF parsing and ingestion  
✅ Summarisation using LLMs (OpenAI or Gemini)  
✅ Vector store indexing via ChromaDB  
✅ Retrieval-Augmented Generation (RAG) pipeline  
✅ Business insights extraction  
✅ Streamlit frontend for seamless interaction

---

## 🗂 **Project Structure**
finai-analyst/
├── app.py # Streamlit frontend app
├── insights.py # Business insights module
├── llm_client.py # Reusable LLM client functions
├── pdf_parser.py # PDF parsing and text extraction
├── rag_pipeline.py # RAG pipeline setup and querying
├── summariser.py # Summarisation functions using LLM
├── requirements.txt # Project dependencies
├── .env # Environment variables (API keys)
└── README.md # Project documentation

---

## ⚙️ **Setup Instructions**
🚀 Quick Start
1. **Clone the repository**

```bash
git clone git@github.com:ethanhunt15/ML.git
cd ML/finai-analyst

2. Setup Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Configure .env
OPENAI_API_KEY=your_openai_key_here
GOOGLE_API_KEY=your_gemini_key_here
LLM_PROVIDER=openai   # or gemini

4. Run App
streamlit run app.py

🐳 Docker Deployment (Build and run with Docker)
docker build -t finai-analyst .
docker run -p 8501:8501 --env-file .env finai-analyst

---
ChromaDB is a vector database that stores embedded representations of ingested documents and performs fast similarity searches to retrieve contextually relevant chunks for downstream LLM querying in Retrieval-Augmented Generation pipelines.
---
app.py	=> Main Streamlit application: Handles UI, user inputs, and calls backend modules (PDF parsing, RAG pipeline, insights).
insights.py => Business Insights Module: Contains logic to derive actionable financial or operational insights from retrieved/summarised data.
llm_client.py	=> LLM Client Wrapper: Provides reusable functions to interact with GPT or Gemini models for summarisation, embeddings, or answering.
pdf_parser.py	=> PDF Parsing Module: Extracts raw text from uploaded PDFs using libraries like PyMuPDF or pdfplumber.
rag_pipeline.py => RAG Pipeline Implementation: Sets up vector store (ChromaDB), embeddings, and defines functions to ingest documents and query using Retrieval-Augmented Generation.
requirements.txt => Python dependencies list: Contains all required packages to run the project (LangChain, Streamlit, ChromaDB, etc.).
.env	=> Environment configuration file: Stores sensitive keys (OpenAI, Gemini API keys) and configurable variables used across modules.
summariser.py	=> Summarisation Module: Uses LLM to create concise summaries from parsed document texts for faster retrieval and insights generation.
---

🖼️ Architecture Diagram
📊 FinAI Analyst - RAG Pipeline Architecture
────────────────────────────────────────────────────

                ┌────────────────────────┐
                │      User Query        │
                └──────────┬─────────────┘
                           │
                           ▼
                ┌────────────────────────┐
                │  Streamlit Frontend    │
                └──────────┬─────────────┘
                           │
                           ▼
                ┌───────────────────────────────┐
                │      RAG Pipeline (Python)    │
                │                               │
                │ - load .env configs           │
                │ - query_rag(question)         │
                └──────────┬────────────────────┘
                           │
           ┌───────────────┼─────────────────────────────┐
           │                                             │
           ▼                                             ▼
 ┌────────────────────────────┐               ┌───────────────────────────────┐
 │     PDF Parsing Module     │               │   Vector DB (Chroma)          │
 │                            │               │ - Stores embeddings           │
 │ - Reads and extracts text  │──────────────►│ - Similarity search           │
 │   from uploaded PDFs       │               └──────────┬────────────────────┘
 └───────────┬────────────────┘                          │
             │                                           │
             ▼                                           │
 ┌────────────────────────────┐                          │
 │   Summarisation Module     │                          │
 │                            │                          │
 │ - Uses LLM to summarise    │                          │
 │   parsed PDF content       │                          │
 └───────────┬────────────────┘                          │
             │                                           │
             ▼                                           │
 ┌────────────────────────────┐                          │
 │   Embedding Model          │                          │
 │                            │                          │
 │ - OpenAI or Gemini         │◄─────────────────────────┘
 │ - Converts text chunks to  │
 │   embeddings               │
 └───────────┬────────────────┘
             │
             ▼
 ┌────────────────────────────┐
 │ Similarity Search Query    │
 │ - Embed user question      │
 │ - Retrieve top-k docs      │
 └───────────┬────────────────┘
             │
             ▼
 ┌────────────────────────────┐
 │   LLM Answer Generation    │
 │                            │
 │ - GPT-4o (OpenAI)          │
 │ - Gemini Pro/Flash (Google)│
 │ - Uses retrieved chunks    │
 │   + summaries as context   │
 └───────────┬────────────────┘
             │
             ▼
 ┌────────────────────────────┐
 │  Business Insights Module  │
 │                            │
 │ - Analyzes summarised and  │
 │   retrieved data to derive │
 │   actionable insights      │
 └───────────┬────────────────┘
             │
             ▼
 ┌─────────────────────────────┐
 │        Final Output         │
 │ - Answer + Summaries +      │
 │   Business Insights         │
 └─────────────────────────────┘

────────────────────────────────────────────────────
