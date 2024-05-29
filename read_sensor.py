import paho.mqtt.client as mqtt
import time
import mpu6050

# Define MQTT broker and topic
broker_address = "YOUR_MQTT_BROKER_ADDRESS"  # Replace with your broker's IP address or hostname
topic = "GYROSCOPE_DATA"

# Initialize MPU6050 sensor
mpu = mpu6050.MPU6050(0x68)
mpu.setup()

# Create MQTT client
client = mqtt.Client()

# Connect to MQTT broker
client.connect(broker_address)

while True:
    # Read gyroscope data
    gyro_data = mpu.get_gyro_data()

    # Create data payload (JSON format)
    data_payload = {
        "timestamp": time.time(),
        "gyroscope": {
            "x": gyro_data["x"],
            "y": gyro_data["y"],
            "z": gyro_data["z"]
        }
    }

    # Publish data to MQTT topic
    client.publish(topic, json.dumps(data_payload))

    # Wait for a short interval before next reading
    time.sleep(0.1)
