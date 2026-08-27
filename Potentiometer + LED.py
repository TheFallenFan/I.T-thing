from machine import Pin, ADC, PWM
from time import sleep
Potentiometer_Pin = ADC(26)
LED_Pin = PWM(0)
LED_Pin.freq(1000)
while True:
    PotentiometerValue = Potentiometer_Pin.read_u16()
    LED_Pin.duty_u16(PotentiometerValue)
    print(PotentiometerValue)

