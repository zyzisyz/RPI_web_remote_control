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





def IR_turn_on():
    pass


def IR_turn_off():
    pass


def IR_turn_down(state):
    if state == 17:
        print('ir_down')
        os.system('irsend SEND_ONCE AIR KEY_16')
    elif state == 18:
        print('ir_down')
        os.system('irsend SEND_ONCE AIR KEY_17')
    elif state == 19:
        print('ir_down')
        os.system('irsend SEND_ONCE AIR KEY_18')
    elif state == 20:
        print('ir_down')
        os.system('irsend SEND_ONCE AIR KEY_19')
    elif state == 21:
        print('ir_down')
        os.system('irsend SEND_ONCE AIR KEY_20')
    elif state == 22:
        print('ir_down')
        os.system('irsend SEND_ONCE AIR KEY_21')
    elif state == 23:
        print('ir_down')
        os.system('irsend SEND_ONCE AIR KEY_22')
    elif state == 24:
        print('ir_down')
        os.system('irsend SEND_ONCE AIR KEY_23')
    elif state == 25:
        print('ir_down')
        os.system('irsend SEND_ONCE AIR KEY_24')
    elif state == 26:
        print('ir_down')
        os.system('irsend SEND_ONCE AIR KEY_25')
    elif state == 27:
        print('ir_down')
        os.system('irsend SEND_ONCE AIR KEY_26')
    elif state == 28:
        print('ir_down')
        os.system('irsend SEND_ONCE AIR KEY_27')
    elif state == 29:
        print('ir_down')
        os.system('irsend SEND_ONCE AIR KEY_28')
    elif state == 30:
        print('ir_down')
        os.system('irsend SEND_ONCE AIR KEY_29')
    else:
        pass


def IR_turn_up(state):
    if state == 16:
        print('ir_up')
        os.system('irsend SEND_ONCE AIR KEY_17')
    elif state == 17:
        print('ir_up')
        os.system('irsend SEND_ONCE AIR KEY_18')
    elif state == 18:
        print('ir_up')
        os.system('irsend SEND_ONCE AIR KEY_19')
    elif state == 19:
        print('ir_up')
        os.system('irsend SEND_ONCE AIR KEY_20')
    elif state == 20:
        print('ir_up')
        os.system('irsend SEND_ONCE AIR KEY_21')
    elif state == 21:
        print('ir_up')
        os.system('irsend SEND_ONCE AIR KEY_22')
    elif state == 22:
        print('ir_up')
        os.system('irsend SEND_ONCE AIR KEY_23')
    elif state == 23:
        print('ir_up')
        os.system('irsend SEND_ONCE AIR KEY_24')
    elif state == 24:
        print('ir_up')
        os.system('irsend SEND_ONCE AIR KEY_25')
    elif state == 25:
        print('ir_up')
        os.system('irsend SEND_ONCE AIR KEY_26')
    elif state == 26:
        print('ir_up')
        os.system('irsend SEND_ONCE AIR KEY_27')
    elif state == 27:
        print('ir_up')
        os.system('irsend SEND_ONCE AIR KEY_28')
    elif state == 28:
        print('ir_up')
        os.system('irsend SEND_ONCE AIR KEY_29')
    elif state == 29:
        print('ir_up')
        os.system('irsend SEND_ONCE AIR KEY_30')
    else:
        pass


def LED_turn_on():
    GPIO.output(37, GPIO.LOW)
    print("LED turn on")


def LED_turn_off():
    GPIO.output(37, GPIO.HIGH)
    print("LED turn off")


if __name__ == '__main__':
    print("this is rpi")
