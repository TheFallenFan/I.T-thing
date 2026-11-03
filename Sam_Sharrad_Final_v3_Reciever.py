#PortFive
import network
import socket
from machine import Pin, PWM
from time import sleep

SSID = "Pixel_6178"
PASSWORD = "SecretMoney"
led = Pin(1, Pin.OUT)
buzzer = PWM(Pin(15))
min_duty = 2500
max_duty = 7000
port = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
wlan = network.WLAN(network.STA_IF)
servo = PWM(Pin(0))

buzzer.freq(500)
servo.freq(50)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    sleep(0.1)

print("Connected to Wi-Fi")
led.toggle()


sock.bind(("0.0.0.0", port))

print("Waiting for potentiometer data...")
buzzer.duty_u16(1000)
sleep(1)
buzzer.duty_u16(0)
try:
    while True:
        data, address = sock.recvfrom(1024)
        reading = int(data.decode())
        duty = min_duty + (reading * (max_duty - min_duty) // 65535)
        servo.duty_u16(duty)

except KeyboardInterrupt:
    sock.close()
    servo.deinit()
    led.toggle()
    print("Stopped")