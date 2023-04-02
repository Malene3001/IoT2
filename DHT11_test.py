from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(14))
g = Pin(21, Pin.OUT, value=0)
y = Pin(22, Pin.OUT, value=0)
r = Pin(23, Pin.OUT, value=0)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print('Temperature: %3.1f C' %temp)
        print('Humidity: %3.1f %%' %hum)
        sleep(2)
    except OSError as e:
        print('Failed to read sensor.')
        
    if temp > 4 and temp <= 7:
        g.value(1)
        y.value(0)
        r.value(0)
    elif temp > 7 and temp <= 9:
        y.value(1)
        g.value(0)
        r.value(0)
    elif temp > 9:
        r.value(1)
        g.value(0)
        y.value(0)
    else:
        g.value(0)
        y.value(0)
        r.value(0)
