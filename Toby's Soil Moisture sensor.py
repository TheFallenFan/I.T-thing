# Import the libraries for the pins, buzzer and sensors
from machine import Pin, PWM
from dht import DHT11
import time

# Set up the two sensors, the buzzer and the LED (valve)
s1 = DHT11(Pin(16))
s2 = DHT11(Pin(17))
buzzer = PWM(0)
buzzer.freq(500)
valve_led = Pin(15, Pin.OUT)

# Keep checking the moisture forever
while True:
    # Take a reading from both sensors and average them
    s1.measure()
    s2.measure()
    avg_moisture = (s1.humidity() + s2.humidity()) / 2

    # If the soil is too dry, turn on the LED and buzzer for 30 seconds
    if avg_moisture <= 49:
        valve_led.on()
        print(avg_moisture)
        print("watering")
        buzzer.duty_u16(16384)
        time.sleep(30)
        buzzer.duty_u16(0)
        valve_led.off()
    # Otherwise, don't water
    else:
        print("Enough moisture, not watering")

    # Print both readings and the average so we can check it's working
    print("average moisture is", str(avg_moisture) + "%", "(average of", s1.humidity(), "and", str(s2.humidity())+")")

    # Wait 1 second before checking again
    time.sleep(1)
