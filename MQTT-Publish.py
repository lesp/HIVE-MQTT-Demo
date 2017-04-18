import time
import paho.mqtt.client as mqtt
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
client = mqtt.Client()
client.connect("192.168.1.147", 1883, 60)
while True:
    temp = sensor.get_temperature()
    client.publish("temperature",temp)
    print(temp)
    time.sleep(10)
