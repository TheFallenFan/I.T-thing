from import machine import Pin, ADC
import dht
import time 

soil_sensor = ADC(26)
potentiometer = ADC(27)
dht_sensor = dht.DHT11(
