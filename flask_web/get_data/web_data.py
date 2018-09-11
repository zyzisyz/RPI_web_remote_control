#!python
# -*- coding: utf-8 -*- 
import datetime
from .Raspi_BMP085 import BMP085

bmp = BMP085(0x77)


def get_time():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("time:", now)
    return now


def get_temperature():
    temp = bmp.readTemperature()
    print("Temperature: %.2f C" % temp)
    return float(temp)


def get_wet():
    wet = 12
    
    print("wet:", wet)
    return wet


if __name__ == '__main__':
    print("time:", get_time())
    print("temperature:", get_temperature())
    print("wet:", get_wet())
