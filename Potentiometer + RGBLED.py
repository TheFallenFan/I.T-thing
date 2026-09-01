from machine import Pin, ADC, PWM
from time import sleep

Potentiometer1_Pin = ADC(26)
Potentiometer2_Pin = ADC(27)
Potentiometer3_Pin = ADC(28)

RED_Pin = PWM(0)
GREEN_Pin = PWM(1)
BLUE_Pin = PWM(2)

RED_Pin.freq(1000)
BLUE_Pin.freq(1000)
GREEN_Pin.freq(1000)


while True:
    RED_Pin.duty_u16(Potentiometer1_Pin.read_u16())
    GREEN_Pin.duty_u16(Potentiometer2_Pin.read_u16())
    BLUE_Pin.duty_u16(Potentiometer3_Pin.read_u16())

