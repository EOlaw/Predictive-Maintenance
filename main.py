import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parameters
num_records = 10000
num_equipment = 10

# Generate timestamps
start_time = datetime(2024, 1, 1)
timestamps = [start_time + timedelta(hours=i) for i in range(num_records)]

# Generate equipment IDs
equipment_ids = np.random.randint(1, num_equipment + 1, num_records)

# Generate sensor data
sensor_1 = np.random.normal(0.5, 0.1, num_records)
sensor_2 = np.random.normal(0.3, 0.1, num_records)
sensor_3 = np.random.normal(0.4, 0.1, num_records)

# Generate environmental data
temperature = np.random.normal(22, 2, num_records)
humidity = np.random.normal(30, 5, num_records)
vibration = np.random.normal(0.05, 0.01, num_records)

# Generate maintenance flag
maintenance_flag = np.random.choice([0, 1], num_records, p=[0.95, 0.05])

# Create DataFrame
data = {
    'timestamp': timestamps,
    'equipment_id': equipment_ids,
    'sensor_1': sensor_1,
    'sensor_2': sensor_2,
    'sensor_3': sensor_3,
    'temperature': temperature,
    'humidity': humidity,
    'vibration': vibration,
    'maintenance_flag': maintenance_flag
}

df = pd.DataFrame(data)
df.to_csv('synthetic_maintenance_data.csv', index=False)
print("Data saved to synthetic_maintenance_data.csv")
