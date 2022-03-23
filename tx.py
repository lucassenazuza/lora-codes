from time import sleep
import serial

ser = serial.Serial(
        port='/dev/ttyUSB1', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
while True:
    ser.write(b"0123456789abcdefgh")
    sleep(1)