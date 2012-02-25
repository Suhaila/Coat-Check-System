# This script is used to write to the Arduino and ultimately send the hanger number to the Arduino to transmit

# importing modules to be used in the script
import serial

# Testing whether the Arduino is connected
try:  
    arduino = serial.Serial('COM3', 9600)  
	
except:  
    print "Failed to connect on COM3" 

# Get input from user
num = ''
while (num != 'Exit'):
	num = raw_input('Enter a hanger number:')

	# Writing to the Ardino
	try:  
		arduino.write(num)  
		#time.sleep(1)  
		#print arduino.readline()
		#print arduino.readline()  	
	except:
		print "Failed to send!"