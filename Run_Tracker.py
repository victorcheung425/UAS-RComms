import math
import serial
import os
from decimal import *

from GPS_computation import gps_process
from ReadGPS import GPS_code
from motor_control import dynamixel_control

if __name__ == "__main__":
  #Hardcoded values: Change Later
  mag_angle = 90
  drone_alt = 100
  drone_lat = 49.25
  drone_long = -123 

  #Initialization
  ant_gps = GPS_code()
  ant_lat = 49
  ant_long = -123.1
  ant_alt = 1.5 #height of antenna tracker
  dynamix = dynamixel_control() #motor control instantiation
  dynamix.start_serial() #init serial

  while True:
    #receive antenna gps
    (ant_lat_temp,ant_long_temp) = ant_gps.get_gps()
    if(ant_lat_temp != 0):
      (ant_lat,ant_long) = (ant_lat_temp,ant_long_temp)
      print("Received AntLatLong")

    #compute pan/tilt
    (pan,tilt) = gps_process(drone_alt, ant_alt, drone_long, ant_long, drone_lat, ant_lat)
    pan = pan - mag_angle #normalizes pan to zero direction

    #motor control
    motor_pan = pan*4095*7/(360*3)
    motor_tilt = tilt*4095/360
    dynamix.motor_pos(motor_pan,motor_tilt) #set motor position
    
