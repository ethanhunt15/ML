# Use a slim Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy FastAPI app
COPY src/serving/app.py .

# Copy requirements first for layer caching
COPY src/serving/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your trained model into the container
COPY models/lr_imdb_model.pkl ./lr_imdb_model.pkl

# Expose FastAPI port
EXPOSE 8080

# Run FastAPI with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
