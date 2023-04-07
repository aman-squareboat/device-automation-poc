from typing import Union
from fastapi import FastAPI
import paho.mqtt.client as mqtt
import time
client = mqtt.Client()
client.connect("mosquitto.squareboat.info")
app = FastAPI()
def on_connect(*args):
    print(args)
def on_publish(client,userdata,result): 
    print("PUBLISHED MESSAGE")
client.on_publish = on_publish
client.on_connect = on_connect
client.publish("test","OFF")

@app.get("/house/light/toggle")
def toggle_light():
    sent,_ = client.publish(topic="house/light",payload="TOGGLE")
    if(sent != 0):
        client.connect("mosquitto.squareboat.info")
        client.publish(topic="house/light",payload="TOGGLE")
   
    # time.sleep(4)
    
    return "Toggling light"
