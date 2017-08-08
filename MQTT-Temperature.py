import time
import paho.mqtt.client as mqtt
from envirophat import weather
client = mqtt.Client()
client.connect("BROKER IP ADDRESS", 1883, 60)
while True:
    temp = weather.temperature()
    client.publish("temperature",temp)
    print(temp)
    time.sleep(10)
