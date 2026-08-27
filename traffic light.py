from machine import Pin, PWM
from time import sleep

freq_num = 10000

redLED = PWM(Pin(0))
greenLED = PWM(Pin(1))
blueLED = PWM(Pin(2))
redLED.freq(freq_num)
greenLED.freq(freq_num)
blueLED.freq(freq_num)

def set_led(r, g, b):
    red = r*257
    green = g*257
    blue = b*257
    return red, green, blue

def change_LED(red, green, blue):
    redLED.duty_u16(red)
    greenLED.duty_u16(green)
    blueLED.duty_u16(blue)

while True:
    change_LED(*set_led(255, 0, 0))
    sleep(3)
    for i in range (0, 5):
        change_LED(*set_led(255, 43, 0))
        sleep(0.5)
        change_LED(*set_led(0, 0, 0))
        sleep(0.5)
    change_LED(*set_led(0, 255, 0))
    sleep(3)


#You should be able to change triggers easily for this one
