import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(port='/dev/ttyACM0',baudrate=57600)

ser.isOpen()
ser.write('begin 57600 \r\n')
ser.write('scan 10 \r\n')

ser.write('write 1 Torque_Enable 0 \r\n')
ser.write('reboot 1 \r\n')
ser.write('write 1 Operating_Mode 4 \r\n')
ser.write('write 1 LED 1 \r\n')
ser.write('write 1 Torque_Enable 1 \r\n')
ser.write('write 2 Torque_Enable 0 \r\n')
ser.write('reboot 2 \r\n')
ser.write('write 2 Operating_Mode 4 \r\n')
ser.write('write 2 LED 1 \r\n')
ser.write('write 2 Torque_Enable 1 \r\n')

ser.write('sync_write_handler 1 Goal_Position \r\n')
ser.write('sync_write_handler 2 Goal_PWM \r\n')

time.sleep(3)
out = ''
while ser.inWaiting() > 0:
	out += ser.read(1)
if out != '':
	print (out)

print ('Enter your commands below.\r\nInsert "exit" to leave the application.')

input=1
while 1 :
    input = raw_input(">> ")
    if input == 'exit':
        ser.close()
        exit()
    elif input[0:9] == 'move both':
        ser.write('sync_write 1 2 0 ' + input[10:] + '\r\n')
    elif input[0:4] == 'move':
        ser.write('write ' + input[5] + ' Goal_Position ' + input[7:] + '\r\n')
    elif input[0:10] == 'speed both':
        ser.write('sync_write 1 2 1 ' + input[11:] + '\r\n')
    elif input[0:5] == 'speed':
        ser.write('write ' + input[6] + ' Goal_PWM ' + input[8:] + '\r\n')
    else:
        ser.write(input + '\r\n')
    out = ''
    
    time.sleep(0.5)	
    while ser.inWaiting() > 0:
        out += ser.read(1)
    if out != '':
        print (">>" + out)
