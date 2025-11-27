FROM public.ecr.aws/lambda/python:3.10

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all source code
COPY src/ ./src
COPY xgboost_diabetes_model.pkl .

# Lambda handler command (ASGI)
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8080"]
