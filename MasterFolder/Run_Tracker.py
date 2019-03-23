import math
import serial
import os
import time
from decimal import *

from GPS_computation import gps_process
from ReadGPS import GPS_code
from motor_control import dynamixel_control

if __name__ == "__main__":
  #Hardcoded values: Change Later
  mag_angle = 0
  drone_alt_array = [0, 250, 500, 750, 1000, 750, 500, 250]
  drone_alt = 0
  drone_lat_array = [49.2715, 49.267993, 49.261776, 49.253954, 49.251517, 49.255943, 49.262609, 49.27521]
  drone_lat = 49
  drone_long = -123
  drone_long_array = [-123.243634, -123.233109, -123.228903, -123.232626, -123.247743, -123.259502, -123.266025, -123.257614]
  index = 0;
  #Initialization
  ant_gps = GPS_code()
  ant_lat = 0
  ant_lat_temp = 0
  ant_long = 0
  ant_long_temp = 0
  ant_alt = 1.5 #height of antenna tracker
  prev_pan = 0
  new_pan = 0
  pan = 0
  dynamix = dynamixel_control() #motor control instantiation
  dynamix.start_serial() #init serial

  while True:
    #receive antenna gps
    while(ant_lat_temp == 0):
      (ant_lat_temp,ant_long_temp) = ant_gps.get_gps()
    (ant_lat,ant_long) = (float(ant_lat_temp),float(ant_long_temp))

    if (index == 7):
      index = 0
    else:
      index += 1
    drone_alt = drone_alt_array[index]
    drone_long = drone_long_array[index]
    drone_lat = drone_lat_array[index]
    dynamix.read_serial()
    time.sleep(0.5)

    #compute pan/tilt

    (new_pan,tilt) = gps_process(drone_alt, ant_alt, drone_long, ant_long, drone_lat, ant_lat)
    new_pan = new_pan - mag_angle #normalizes pan to zero direction

    if (new_pan - prev_pan <= -180):
      pan += new_pan - prev_pan + 360
    elif (new_pan - prev_pan >= 180):
      pan += new_pan - prev_pan - 360
    else:
      pan += new_pan - prev_pan

    prev_pan = new_pan

    #motor control
    motor_pan = pan*4095/(360)*4 #gear ratio
    motor_tilt = tilt*4095/360
    dynamix.motor_pos(motor_pan,motor_tilt) #set motor position
    print "pan: " + str(motor_pan) + " tilt: " + str(motor_tilt)

