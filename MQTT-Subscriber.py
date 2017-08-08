import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):  
        print("Connected with result code "+str(rc))
        client.subscribe("temperature")

def on_message(client, userdata, msg):  
        message = str(msg.payload)
        message = message[2:(len(message)-1)]
        message = float(message)
        print(message)
"""
        if 
        elif 
        elif 
        else:
"""

client = mqtt.Client()  
client.on_connect = on_connect  
client.on_message = on_message  
client.connect("BROKER IP ADDRESS", 1883, 60)

client.loop_forever()  
