from machine import Pin, PWM
from time import sleep

freq_num = 10000

redLED = PWM(Pin(0))
greenLED = PWM(Pin(1))
blueLED = PWM(Pin(2))
redLED.freq(freq_num)
greenLED.freq(freq_num)
blueLED.freq(freq_num)

def setColor(r, g, b):
    redLED.duty_u16(r*256)
    greenLED.duty_u16(g*256)
    blueLED.duty_u16(b*256)
    
red   = 0
green = 0
blue  = 0

setColor(red, green, blue)
sleep(5)

