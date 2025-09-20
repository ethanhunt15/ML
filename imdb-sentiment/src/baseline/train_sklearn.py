import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,accuracy_score
from sklearn.model_selection import train_test_split
from datasets import load_dataset


ds = load_dataset("imdb")
X = ds["train"]["text"]
y = ds["train"]["label"]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.15, random_state=42)
print(f"Train size: {len(X_train)}, Validation size: {len(X_val)}")

# convert raw text to a sparse matrix of word/bi-gram features (max 30k).
# then train a LogisticRegression (saga): fast linear classifier with L2 regularization.
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=30000,ngram_range=(1,2))),
    ('clf', LogisticRegression(max_iter=1000,C=1.0, solver='saga', n_jobs=-1))
])
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_val)

# print precision, recall, F1, and support.
print(classification_report(y_val, y_pred))
print("Accuracy:", accuracy_score(y_val, y_pred))

# save the entire pipeline for reuse
joblib.dump(pipeline, "models/lr_imdb_model.pkl")