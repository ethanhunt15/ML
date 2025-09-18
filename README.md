
# Machine Learning Projects Repository

This repository contains multiple ML and AI projects, each in its own folder.

Each project has its own README with detailed instructions, code, and requirements.

---
  

## 📂 Projects Overview

  
| Project | Description |
|--|--|
| **[finai-analyst](finai-analyst/)** | Generative AI-powered **Financial Analyst RAG pipeline** to parse PDFs, summarize content, derive insights, and answer queries using OpenAI / Google Gemini LLMs. |
|**[IMDB Sentiment Analysis](imdb-sentiment/)**  |End-to-end **MLOps-style NLP pipeline** for classifying IMDB movie reviews as positive or negative; includes TF-IDF + Logistic Regression and Transformer-based models, served via FastAPI and integrated with Spring Boot backend. |
  
---

  

## ⚙️ Setup Instructions

  

### 1. Clone Repository

```bash

git  clone  https://github.com/ethanhunt15/ML.git

cd  ML

```

### 2. Install Python Environment

Each project may have its own dependencies listed in requirements.txt or environment.yml.

For example, to create a conda environment:

```bash
conda  env  create  -f  environment.yml

conda  activate  ML
```

### 3. Running a Project

Navigate to the project folder:

```bash
cd  finai-analyst  # or any other project
```

Install project-specific dependencies if needed:

```bash
pip  install  -r  requirements.txt
```

Follow project README for training or running the pipeline:

```bash
python  run_pipeline.py  # for finai-analyst

python  src/baseline/train_sklearn.py  # for IMDB Sentiment Analysis
```


### Tech Stack Overview

 - Python: Data processing, ML model training, Hugging Face Transformers
 -  scikit-learn: Traditional ML models (Logistic Regression, Random
   Forest)
 - PyTorch: Deep learning (LSTM, Transformer models)
 - FastAPI: Model serving
 - Docker: Containerization and MLOps workflow
 - LangChain / RAG: For retrieval-augmented generation pipelines
 - Pandas / NumPy / PyPDF2: Data extraction and preprocessing
