from machine import ADC, Pin
import time

ir_sensor = ADC(Pin(26))

while True:
    val = ir_sensor.read_u16()
    print("Raw Value:", val)
    time.sleep(0.5)