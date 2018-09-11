#!python
# -*- coding: utf-8 -*- 
import os


def LED_turn_on():
    os.system('irsend SEND_ONCE AIR KEY_OPEN')


def LED_turn_off():
    os.system('irsend SEND_ONCE AIR KEY_OFF')
    

def LED_shine():
    pass





if __name__ == '__main__':
    pass
