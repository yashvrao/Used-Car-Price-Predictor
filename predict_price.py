import joblib
import pandas as pd
from preprocess import preprocess_data
from db_connection import get_connection_string
from sqlalchemy import create_engine

def get_user_input():
    user_input = {
        'year': int(input("Enter the year of the car: ")),
        'miles': int(input("Enter the miles driven: ")),
        'city_mileage': int(input("Enter the city mileage: ")),
        'highway_mileage': int(input("Enter the highway mileage: ")),
        'horsepower': int(input("Enter the horsepower: ")),
        'torque': int(input("Enter the torque: ")),
        'engine_capacity_litre': float(input("Enter the engine capacity in litres: ")),
        'fuel_capacity': float(input("Enter the fuel capacity: ")),
        'num_cylinder': int(input("Enter the number of cylinders: ")),
        'num_seat': int(input("Enter the number of seats: ")),
        'num_owners': int(input("Enter the number of previous owners: ")),
        'doors': int(input("Enter the number of doors: ")),
        'wheel_drive': int(input("Enter the wheel drive type (e.g., 2, 4): ")),
        'speed_levels': int(input("Enter the number of speed levels: ")),
        'front_headroom': float(input("Enter the front headroom: ")),
        'front_legroom': float(input("Enter the front legroom: ")),
        'rear_headroom': float(input("Enter the rear headroom: ")),
        'rear_legroom': float(input("Enter the rear legroom: ")),
        'service_records': int(input("Enter the number of service records: ")),
        'brand': "brand_" + input("Enter the brand of the car: "),
        'model': "model_" + input("Enter the model of the car: "),
        'type': "type_" + input("Enter the type of the car (e.g., sedan): "),
        'engine_type': "engine_type_" + input("Enter the engine type (e.g., gas, hybrid_gas_electric): ")
    }
    return pd.DataFrame([user_input])

def main():
    model = joblib.load('used_car_price_model.pkl')
    model_columns = joblib.load('model_columns.pkl')
    user_input = get_user_input()
    
    # Load some data to get the structure for preprocessing
    connection_string = get_connection_string()
    engine = create_engine(connection_string)
    sample_data = pd.read_sql("SELECT * FROM used_cars LIMIT 1", engine)
    
    # Append user input to sample data for preprocessing
    combined_data = pd.concat([sample_data, user_input], ignore_index=True)
    processed_data = preprocess_data(combined_data)
    
    # Extract the processed user input
    processed_user_input = processed_data.iloc[-1:].drop(columns=['price'])
    
    # Ensure the processed user input has the same columns as the model
    processed_user_input = processed_user_input.reindex(columns=model_columns, fill_value=0)
    
    prediction = model.predict(processed_user_input)
    print(f"The predicted price of the car is: ${prediction[0]:,.2f}")

if __name__ == "__main__":
    main()
