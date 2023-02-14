from machine import Pin
import time

sprinkler = Pin(2, Pin.OUT)
sprinkler.value(True)

def irrigate(measurement):
    soil_hum = int(measurement["soil_hum"])
    period = 0
    if soil_hum < 75:
        sprinkler.value(False)
        period = soil_hum * -0.1 + 10
        time.sleep(period)
        sprinkler.value(True)
    return period    
 