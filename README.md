# Synthetic Data Generation Script

## Overview

This script generates a synthetic dataset to simulate maintenance data for multiple pieces of equipment. The data includes timestamps, sensor readings, environmental conditions, and maintenance flags, designed to resemble real-world monitoring scenarios in industries such as manufacturing or IoT.

The dataset is saved in a CSV file, `synthetic_maintenance_data.csv`, which can be used for testing, machine learning, or statistical analysis.

---

## Code Summary

### 1. **Libraries Used**
- **`pandas`**: To structure the generated data into a tabular format (DataFrame) and save it as a CSV file.
- **`numpy`**: To generate random data for numerical fields like sensor readings and environmental conditions.
- **`datetime`**: To create timestamps for the data.

---

### 2. **Parameters**
- **`num_records`**: Total number of records to generate (10,000 in this example).
- **`num_equipment`**: Number of unique equipment IDs to simulate (10).

---

### 3. **Data Generation**

#### Timestamps
- Start from January 1, 2024.
- Increment by one hour for each record.

#### Equipment IDs
- Randomly assigned integers between 1 and `num_equipment` (inclusive).

#### Sensor Data
- **`sensor_1`**: Random values following a normal distribution with mean `0.5` and standard deviation `0.1`.
- **`sensor_2`**: Random values with mean `0.3` and standard deviation `0.1`.
- **`sensor_3`**: Random values with mean `0.4` and standard deviation `0.1`.

#### Environmental Data
- **Temperature**: Normal distribution with mean `22°C` and standard deviation `2°C`.
- **Humidity**: Normal distribution with mean `30%` and standard deviation `5%`.
- **Vibration**: Normal distribution with mean `0.05` and standard deviation `0.01`.

#### Maintenance Flag
- Randomly set as `1` (requires maintenance) or `0` (does not require maintenance).
- Probability distribution: 95% `0` and 5% `1`.

---

### 4. **Output**
The generated data is stored in a `pandas` DataFrame and saved as a CSV file:
- File Name: `synthetic_maintenance_data.csv`
- **Columns**:
  - `timestamp`: Date and time of the record.
  - `equipment_id`: Unique identifier for each piece of equipment.
  - `sensor_1`, `sensor_2`, `sensor_3`: Simulated sensor readings.
  - `temperature`, `humidity`, `vibration`: Simulated environmental conditions.
  - `maintenance_flag`: Indicates whether maintenance is needed (`1`) or not (`0`).

---

## Purpose and Applications

### Purpose
This script is designed for creating a large, structured dataset for scenarios where:
- Real-world data is unavailable or difficult to access.
- Testing algorithms for predictive maintenance, anomaly detection, or data visualization.

### Potential Applications
- **Machine Learning**: Training models to predict maintenance needs based on sensor and environmental data.
- **Statistical Analysis**: Studying the distribution and correlation of variables in maintenance scenarios.
- **Testing Pipelines**: Validating data ingestion and processing pipelines.

---

## Improvements and Customization

### Possible Enhancements
- Increase the number of sensors or environmental parameters.
- Add complex dependencies between variables (e.g., higher vibration correlating with maintenance needs).
- Simulate equipment-specific variations or failure patterns.

### Customization
- Adjust the `num_records` and `num_equipment` parameters for datasets of different sizes.
- Modify the probability distribution of the maintenance flag based on domain-specific requirements.

---

## Conclusion

This script provides a straightforward way to generate realistic synthetic maintenance data. By simulating various factors like sensor readings and environmental conditions, it enables robust testing and development of analytical tools and predictive models.
