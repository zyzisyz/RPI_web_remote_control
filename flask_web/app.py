import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from get_data import web_data
import os
from rpi_control import *
import threading
from time import sleep

app = Flask(__name__)

num = 0
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

        sleep(1000)


@app.route('/')
def hello_world():
    global temp
    global wet
    global Pi_time
    return render_template('index.html', Temperature=temp[-1], Wet=wet[-1], Time=Pi_time[-1])


@app.route('/index')
def index():
    return render_template('index.html', Temperature=temp[-1], Wet=wet[-1], Time=Pi_time[-1])


@app.route('/IR_ON')
def ir_on():
    global num
    global temp
    global wet
    global Pi_time
    if num % 2 == 0:
        print('ir_on')
        os.system('bash irsend SEND_ONCE AIR KEY_OPEN')
        num += 1
        return render_template('index.html', Temperature=temp[-1], Wet=wet[-1], Time=Pi_time[-1])
    else:
        print("ir_off")
        os.system('bash irsend SEND_ONCE AIR KEY_OFF')
        num += 1
        return render_template('index.html', Temperature=temp[-1], Wet=wet[-1], Time=Pi_time[-1])


@app.route('/IR_UP')
def ir_up():
    global temp
    global wet
    global Pi_time
    print('ir_up')
    os.system('bash irsend SEND_ONCE AIR KEY_UP')
    return render_template('index.html', Temperature=temp[-1], Wet=wet[-1], Time=Pi_time[-1])


@app.route('/IR_DOWN')
def ir_DOWN():
    global temp
    global wet
    global Pi_time
    print('ir_down')
    os.system('bash irsend SEND_ONCE AIR KEY_DOWN')
    return render_template('index.html', Temperature=temp[-1], Wet=wet[-1], Time=Pi_time[-1])


@app.route('/LE_ON')
def led_on():
    global temp
    global wet
    global Pi_time
    LED_turn_on()
    return render_template('index.html', Temperature=temp[-1], Wet=wet[-1], Time=Pi_time[-1])


@app.route('/LED_OFF')
def led_off():
    global temp
    global wet
    global Pi_time
    LED_turn_off()
    return render_template('index.html', Temperature=temp[-1], Wet=wet[-1], Time=Pi_time[-1])


@app.route('/LED_SHINE')
def led_shine():
    global temp
    global wet
    global Pi_time
    LED_shine()
    return render_template('index.html', Temperature=temp[-1], Wet=wet[-1], Time=Pi_time[-1])


def run_app():
    app.run(host='0.0.0.0', port=80)


if __name__ == '__main__':
    os.system('bash sudo /etc/init.d/lircd restart')
    threads = []
    threads.append(threading.Thread(target=update_data))
    threads.append(threading.Thread(target=run_app))
    for t in threads:
        t.start()
