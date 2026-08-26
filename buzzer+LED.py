from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(1))
buzzer.freq(500)
led = Pin(0, Pin.OUT)

while True:
    led.toggle()
    buzzer.duty_u16(50000)
    sleep(0.5)
    buzzer.duty_u16(0)
    led.toggle()
    sleep(0.5)
