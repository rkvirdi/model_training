from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Pydantic model for input
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
    prediction = model.predict(features_array)[0]   # numpy value

    # Determine risk
    risk = get_risk(prediction)

    # Return everything
    return {
        "prediction": float(prediction),
        "risk_level": risk
    }


def get_risk(prediction_value):
    if prediction_value < 100:
        return "Low Risk"
    elif prediction_value < 200:
        return "Medium Risk"
    else:
        return "High Risk"
    
    