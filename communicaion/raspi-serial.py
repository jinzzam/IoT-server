# this code will be run in raspberry pi

import serial
from socketIO_client import SocketIO, LoggingNamespace

ser = serial.Serial(
    port='/dev/cu.usbmodem1411',
    baudrate='9600',
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)


def on_connect():
    print('Connected!')


def on_reconnect():
    print('Reconnected.')


def on_disconnect():
    print('Disconnected..')


with SocketIO('localhost', 8801, LoggingNamespace, wait_for_connection=True, resource='socket.io',
              hurry_interval_in_seconds=1) as socketIO:
    socketIO.on('connect', on_connect())
    socketIO.on('disconnect', on_disconnect())

try:
    while 1:
        response = ser.readline()
        realResponse = response.decode('utf-8')[:len(response) - 1]
        print(realResponse)

except KeyboardInterrupt:
    ser.close()
