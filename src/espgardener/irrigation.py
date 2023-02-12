from machine import Pin
import time

def irrigate(measurement):
    soil_hum = int(measurement["soil_hum"])
    sprinkler = Pin(2, Pin.OUT)
    period = 0
    if soil_hum < 75:
        sprinkler.value(True)
        period = soil_hum * -0.1 + 10
        time.sleep(period)
        sprinkler.value(False)
    return period    
