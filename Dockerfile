FROM python:3.10-slim

WORKDIR /app

# Copy the FastAPI app
COPY src/api.py /app/api.py

# Copy model
COPY xgb_diabetes_model.pkl /app/

# Copy requirements
COPY requirements.txt /app/

RUN pip install -r requirements.txt

# Start FastAPI (must use port 8080 for Lambda)
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]
