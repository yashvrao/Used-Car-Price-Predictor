from db_connection import load_data, get_connection_string
from preprocess import preprocess_data
from sklearn.model_selection import train_test_split
from train_model import train_and_evaluate
import joblib
import pandas as pd
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

connection_string = get_connection_string()
query = "SELECT * FROM used_cars"

data = load_data(query, connection_string)
data = preprocess_data(data)

# Ensure there are no NaN values in the target variable
data = data.dropna(subset=['price'])

X = data.drop('price', axis=1)
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model, mse, r2 = train_and_evaluate(X_train, X_test, y_train, y_test)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

var_price = data['price'].var()
print(f"Variance of Price: {var_price}")

joblib.dump(model, 'used_car_price_model.pkl')
joblib.dump(X.columns, 'model_columns.pkl')