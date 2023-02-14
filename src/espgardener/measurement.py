import dht
import time
from machine import ADC, Pin
from time_utils import *

SOIL_HUM_MIN = 26
SOIL_HUM_MAX = 51

global soil_detector   
def measure():
    
    d = dht.DHT22(Pin(4))
    d.measure()
    
    global soil_detector
    soil_detector = ADC(Pin(34))
    soil_detector.atten(ADC.ATTN_11DB)
    print(soil_detector.read())
    value = soil_detector.read() #// -40.96 +100
    measurement = {
        "air_temp":d.temperature(),
        "air_hum":d.humidity(),
        "soil_hum":value
        }
    return (measurement)