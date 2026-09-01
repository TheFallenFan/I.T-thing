import machine
import dht
import time

sensor = dht.DHT11(machine.Pin(16))

while True:

    sensor.measure()
    temp = str(sensor.temperature()) + "°C"
    hum = str(sensor.humidity()) + "%"
    print("Temperature:", temp, "| Humidity:" ,hum)
    time.sleep(1)
