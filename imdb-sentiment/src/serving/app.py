from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

# app = FastAPI()

# MODEL_PATH = os.path.join(os.path.dirname(__file__), "lr_imdb_model.pkl")
# model = joblib.load(MODEL_PATH)

# class Review(BaseModel):
#     text: str

# @app.post("/predict")
# async def predict(review: Review):
#     pred = model.predict([review.text])[0]
#     proba = model.predict_proba([review.text])[0].max()
#     return {"label": int(pred), "probability": float(proba)}

#!/usr/bin/env python
"""
FastAPI app that can serve either:
1. A scikit-learn .pkl model
2. A Hugging Face transformer model
based on config.
"""

import os
from fastapi import FastAPI
from pydantic import BaseModel

# Config: choose between "sklearn" or "transformer"
MODEL_TYPE = os.getenv("MODEL_TYPE", "sklearn")  # default to sklearn

app = FastAPI(title="IMDB Sentiment API")

# ======================
#   1. Load Model
# ======================

if MODEL_TYPE == "sklearn":
    import joblib
    MODEL_PATH = os.getenv("MODEL_PATH", "../../models/lr_imdb_model.pkl")
    model = joblib.load(MODEL_PATH)

    def predict_fn(text: str):
        pred = model.predict([text])[0]
        prob = max(model.predict_proba([text])[0])
        return {
            "label": "positive" if pred == 1 else "negative",
            "probability": float(prob)
        }

elif MODEL_TYPE == "transformer":
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    import torch

    MODEL_DIR = os.getenv("MODEL_DIR", "../../models/distilbert-imdb")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)

    def predict_fn(text: str):
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
            pred = torch.argmax(probs, dim=-1).item()
            return {
                "label": "positive" if pred == 1 else "negative",
                "probability": float(probs[0][pred])
            }

else:
    raise ValueError("Unknown MODEL_TYPE: must be 'sklearn' or 'transformer'")

# ======================
#   2. FastAPI Endpoints
# ======================

class TextIn(BaseModel):
    text: str

@app.get("/")
def health():
    return {"status": "ok", "model_type": MODEL_TYPE}

@app.post("/predict")
def predict(input: TextIn):
    return predict_fn(input.text)
