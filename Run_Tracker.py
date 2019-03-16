import math
import serial
import os
from decimal import *

from GPS_computation import gps_process
from ReadGPS import GPS_code

drone_alt = 100
drone_lat = 49.25
drone_long = -123

if __name__ == "__main__":
  mag_angle = 90
  ant_alt = 1.5 #height of antenna tracker
  ant_gps = GPS_code()
  ant_lat = 49
  ant_long = -123.1

  while True:
    (ant_lat_temp,ant_long_temp) = ant_gps.get_gps()
    if(ant_lat_temp != 0):
      (ant_lat,ant_long) = (ant_lat_temp,ant_long_temp)
      print("Received LatLong")
#Insert code to receive drone_lat, drone_long, and drone_alt
    (pan,tilt) = gps_process(drone_alt, ant_alt, drone_long, ant_long, drone_lat, ant_lat)
    pan = pan - mag_angle #normalizes pan to zero direction
#Send command to motors here
