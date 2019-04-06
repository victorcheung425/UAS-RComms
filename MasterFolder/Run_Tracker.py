import math
import serial
import os
import time
from decimal import *
from dronekit import connect, VehicleMode

from GPS_computation import gps_process
from ReadGPS import GPS_code
from motor_control import dynamixel_control
from droneGPS import droneGPS

if __name__ == "__main__":
  #Hardcoded values: Change Later
  mag_angle = 0
  """
  drone_alt_array = [0, 250, 500, 750, 1000, 750, 500, 250]
  drone_alt = 0
  drone_lat_array = [49.2715, 49.267993, 49.261776, 49.253954, 49.251517, 49.255943, 49.262609, 49.27521]
  drone_lat = 49
  drone_long = -123
  drone_long_array = [-123.243634, -123.233109, -123.228903, -123.232626, -123.247743, -123.259502, -123.266025, -123.257614]
  index = 0;
  """
  #Initialization
  drone_gps = droneGPS()
  drone_lat = 0
  drone_long = 0
  drone_alt = 0
  drone_lat_temp = 0
  drone_long_temp = 0
  drone_alt_temp = 0
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
  drone_gps.connect_drone() #connect to drone's RFD

  while True:
    #receive antenna gps
    while(ant_lat_temp == 0):
      (ant_lat_temp,ant_long_temp) = ant_gps.get_gps()
    (ant_lat,ant_long) = (float(ant_lat_temp),float(ant_long_temp))

    #receive drone gps
    if(drone_gps.check_heartbeat()):
      drone_gps.connect_drone()
    while(drone_lat_temp == 0):
      (drone_lat_temp,drone_long_temp,drone_alt_temp) = drone_gps.return_gps_coordinates();
    (drone_lat,drone_long,drone_alt) = (float(drone_lat_temp),float(drone_long_temp),float(drone_alt_temp))
    (drone_lat_temp,drone_long_temp,drone_alt_temp) = (0,0,0)
	
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