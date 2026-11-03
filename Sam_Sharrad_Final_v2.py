from machine import ADC, Pin, PWM
from time import sleep

Potentiometer = ADC(26)
servo = PWM(Pin(0))
servo.freq(50)

min_duty = 2500
max_duty = 7000


try:
    while True:
        reading = Potentiometer.read_u16()

        duty = min_duty + (reading * (max_duty - min_duty) // 65535)
        servo.duty_u16(duty)
        #print("Pot:", reading, "Duty:", duty)
        sleep(0.02)

except KeyboardInterrupt:
    servo.deinit()
    print("Stopped")