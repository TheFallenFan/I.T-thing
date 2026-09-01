from machine import Pin
from time import sleep

greenled = Pin(0, Pin.OUT)
yellowled = Pin(1, Pin.OUT)
redled = Pin(2, Pin.OUT)

greenled.value(1)
sleep(0.5)
greenled.value(0)
yellowled.value(1)
sleep(0.5)
yellowled.value(0)
redled.value(1)
sleep(0.5)
redled.value(0)