import serial

class dynamixel_control:
	def __ini__(self,ser=0):
		self.ser = ser

	def start_serial(self):
		self.ser = serial.Serial(port='/dev/ttyACM0',baudrate=57600)
		self.ser.isOpen()
		self.ser.write('begin 57600' + '\r\n')
		self.ser.write('scan 10' + '\r\n')
		self.ser.write('sync_write_handler 1 Goal_Position' + '\r\n')
		self.ser.write('sync_write_handler 2 Goal_PWM' + '\r\n')
		self.ser.write('torque_on 1' + '\r\n')
		self.ser.write('torque_on 2' + '\r\n')

	def enable_motors(self):
		self.ser.write('torque_on 1' + '\r\n')
		self.ser.write('torque_on 2' + '\r\n')

	def disable_motors(self):
		self.ser.write('torque_off 1' + '\r\n')
		self.ser.write('torque_off 2' + '\r\n')

	def motor_pos(self,motor_1_pos, motor_2_pos):
		self.ser.write('sync_write 1 2 0 ' + str(motor_1_pos) + ' ' + str(motor_2_pos) + '\r\n')

	def motor_speeds(self,motor_1_speed, motor_2_speed):
		self.ser.write('sync_write 1 2 1 ' + str(motor_1_speed) + ' ' + str(motor_2_speed) + '\r\n')
	def read_serial(self):
		out = ''
		while self.ser.inWaiting() > 0:
			out += self.ser.read(1)
		if out != '':
			print (">>" + out)