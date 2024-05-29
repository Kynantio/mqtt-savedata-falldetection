import paho.mqtt.client as mqtt
import time

# Definisikan alamat dan topik broker MQTT
broker_address = (34, 101, 198, 128)
topic = "DATA_GIROSKOP"

# Inisialisasi pustaka sensor (ganti dengan pustaka spesifik Anda)
sensor_lib = "fall-detection/sensor/gyro"  # Ganti dengan pustaka aktual untuk sensor Anda

# Buat klien MQTT
client = mqtt.Client()

# Hubungkan ke broker MQTT
client.connect(broker_address)

while True:
    # Baca data giroskop menggunakan fungsi pustaka sensor
    gyro_data = sensor_lib.read_sensor_data()  # Ganti dengan panggilan fungsi yang sebenarnya

    # Buat muatan data (format JSON)
    data_payload = {
        "timestamp": time.time(),
        "giroskop": {
            "x": gyro_data["x"],
            "y": gyro_data["y"],
            "z": gyro_data["z"]
        }
    }

    # Publikasikan data ke topik MQTT
    client.publish(topic, json.dumps(data_payload))

    # Tunggu interval singkat sebelum pembacaan berikutnya
    time.sleep(0.1)
