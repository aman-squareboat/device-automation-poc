from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import paho.mqtt.client as mqtt
import time
client = mqtt.Client()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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

@app.get("/house/fan/toggle")
def toggle_fan():

    client.connect("mosquitto.squareboat.info")
    client.publish(topic="house/fan",payload="TOGGLE")
   
    # time.sleep(4)
    
    return "Toggling fan"
@app.get("/house/socket/toggle")
def toggle_socket():

    client.connect("mosquitto.squareboat.info")
    client.publish(topic="house/socket",payload="TOGGLE")
   
    # time.sleep(4)
    
    return "Toggling socket"
@app.get("/house/ac/toggle")
def toggle_ac():

    client.connect("mosquitto.squareboat.info")
    client.publish(topic="house/ac",payload="TOGGLE")
   
    # time.sleep(4)
    
    return "Toggling ac"
