#/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from dronekit import connect, VehicleMode
import time

#Set up option parsing to get connection string
import argparse

class droneGPS:
    def __init__ (self,prev_heartbeat=0,vehicle=0):
        self.vehicle = vehicle
        self.prev_heartbeat = prev_heartbeat

    def connect_drone (self):
        #self.vehicle = connect(connection_string, wait_ready=['gps_0'], baud = 57600, heartbeat_timeout = 60)
	    self.vehicle = connect('/dev/ttyUSB0', wait_ready=['gps_0'], baud=57600, heartbeat_timeout=60)

    def check_heartbeat(self):
        if((self.prev_heartbeat != self.vehicle.last_heartbeat) or (self.vehicle.last_heartbeat <= 5)):
            self.prev_heartbeat = self.vehicle.last_heartbeat
            reconnect = 0
        else:
        	reconnect = 1
        return reconnect

    def return_gps_coordinates (self):
        lat = self.vehicle.location.global_relative_frame.lat
        lon = self.vehicle.location.global_relative_frame.lon
        alt = self.vehicle.location.global_relative_frame.alt
        return(lat,lon,alt)

"""
# Code for Testing
def main():
    gps = droneGPS()
    gps.connect_drone()
    while True:
        if(gps.check_heartbeat()):
            gps.connect_drone()
        (lat,lon,alt) = gps.return_gps_coordinates()
        print ("lat = {:10}" .format(lat))
        print ("lon = {:10}" .format(lon))
        print ("alt = {:10}" .format(alt))

if __name__ == "__main__":
    main()
"""