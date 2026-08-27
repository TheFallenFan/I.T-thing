from machine import Pin, PWM, ADC
from time import sleep

Potentiometer_Pin = ADC(26)
buzzer = PWM(0)
buzzer.freq(1000)

while True:
    PotentiometerValue = Potentiometer_Pin.read_u16()
    buzzer.duty_u16(PotentiometerValue)