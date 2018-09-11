# -*- coding: utf-8 -*-

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from get_data import web_data
import os
from rpi_control import *
import threading
from time import sleep

app = Flask(__name__)

state = 0  # 记录空调状态
temp = [26]
wet = [12]
Pi_time = [1]


# 更新数据库
def update_data():
    while True:
        global temp
        global wet
        global Pi_time
        temp.append(web_data.get_temperature())
        wet.append(web_data.get_wet())

        print("temp:", temp[-1])
        print("wet:", wet[-1])

        sleep(3)


def Judge_on_off():
    global state
    global temp
    global wet
    global Pi_time
    if state > 0:
        return render_template('index.html', Temperature=temp[-1], Wet=wet[-1], Time=Pi_time[-1], Turn="turn off", State=state)
    else:
        return render_template('index.html', Temperature=temp[-1], Wet=wet[-1], Time=Pi_time[-1], Turn="turn on", State=state)


@app.route('/')
def hello_world():
    return Judge_on_off()


@app.route('/IR_ON')
def ir_on():
    global state
    if state:
        print("ir_off")
        os.system('irsend SEND_ONCE AIR KEY_OFF')
        state = 0
    else:
        print('ir_on')
        os.system('irsend SEND_ONCE AIR KEY_26')
        state = 26
    return Judge_on_off()


@app.route('/IR_UP')
def ir_up():
    global state
    if state == 0 or state == 30:
        pass
    elif state == 16:
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
    state += 1
    return Judge_on_off()


@app.route('/IR_DOWN')
def ir_DOWN():
    global state
    if state == 0 or state == 16:
        pass
    elif state == 17:
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
    state -= 1
    return Judge_on_off()


@app.route('/LE_ON')
def led_on():
    LED_turn_on()
    return Judge_on_off()


@app.route('/LED_OFF')
def led_off():
    LED_turn_off()
    return Judge_on_off()


@app.route('/LED_SHINE')
def led_shine():
    LED_shine()
    return Judge_on_off()


def run_app():
    app.run(host='0.0.0.0', port=80, debug=True)


if __name__ == '__main__':
    os.system('sudo /etc/init.d/lircd restart')
    threads = []
    threads.append(threading.Thread(target=update_data))
    threads.append(threading.Thread(target=run_app))
    for t in threads:
        t.start()
