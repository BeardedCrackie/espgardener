import sys
sys.path.append('/espgardener/package')

import ssd1306
import network
import esp32
import urequests
from machine import Pin, SoftI2C
import time

api_key = 'HGR8BTLZCGD9351I'


def print_to_thingspeak(data, debug=False, test=True):
    if debug:    
        print("writing to thingspeak")
    HTTP_HEADERS = {'Content-Type': 'application/json'}
    vals = {}
    for x in range(len(data)):
        vals['field{}'.format(x+1)] = data[x]   
    if not test:
        request = urequests.post('http://api.thingspeak.com/update?api_key={}&'.format(api_key),
                                  json = vals, headers = HTTP_HEADERS)
        request.close()
    if debug:    
        print("pushed: {} to thingspeak:{}".format(vals, api_key))
    #request.close()
        
    i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    display.scroll(36, 0) 
    display.text('Air temp: {}'.format(data[0]), 0, 0, 1)
    display.text('Air hum: {}'.format(data[1]), 0, 12, 1)
    display.text('Soil hum: {}'.format(data[2]), 0, 24, 1)
    display.text('Last irri: {}s'.format(data[3]), 0, 36, 1)
    display.contrast(120)  # bright
    display.show()
    
print("Data visualizator loaded.")