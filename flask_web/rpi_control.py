#!python
import os


def IR_turn_on():
    os.system('irsend SEND_ONCE AIR KEY_OPEN')


def IR_turn_off():
    os.system('irsend SEND_ONCE AIR KEY_OFF')


def IR_turn_up():
    os.system('irsend SEND_ONCE AIR KEY_UP')


def IR_turn_down():
    os.system('irsend SEND_ONCE AIR KEY_DOWN')


def LED_turn_on():
    pass


def LED_turn_off():
    pass


def LED_shine():
    pass


if __name__ == '__main__':
    pass
