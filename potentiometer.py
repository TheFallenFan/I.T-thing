from machine import ADC, Pin, PWM
from time import sleep

Potentiometer = ADC(26)

while True:
    PotentiometerValue = Potentiometer.read_u16()
    print(PotentiometerValue)
    sleep(0.1)
