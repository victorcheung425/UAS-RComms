import serial

class dynamixel_control:
	def __ini__(self):
		ser = serial.Serial(port='/dev/ttyACM0',baudrate=57600)

	def start_serial():
		ser.isOpen()
		ser.write('begin 57600' + '\r\n')
		ser.write('scan 10' + '\r\n')
		ser.write('sync_write_handler 1 Goal_Position' + '\r\n')
		ser.write('sync_write_handler 2 Goal_PWM' + '\r\n')
		ser.write('torque_on 1' + '\r\n')
		ser.write('torque_on 2' + '\r\n')

	def enable_motors():
		ser.write('torque_on 1' + '\r\n')
		ser.write('torque_on 2' + '\r\n')

	def disable_motors():
		ser.write('torque_off 1' + '\r\n')
		ser.write('torque_off 2' + '\r\n')

	def motor_pos(motor_1_pos, motor_2_pos):
		ser.write('sync_write 1 2 0 ' + motor_1_pos + ' ' + motor_2_pos + '\r\n')

	def motor_speeds(motor_1_speed, motor_2_speed):
		ser.write('sync_write 1 2 1 ' + motor_1_speed + ' ' + motor_2_speed + '\r\n')
