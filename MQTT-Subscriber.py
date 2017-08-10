import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):  
        print("Connected with result code "+str(rc))
        client.subscribe("temperature")

def on_message(client, userdata, msg):  
        #Receive the message, and convert it to a string
        message = str(msg.payload)
        #The message has some characters that we need to remove using string slicing
        message = message[2:(len(message)-1)]
        #Show the message in the Python shell
        print(message)
"""
        if 
        elif 
        elif 
        else:
"""
#Create an object which we use to start a connection
client = mqtt.Client()  
#Run our on_connect function when a connection is required
client.on_connect = on_connect  
#Run our on_message function when a message is received
client.on_message = on_message  
#These are the details that we use to connect to our MQTT broker
client.connect("BROKER IP ADDRESS", 1883, 60)

client.loop_forever()  
