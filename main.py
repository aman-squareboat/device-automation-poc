from typing import Union
from fastapi import FastAPI
import paho.mqtt.client as mqtt
import time
client = mqtt.Client()
app = FastAPI()
def on_connect(*args):
    print(args)
def on_publish(*args): 
    print("PUBLISHED MESSAGE")
    print(args)
client.on_publish = on_publish
client.on_connect = on_connect
client.publish("test","OFF")

@app.get("/house/light/toggle")
def toggle_light():

    client.connect("mosquitto.squareboat.info")
    client.publish(topic="house/light",payload="TOGGLE")
   
    # time.sleep(4)
    
    return "Toggling light"
