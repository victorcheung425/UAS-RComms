#/usr/bin/python
import serial
import os
from decimal import *

class GPS_code:
   def __init__(self,fix=0,gps_con=0,ser=0):
      self.fix = fix
      self.gps_con = gps_con
      self.ser = ser

   def get_gps(self):
      # check for gps connected on USB0 or USB1
      if self.gps_con == 0 and os.path.exists('/dev/serial0') == True:
         self.ser = serial.Serial('/dev/serial0',9600,timeout = 10)
         print(self.ser.name);
         self.gps_con = 1
         print "connected on UART"
      if self.gps_con == 1:
         gps = self.ser.readline()
#         print (gps);
         if gps[1 : 6] == "GNGGA":
            gps1 = gps.split(',',14)
#            print gps
         if gps[1:6] == "GNGSA":
            self.fix = int(gps[9:10])
         if gps[1 : 6] == "GNGGA" and len(gps) > 68 and (gps1[3] == "N" or gps1[3] == "S")and self.fix > 1:
            lat = int(gps[17:19]) + (Decimal(Decimal(gps[19:26]))/(Decimal(60))) #+ (Decimal(int(gps[22:26]))/(Decimal(3600000)))
            if gps[28:29] == "S":
               lat = 0 - lat
            lon = int(gps[30:33]) + (Decimal(Decimal(gps[33:40]))/(Decimal(60))) #+ (Decimal(int(gps[36:40]))/(Decimal(3600000)))
            if gps[42:43] == "W":
               lon = 0 - lon
            return (lat,lon)
         return (0,0)
#         print "LAT:" ,lat
#         print "LON:",lon
#         print ""

#      if gps[1 : 6] == "GPRMC" and fix > 1:
#         gps2 = gps.split(',',14)
#         print "SPEED:",gps2[7]
#         print "ANGLE:",gps2[8]
#         print ""

# Code for Testing
#def main():
#  getcontext().prec=8
#  gps_inst = GPS_code()
#  while True:
#    (lat,long) = gps_inst.get_gps()
#    print ("lat = {:10}" .format(lat))
#    print ("lon = {:10}" .format(long))
#
#if __name__ == "__main__":
#  main()


