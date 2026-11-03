from machine import ADC, Pin, PWM
from time import sleep

Potentiometer = ADC(26)
servo = PWM(0)

max_duty = 7537
min_duty = 2294
stop_duty = 0

frequency = 50
servo.freq(frequency)


def clockwisefull():
    servo.duty_u16(min_duty)
#     print("Turning Right")
def stop():
    servo.duty_u16(stop_duty)
#     print("Stopping")
def counterclockwisefull():
    servo.duty_u16(max_duty)
#     print("Turning Left")
try:
    
    while True:
        PotentiometerValue = Potentiometer.read_u16()
        print(PotentiometerValue)
        if 50000 < PotentiometerValue < 64534:
            stop()
        elif PotentiometerValue < 45000:
            counterclockwisefull()
        elif PotentiometerValue == 65535:
            clockwisefull()
        else:
            print("Look man, ranges are hard.")
        sleep(0.01)

except KeyboardInterrupt:
    print("Stopped")
    servo.deinit()
