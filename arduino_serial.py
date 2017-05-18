import serial

uno = serial.Serial('/dev/ttyACM0',9600)
while True:
    try:
        val = int(uno.readline())
        if val != 0:
            print val
    except ValueError:
            print "we got a strange value"

