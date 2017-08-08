import time
import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("BROKER IP ADDRESS", 1883, 60)
while True:
    temp = "WHERE IS THE TEMPERATURE?"
    client.publish("temperature",temp)
    print(temp)
    time.sleep(10)
