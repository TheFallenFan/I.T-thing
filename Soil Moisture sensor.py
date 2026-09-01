from machine import ADC, Pin
import time

s1 = ADC(Pin(26))
s2 = ADC(Pin(27))
valve_led = Pin(15, Pin.OUT)

while True:
    avg_moisture = (s1.read_u16() + s2.read_u16()) / 2
    if avg_moisture > 45000:
        valve_led.on()
        time.sleep(30)
        valve_led.off()
    time.sleep(1)
