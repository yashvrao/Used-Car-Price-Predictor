import pandas as pd
from sqlalchemy import create_engine
import os

def load_data(query, connection_string):
    engine = create_engine(connection_string)
    data = pd.read_sql(query, engine)
    return data

def get_connection_string():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    database = os.getenv('DB_NAME')
    return f"mysql+pymysql://{user}:{password}@{host}/{database}"