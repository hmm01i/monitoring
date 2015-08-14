import serial

uno = serial.Serial('/dev/ttyACM0',9600)
while True:
    print uno.readline()