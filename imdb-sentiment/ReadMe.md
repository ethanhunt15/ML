  
# IMDB Sentiment analysis

  

This project demonstrates a complete **MLOps-style pipeline** for a simple NLP use case — classifying movie reviews from the IMDB dataset as **positive** or **negative**.

  

It shows how to:

- Train an ML model in Python.

- Serve the model in a FastAPI microservice.

- Integrate the model server into a Java (Spring Boot) backend.

- Containerize everything with Docker Compose.

  
  

---

## ✨ Features

  

-  **End-to-End ML Workflow** – from training to serving in production-like setup.

-  **Real-Time Predictions** – REST APIs for sentiment classification.

-  **Polyglot Architecture** – Python for ML, Java (Spring Boot) for backend integration.

-  **Containerized Deployment** – each service runs as a separate Docker container.

-  **Configurable & Extensible** – easily swap the model or scale out the backend.

-  **MLOps-Aligned** – separates model training, serving, and orchestration layers.

  

---

  

## 🛠 Tech Stack

  

| Layer | Technology | Purpose |

|-------|-------------|---------|

| **Model Training** | Python, scikit-learn, Hugging Face Datasets | Train TF-IDF + Logistic Regression on IMDB dataset |

| **Model Persistence** | joblib (.pkl) | Save trained model |

| **Model Serving** | FastAPI | Serve model predictions over REST |

| **Backend Service** | Java 17, Spring Boot, Gradle | Provides API endpoint & forwards requests to FastAPI |

| **Containerization** | Docker, Docker Compose | Run both services together |

| **Development/IDE** | IntelliJ IDEA (Spring Boot), VSCode/Jupyter (Python) | Local dev and notebooks |

| **Optional Monitoring** | Spring Actuator (if enabled) | Health checks and metrics |

  

---

  

## 📂 Directory Structure

imdb-sentiment/

├── backend/ # Spring Boot backend project

├── data/ # (optional) raw / intermediate data

├── environment.yml / .yaml # Conda environment for Python ML code

├── frontend/ # (optional) UI / NodeJS project

├── models/

│ ├── lr_imdb_model.pkl # Saved Logistic Regression model

│ └── predict.py # Quick script to test the model

├── ReadMe.md # Project documentation

└── src/

├── baseline/

│ └── train_sklearn.py # Training script (scikit-learn)

├── serving/

│ ├── app.py # FastAPI app to serve predictions

│ ├── Dockerfile # FastAPI container

│ └── requirements.txt # Python dependencies for FastAPI

└── transform/

└── train_transformer.py # Transformer-based model

  

**Key Files**

-  `train_sklearn.py` – trains the model and saves `.pkl` under `models/`.

-  `app.py` – FastAPI app exposing `/predict` endpoint.

-  `predict.py` – standalone test script for the saved model.

-  `backend/` – Spring Boot service with `/predict` endpoint that calls FastAPI.

-  `Dockerfile` – container definition for each service.

-  `docker-compose.yml` – orchestrates containers (FastAPI + Spring Boot).

  

---

## 🏗 **Architecture**

  

  

```

┌──────────────────────┐

│ User / Client App    │

│ (sends review text)  │

└──────────┬───────────┘

           │ HTTP POST /predict

           ▼

┌────────────────────────────────────┐

│ Spring Boot Backend (port 8081)    │

│ - Receives /predict requests       │

│ - Calls FastAPI model server       │

└──────────┬─────────────────────────┘

           │ Internal network (Docker)

           ▼

┌──────────────────────────────────────┐

│ FastAPI Model Server (port 8080)     │

│ - Loads lr_imdb_model.pkl            │

│ - Predicts sentiment from text       │

└──────────┬───────────────────────────┘

           │

           ▼

┌──────────────────────────────────────┐

│ Logistic Regression Model (.pkl)     │

│ - TF-IDF + LR trained on IMDB        │

└──────────────────────────────────────┘


```

---

  

## ⚙️ Setup Instructions

  

### 1️⃣ Prerequisites

-  **Conda** (Miniconda or Anaconda)

-  **Docker & Docker Compose**

-  **Java 17** (if building Spring Boot locally)

  

### 2️⃣ Create Python Environment

```bash

conda  env  create  -f  environment.yml

conda  activate  imdb-sentiment

```

  

Train the model (optional if lr_imdb_model.pkl already exists):
```bash
python src/baseline/train_sklearn.py
```
This will produce models/lr_imdb_model.pkl.

  

### 3️⃣ Build Containers

From the project root:
```bash
docker compose build
```
  

### 4️⃣ Run Containers
```bash
docker compose up
```
  

This launches:

FastAPI at http://localhost:8080

Spring Boot at http://localhost:8081

  
  

### How to Test

  

Directly test FastAPI model server:
```bash
curl -X POST "http://localhost:8080/predict" \

-H "Content-Type: application/json" \

-d '{"text":"This movie was awesome!"}'

  ```

Expected response (JSON):

{"label": "positive", "probability": 0.91}

  

Test via Spring Boot backend:
```bash
curl -X POST "http://localhost:8081/predict" \

-H "Content-Type: application/json" \

-d '{"text":"This movie was awesome!"}'
  ```
  

Spring Boot forwards the request to FastAPI and returns the same JSON.

  

### Deploying / Extending

Replace lr_imdb_model.pkl with any new model trained by train_transformer.py or other scripts.

Adjust environment variable FASTAPI_URL in Spring Boot to point to external FastAPI service if needed.

Add more endpoints to FastAPI for batch predictions, model metrics, etc.

--- 
License
MIT License
---