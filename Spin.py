from machine import Pin, PWM
from time import sleep

servo = PWM(0)

max_duty = 7537
min_duty = 2294
stop_duty = 0

frequency = 50
servo.freq (frequency)

def clockwisefull():
    servo.duty_u16(min_duty)
    sleep(2)
def stop():
    servo.duty_u16(stop_duty)
    sleep(2)
def counterclockwisefull():
    servo.duty_u16(max_duty)
    sleep(2)

try:
    while True:
        clockwisefull()
        stop()
        counterclockwisefull()
      
except KeyboardInterrupt:
    print("Stopped")
    servo.deinit()