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
                               Temperature=temp, Wet=wet, State=state)
    else:
        return render_template('index.html', methods=['POST'],
                               Temperature=temp, Wet=wet, State='空调关闭')


@app.route('/')
def hello_world():
    return return_fun()


@app.route('/index/')
def index():
    return return_fun()


@app.route('/IR_ON/')
def ir_on():
    global state
    print('ir_on')
    os.system('irsend SEND_ONCE AIR KEY_26')
    state = 26
    return return_fun()


@app.route('/IR_OFF/')
def ir_off():
    global state
    print('ir_off')
    state = 0
    return return_fun()


@app.route("/IR_UP/")
def ir_up():
    global state
    if state != 0 and state < 28 and state > - 17:
        print("ir_up")
        rpi_control.IR_turn_up(state)
        state += 1
    else:
        pass
    return return_fun()


@app.route("/IR_DOWN/")
def ir_down():
    global state
    if state != 0 and state <= 28 and state > 17:
        print("ir_down")
        rpi_control.IR_turn_down(state)
        state -= 1
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
    app.run(port=8000)
