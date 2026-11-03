#PortSeven
import network
import socket
from machine import Pin, ADC
from time import sleep

SSID = "Pixel_6178"
PASSWORD = "SecretMoney"
led = Pin(1, Pin.OUT)
Potentiometer = ADC(26)
wlan = network.WLAN(network.STA_IF)
receiver_ip = "10.22.0.118"
port = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    sleep(0.1)

print("Connected to Wi-Fi")
led.toggle()

try:
    while True:
        reading = Potentiometer.read_u16()
        message = str(reading)
        sock.sendto(message.encode(), (receiver_ip, port))
        sleep(0.02)

except KeyboardInterrupt:
    sock.close()
    led.toggle()
    print("Stopped")