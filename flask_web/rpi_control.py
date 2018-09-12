#!python
# -*- coding: utf-8 -*-
import os
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)


def IR_turn_on():
    pass


def IR_turn_off():
    pass


def IR_turn_down():
    pass


def IR_turn_up():
    pass


def LED_turn_on():
    GPIO.output(37, GPIO.LOW)
    print("LED turn on")


def LED_turn_off():
    GPIO.output(37, GPIO.HIGH)
    print("LED turn off")


def LED_shine():
    while True:
        GPIO.output(37, GPIO.LOW)
        time.sleep(1)
        print("turn on")
        GPIO.output(37, GPIO.HIGH)
        print("turn off")
        time.sleep(1)


if __name__ == '__main__':
    n = input("model:")
    while n == 1 or n == 2 or n == 3:
        if n == 1:
            LED_shine()
        elif n == 2:
            LED_turn_on()
        elif n == 3:
            LED_turn_off()
