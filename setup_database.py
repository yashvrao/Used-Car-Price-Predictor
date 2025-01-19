import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

def get_connection_string():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    database = os.getenv('DB_NAME')
    return f"mysql+pymysql://{user}:{password}@{host}/{database}"

def setup_database():
    connection_string = get_connection_string()
    engine = create_engine(connection_string)
    
    try:
        with engine.connect() as connection:
            connection.execute("CREATE DATABASE IF NOT EXISTS UsedCarPricePredictor;")
            connection.execute("USE UsedCarPricePredictor;")
            connection.execute("""
                CREATE TABLE IF NOT EXISTS used_cars (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    year INT,
                    miles INT,
                    city_mileage FLOAT,
                    highway_mileage FLOAT,
                    horsepower INT,
                    torque INT,
                    engine_capacity_litre FLOAT,
                    fuel_capacity FLOAT,
                    num_cylinder INT,
                    num_seat INT,
                    num_owners INT,
                    doors INT,
                    wheel_drive INT,
                    speed_levels INT,
                    front_headroom FLOAT,
                    front_legroom FLOAT,
                    rear_headroom FLOAT,
                    rear_legroom FLOAT,
                    service_records INT,
                    brand VARCHAR(255),
                    model VARCHAR(255),
                    type VARCHAR(255),
                    engine_type VARCHAR(255),
                    price FLOAT,
                    link VARCHAR(255),
                    condition INT
                );
            """)
            
        print("Database setup completed successfully.")
    except SQLAlchemyError as e:
        print(f"Error setting up the database: {e}")

if __name__ == "__main__":
    setup_database()
