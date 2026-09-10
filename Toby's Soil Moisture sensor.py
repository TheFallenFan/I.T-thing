from machine import Pin, PWM
from dht import DHT11
import time

s1 = DHT11(Pin(16))
s2 = DHT11(Pin(17))
buzzer = PWM(0)
buzzer.freq(500)
valve_led = Pin(15, Pin.OUT)

while True:
    s1.measure()
    s2.measure()
    avg_moisture = (s1.humidity() + s2.humidity()) / 2
    if avg_moisture <= 49:
        valve_led.on()
        print(avg_moisture)
        print("watering")
        buzzer.duty_u16(16384)
        time.sleep(30)
        buzzer.duty_u16(0)
        valve_led.off()
    else:
        print("Enough moisure, not watering")
    print("average moisture is", str(avg_moisture) + "%", "(average of", s1.humidity(), "and", str(s2.humidity())+")")
    time.sleep(1)
