from machine import Pin
from time import sleep

LED = Pin("Led", Pin.OUT)

while True:
  led.toggle()
  sleep(0.25)
