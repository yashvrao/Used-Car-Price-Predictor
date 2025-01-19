import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def preprocess_data(data):
    numeric_data = data.select_dtypes(include=[np.number])
    numeric_data.fillna(numeric_data.median(), inplace=True)
    
    for col in numeric_data.columns:
        q1 = numeric_data[col].quantile(0.25)
        q3 = numeric_data[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        numeric_data = numeric_data[(numeric_data[col] >= lower_bound) & (numeric_data[col] <= upper_bound)]
    
    non_numeric_data = data.select_dtypes(exclude=[np.number])
    data = pd.concat([numeric_data, non_numeric_data], axis=1)
    
    data = pd.get_dummies(data, columns=['brand', 'model', 'type', 'engine_type', 'wheel_drive'], drop_first=True)
    scaler = StandardScaler()
    num_cols = ['year', 'miles', 'city_mileage', 'highway_mileage', 'horsepower', 'torque', 'engine_capacity_litre', 'fuel_capacity', 'num_cylinder', 'num_seat', 'num_owners', 'doors', 'speed_levels', 'front_headroom', 'front_legroom', 'rear_headroom', 'rear_legroom', 'service_records']
    data[num_cols] = scaler.fit_transform(data[num_cols])
    data = data.drop(columns=['id', 'link', 'condition'])
    return data