import sys
sys.path.append('/espgardener/package')

import wifimgr
from time import sleep
import machine

def run(debug=False):
    wlan = wifimgr.get_connection()
    if wlan is None:
        if debug:
            print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D

def deactivate(debug=False):
    wifi_lib.disconnect()
    
