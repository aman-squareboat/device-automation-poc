import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # Set pin numbering mode to BCM

def toggle_pin(pin):
    GPIO.setup(pin, GPIO.OUT)  # Set the pin as an output
    GPIO.output(pin, not GPIO.input(pin)) 

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if "TOGGLE" in msg.payload:
        toggle_pin(18)
        print("Toggleing pin 18")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.subscribe("house/light")

client.loop_forever()