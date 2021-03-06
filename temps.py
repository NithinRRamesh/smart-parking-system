import paho.mqtt.client as mqtt
import time

def on_log(client,userdata,level,buff):
    print("log:",buff)

    
def on_connect(client,userdata,flags,rc):
    if(rc == 0):
        print("connected ok")
    else:
        print("bad connection returned code=",rc)
def on_disconnect(client,userdata,flags,rc=0):
    print("Disconnection result code : ",rc)

def on_message(client,userdata,msg):
    topic = msg.topic
    print("got message")
    print(msg.payload.decode("utf-8"))
broker = "test.mosquitto.org"

client = mqtt.Client("nithin2")

client.on_connect = on_connect
client.on_log = on_log
client.on_disconnect = on_disconnect
client.on_message = on_message

print("connecting to broker...",broker)
client.connect(broker)
client.subscribe("temp")
client.publish("temp","my first message")
client.loop_forever()
client.disconnect()
