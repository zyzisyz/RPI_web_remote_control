#!python
# -*- coding: utf-8 -*- 
import datetime
from .Raspi_BMP085 import BMP085
import smbus2
from .am2320 import Am2320sensor

bmp = BMP085(0x77)
sensor = Am2320sensor()

def get_time():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("time:", now)
    return now


def get_temperature():
    #temp = bmp.readTemperature()
   
    temp = sensor.read()['temperature']
    print("Temperature: %.2f C" % temp)
    return float(temp)


def get_wet():
    #wet = 12
    humidity = sensor.read()['humidity']
    print("humidity:", humidity)
    return humidity


if __name__ == '__main__':
    sensor.setup()
    print("time:", get_time())
    print("temperature:", get_temperature())
    print("wet:", get_wet())
