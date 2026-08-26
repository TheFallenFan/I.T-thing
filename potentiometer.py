from machine import ADC, Pin, PWM
from time import sleep

Potentiometer = ADC(26)

while True:
    PotentiometerValue = Potentiometer.read_u16()
    print(PotentiometerValue)
    sleep(0.1)
#You should be able to just use the "potentiometervalue" for use in other things, and you could also divide by 65535 and times by 100 to get an
#Aproximate percentage value
