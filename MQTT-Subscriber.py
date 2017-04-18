import paho.mqtt.client as mqtt
from gpiozero import LED

red = LED(17)



def on_connect(client, userdata, flags, rc):  
        print("Connected with result code "+str(rc))
        client.subscribe("temperature")

def on_message(client, userdata, msg):  
        message = str(msg.payload)
        message = message[2:(len(message)-1)]
        message = float(message)
        print(message)
        if message < 10.0 and message >= 0.0:
                print(message)
                red.blink(1,1)
        elif message >= 10.0 and message < 20:
                print(message)
                red.blink(0.5,0.5)
        elif message >=20 and message <30:
                print(message)
                red.blink(0.25,0.25)
        

client = mqtt.Client()  
client.on_connect = on_connect  
client.on_message = on_message  
client.connect("192.168.1.147", 1883, 60)

client.loop_forever()  
