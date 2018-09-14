# -*- coding: utf-8 -*-

import sqlite3
from flask import Flask, request, session, g, redirect, url_for,\
    abort, render_template, flash
import os
import rpi_control
import threading
from time import sleep
import time


try:
    from get_data import web_data
    print("import web_data successfully!")
except:
    print("can not import web_data moudle")


app = Flask(__name__)

state = 0
degree = 26
signal = [
    'irsend SEND_ONCE AIR KEY_OFF', 'irsend SEND_ONCE AIR KEY_16',
    'irsend SEND_ONCE AIR KEY_17', 'irsend SEND_ONCE AIR KEY_18',
    'irsend SEND_ONCE AIR KEY_19', 'irsend SEND_ONCE AIR KEY_20',
    'irsend SEND_ONCE AIR KEY_21', 'irsend SEND_ONCE AIR KEY_22',
    'irsend SEND_ONCE AIR KEY_23', 'irsend SEND_ONCE AIR KEY_24',
    'irsend SEND_ONCE AIR KEY_25', 'irsend SEND_ONCE AIR KEY_26',
    'irsend SEND_ONCE AIR KEY_27', 'irsend SEND_ONCE AIR KEY_28',
    'irsend SEND_ONCE AIR KEY_29', 'irsend SEND_ONCE AIR KEY_30'
]


def return_fun():
    global state
    try:
        temp = web_data.get_temperature()
        wet = web_data.get_wet()
    except:
        temp = 26.6
        wet = 12.2
    if state != 0:
        return render_template('index.html', methods=['POST'],
                               Temperature=temp, Wet=wet, Degree=degree)
    else:
        return render_template('index.html', methods=['POST'],
                               Temperature=temp, Wet=wet, Degree=0)


@app.route('/')
def hello_world():
    return return_fun()


@app.route('/index/')
def index():
    return return_fun()


@app.route('/IR_ON/')
def ir_on():
    global degree
    global state
    print('ir_on')
    os.system(signal[degree-15])
    state = 1
    return return_fun()


@app.route('/IR_OFF/')
def ir_off():
    global state
    print('ir_off')
    os.system(signal[0])
    state = 0
    return return_fun()


@app.route("/IR_UP/")
def ir_up():
    global degree
    global state
    if state != 0 and degree < 30:
        os.system(signal[degree-14])
        degree += 1
    else:
        pass
    return return_fun()


@app.route("/IR_DOWN/")
def ir_down():
    global degree
    global state
    if state != 0 and degree > 16:
        print("ir_down")
        os.system(signal[degree-16])
        degree -= 1
    else:
        pass
    return return_fun()


@app.route('/LED_ON')
def led_on():
    rpi_control.LED_turn_on()
    return return_fun()


@app.route('/LED_OFF')
def led_off():
    rpi_control.LED_turn_off()
    return return_fun()


if __name__ == '__main__':
    os.system('sudo /etc/init.d/lircd restart')
    app.run(host='0.0.0.0', port=80)
