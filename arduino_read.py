import serial

ard = serial.Serial('/dev/ttyS0', 9600)
while True:
    print ard.readline()