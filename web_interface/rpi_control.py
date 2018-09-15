#!python
# -*- coding: utf-8 -*-
import os
import time

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)
except:
    print("can not import GPIO")


def LED_turn_on():
    GPIO.output(37, GPIO.LOW)
    print("LED turn on")


def LED_turn_off():
    GPIO.output(37, GPIO.HIGH)
    print("LED turn off")


if __name__ == '__main__':
    print("this is rpi")
