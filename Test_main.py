from hmc5883l import HMC5883L
import smbus


bus = smbus.SMBus(1)
mag = HMC5883L(bus,0x1e,0x00)

while True:
    bearing = mag.read_bearing()
    print bearing



