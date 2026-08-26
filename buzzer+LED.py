from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(15))
buzzer.freq(500)
led = Pin(0, Pin.OUT)

while True:
    led.toggle()
    sleep(0.5)
    buzzer.duty_u16(1000)
    sleep(1)
    buzzer.duty_u16(0)