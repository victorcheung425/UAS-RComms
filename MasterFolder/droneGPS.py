#/usr/bin/env python
# -*- coding: utf-8 -*-

"""
© Copyright 2015-2016, 3D Robotics.
vehicle_state.py: 

Demonstrates how to get and set vehicle state and parameter information, 
and how to observe vehicle attribute (state) changes.

Full documentation is provided at http://python.dronekit.io/examples/vehicle_state.html
"""
from __future__ import print_function
from dronekit import connect, VehicleMode
import time

#Set up option parsing to get connection string
import argparse

class droneGPS:
    def __init__ (self,lat=0,lon=0,alt=0,vehicle=0):
        self.lat = lat
        self.lon = lon
        self.alt = alt
        self.vehicle = vehicle

    def connect_drone (self):
    #self.vehicle = connect(connection_string, wait_ready=['gps_0'], baud = 57600, heartbeat_timeout = 60)
	self.vehicle = connect('/dev/ttyUSB0', wait_ready=['gps_0'], baud=57600, heartbeat_timeout=60)

    def return_gps_coordinates (self):
        self.lat = self.vehicle.location.global_relative_frame.lat
        self.lon = self.vehicle.location.global_relative_frame.lon
        self.alt = self.vehicle.location.global_relative_frame.alt
        return(self.lat,self.lon,self.alt)

"""
# Code for Testing
def main():
    gps = droneGPS()
    gps.connect_drone()
    while True:
        (lat,lon,alt) = gps.return_gps_coordinates()
        print ("lat = {:10}" .format(lat))
        print ("lon = {:10}" .format(lon))
        print ("alt = {:10}" .format(alt))

if __name__ == "__main__":
    main()
"""