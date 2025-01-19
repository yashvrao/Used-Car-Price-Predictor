import pandas as pd
from sqlalchemy import create_engine
from db_connection import get_connection_string

def load_csv_to_db(csv_file):
    connection_string = get_connection_string()
    engine = create_engine(connection_string)
    
    data = pd.read_csv(csv_file)
    data.to_sql('used_cars', engine, if_exists='append', index=False)

if __name__ == "__main__":
    csv_file = 'path_to_your_csv_file.csv'
    load_csv_to_db(csv_file)
