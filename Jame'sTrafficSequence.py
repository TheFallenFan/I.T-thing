from machine import Pin
from time import sleep

# Traffic light LEDs
greenled = Pin(0, Pin.OUT)
yellowled = Pin(1, Pin.OUT)
redled = Pin(2, Pin.OUT)

# PIR motion sensor
pir = Pin(3, Pin.IN)

def lights_off():
    greenled.value(0)
    yellowled.value(0)
    redled.value(0)

def normal_cycle():
    # GREEN
    lights_off()
    greenled.value(1)

    for i in range(50):
        if pir.value() == 1:
            return True
        sleep(0.1)

    # YELLOW
    lights_off()
    yellowled.value(1)

    for i in range(20):
        if pir.value() == 1:
            return True
        sleep(0.1)

    # RED
    lights_off()
    redled.value(1)

    for i in range(50):
        if pir.value() == 1:
            return True
        sleep(0.1)

    return False


lights_off()

while True:

    # Check for motion
    if pir.value() == 1:

        print("MOTION DETECTED!")
        print("Giving green light priority")

        # Yellow before changing
        lights_off()
        yellowled.value(1)
        sleep(1)

        # Give priority to traffic
        lights_off()
        greenled.value(1)
        sleep(5)

        # Return to red
        lights_off()
        redled.value(1)
        sleep(2)

    else:

        print("No motion detected")

        # Run normal traffic cycle
        normal_cycle()
