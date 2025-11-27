from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Load the diabetes dataset
data = load_diabetes()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = XGBRegressor()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
#print("Predictions:", y_pred)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Save the trained model to a file
joblib.dump(model, 'xgboost_diabetes_model.pkl')
print("Model saved to xgboost_diabetes_model.pkl")