import math

# GPS Data Processing
# This function receives latitude and longitude in degrees, altitude in maters,
# and returns a pan and tilt angle in degrees pan is the angle to the north
# rotated to the east and tilt is the angle from horizontal upwards
def gps_process(drone_alt, ant_alt, drone_long, ant_long, drone_lat, ant_lat):

  earth_rad = 6371000.0
  
  # Common values
  b = earth_rad + drone_alt
  c = earth_rad + ant_alt

  b2 = b*b
  c2 = c*c
  bc2 = 2*b*c

  # Longitudinal calculations
  alpha = drone_long*1.0 - ant_long
  # Conversion to radian
  alpha = alpha*math.pi/180
  # Small-angle approximation
  # cos = 1 - alpha*alpha/2; //Math.cos(alpha)
  # Use the law of cosines
  x = alpha/abs(alpha)*math.sqrt(b2 + c2 - bc2*math.cos(alpha))

  # Repeat for latitudinal calculations
  alpha = drone_lat*1.0 - ant_lat
  alpha = alpha*math.pi/180
  y = alpha/abs(alpha)*math.sqrt(b2 + c2 - bc2*math.cos(alpha))

  # Obtain vertical difference, too
  z = drone_alt*1.0 - ant_alt

  r = math.sqrt(x*x+y*y+z*z)
  
  # tilt angle is from horizontal upwards
  tilt_angle = math.asin(z/r)

  # pan angle is from north to west:

  if y>0:  
    if x>0:
      pan_angle = math.atan(x/y) # quadrant 1
    else:
      pan_angle = -1.0*math.acos(y/(r*math.cos(tilt_angle))) # quadrant 4
  else:
    if x>0:
      pan_angle = math.pi-math.asin(x/(r*math.cos(tilt_angle))) # quadrant 2
    else:
      pan_angle = math.atan(x/y)-math.pi # quadrant 3

  # convert to degrees
  tilt_angle = tilt_angle*180/math.pi
  pan_angle = pan_angle*180/math.pi
  
  # returns pan and tilt angles in radians
  return (pan_angle,tilt_angle)

# GPS Data Processing Testbench

def main():
  drone_alt = 100
  ant_alt = 10
  drone_long = -123.3
  ant_long = -123.26
  drone_lat = 49.3
  ant_lat = 49.2631277

  (pan_angle,tilt_angle) = gps_process(drone_alt,ant_alt, drone_long, ant_long, drone_lat, ant_lat)
  print ("pan = {:10}" .format(pan_angle))
  print ("tilt = {:10}" .format(tilt_angle))

if __name__ == "__main__":
  main()

