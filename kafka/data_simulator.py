""" 
Simulates sensor data for 10 reefer trucks and sends messages to a Kafka topic.
"""
import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

# Configuration
KAFKA_BROKER = 'localhost:9092'
TOPIC = 'reefer-sensor-data'
NUM_TRUCKS = 10

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_sensor_data(truck_id):
    """Simulate sensor data for a truck."""
    data = {
        "truck_id": truck_id,
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(-5, 10), 2),
        "humidity": round(random.uniform(60, 100), 2),
        "vibration": round(random.uniform(0, 5), 2),
        "pressure": round(random.uniform(0.8, 1.2), 2)
    }
    return data

if __name__ == "__main__":
    while True:
        for truck_id in range(1, NUM_TRUCKS + 1):
            sensor_data = generate_sensor_data(truck_id)
            producer.send(TOPIC, sensor_data)
            print(f"Sent data: {sensor_data}")
        time.sleep(2)  # simulate data every 2 seconds