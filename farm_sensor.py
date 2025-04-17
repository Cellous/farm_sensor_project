import time
import random
import csv
from datetime import datetime

# Simulated sensor read (normally use Adafruit_DHT, GPIO, etc.)
def read_sensors():
    return {
        'temperature': round(random.uniform(65, 85), 2),
        'humidity': round(random.uniform(30, 70), 2),
        'soil_ph': round(random.uniform(5.5, 7.5), 2),
    }

def save_to_csv(data, file='sample_data/sensor_data.csv'):
    with open(file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), data['temperature'], data['humidity'], data['soil_ph']])

# Main loop
if __name__ == "__main__":
    print("Logging sensor data...")
    for _ in range(5):  # Simulate 5 readings
        sensor_data = read_sensors()
        save_to_csv(sensor_data)
        print("Logged:", sensor_data)
        time.sleep(2)
