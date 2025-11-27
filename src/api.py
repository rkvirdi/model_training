from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum
import numpy as np
import pickle

app = FastAPI()

# Input model
class Features(BaseModel):
    features: list[float]

# Load the trained model
with open("xgboost_diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Diabetes Prediction API"}

@app.post("/predict")
def predict(input_data: Features):
    # Convert list to numpy array
    features_array = np.array(input_data.features).reshape(1, -1)

    # Predict using the model
    prediction = model.predict(features_array)[0]

    # Determine risk
    risk = get_risk(prediction)

    return {
        "prediction": float(prediction),
        "risk_level": risk
    }

def get_risk(prediction_value: float):
    if prediction_value < 100:
        return "Low Risk"
    elif prediction_value < 200:
        return "Medium Risk"
    else:
        return "High Risk"

# Lambda handler
handler = Mangum(app)
