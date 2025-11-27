FROM public.ecr.aws/lambda/python:3.10

# Install Python dependencies
COPY requirements.txt  .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy your application code
COPY src/ ${LAMBDA_TASK_ROOT}/
COPY xgboost_diabetes_model.pkl ${LAMBDA_TASK_ROOT}/

# Set handler
CMD ["api.handler"]
