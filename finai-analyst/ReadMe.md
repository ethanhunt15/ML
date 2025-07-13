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
```
finai-analyst/
├── app.py # Main Streamlit application: Handles UI, user inputs, and calls backend modules (PDF parsing, RAG pipeline, insights).
├── insights.py # Business Insights Module: Contains logic to derive actionable financial or operational insights from retrieved/summarised data.
├── llm_client.py # LLM Client Wrapper: Provides reusable functions to interact with GPT or Gemini models for summarisation, embeddings, or answering.
├── pdf_parser.py # PDF Parsing Module: Extracts raw text from uploaded PDFs using libraries like PyMuPDF or pdfplumber.
├── rag_pipeline.py # RAG Pipeline Implementation: Sets up vector store (ChromaDB), embeddings, and defines functions to ingest documents and query using Retrieval-Augmented Generation.
├── summariser.py # Summarisation Module: Uses LLM to create concise summaries from parsed document texts for faster retrieval and insights generation.
├── requirements.txt # Python dependencies list: Contains all required packages to run the project (LangChain, Streamlit, ChromaDB, etc.).
├── .env # Environment configuration file: Stores sensitive keys (OpenAI, Gemini API keys) and configurable variables used across modules.
└── README.md # Project documentation
```
---

## 🏗 **Architecture**

```
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

```

---

## ⚙️ **Setup Instructions**

1. **Clone the repository**

```bash
git clone git@github.com:ethanhunt15/ML.git
cd ML/finai-analyst
```

2. **Create virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Add environment variables**

Create a `.env` file with:

```
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key
```

5. **Run the app**

```bash
streamlit run app.py
```

---

## 🔑 **Environment Variables**

| Variable         | Description                |
| ---------------- | -------------------------- |
| OPENAI\_API\_KEY | Your OpenAI API key        |
| GOOGLE\_API\_KEY | Your Google Gemini API key |

---

## 📌 **Requirements**

- Python 3.9+
- OpenAI / Gemini API keys
- Streamlit
- LangChain
- ChromaDB

---

## ✨ **Future Enhancements**

- Multi-LLM orchestration for cost-performance optimisation
- Fine-tuned business insights module for domain-specific KPIs
- RAG pipeline performance benchmarking
- Deployment on cloud (AWS Lambda / GCP Cloud Run)

---

## 📝 **License**

MIT License.

---

## 🙌 **Acknowledgements**

Built as a FinTech Generative AI showcase integrating **LangChain, ChromaDB, OpenAI, and Gemini** for robust document understanding and insights generation.

---

```

---

