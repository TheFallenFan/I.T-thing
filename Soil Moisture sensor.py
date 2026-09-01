              from machine import ADC, Pin
import time

s1 = ADC(Pin(26))
s2 = ADC(Pin(27))
l = Pin(15, Pin.OUT)

while True:
    avg_moisture = (s1.read_u16() + s2.read_u16()) / 2
    
    if avg_moisture > 45000:
        l.on()
        time.sleep(30)
        l.off()
        
    time.sleep(1)
