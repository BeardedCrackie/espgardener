import sys
sys.path.append('/espgardener/package')

import measurement
import irrigation
import configurator
import data_visualization

import machine
import os
import esp32

def run(debug=False, test=False):
    
    if debug:
        if machine.reset_cause() == machine.DEEPSLEEP_RESET:
            print('woke from a deep sleep') 
    
    configurator.run(debug)
    values = measurement.measure()
    iri_time = irrigation.irrigate(values)
    if debug:
        print("dht values: {}".format(values))
        print("iri time: {}".format(iri_time))
    data = list()
    for x in values.values():
        data.append(x)
    data.append(iri_time)
    data_visualization.print_to_thingspeak(data, debug=debug, test=test)
    configurator.deactivate(debug=debug)
    
    sleep_time = 150000
    
    if debug:
        print("deep sleep for: {}ms".format(sleep_time))
    machine.deepsleep(sleep_time)
    
