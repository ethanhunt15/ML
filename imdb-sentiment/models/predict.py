import joblib

# Load the model once
model = joblib.load("lr_imdb_model.pkl")

# Example usage
examples = [
    "The acting was brilliant and I loved the story!",
    "Terrible movie, I want my money back."
]

preds = model.predict(examples)
for text, label in zip(examples, preds):
    print(f"{text} → {'Positive' if label == 1 else 'Negative'}")
