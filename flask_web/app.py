# -*- coding: utf-8 -*-

import sqlite3
from flask import Flask, request, session, g, redirect, url_for,\
    abort, render_template, flash
from get_data import web_data
import os
import rpi_control
import threading
from time import sleep
import time


app = Flask(__name__)

state = 0  # 记录空调状态
conn = sqlite3.connect('data.db')


def connect_db():
    return sqlite3.connect(app.config['data.db'])


def init_db():
    db = connect_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.after_request
def after_request(response):
    g.db.close()
    return response


# 更新form_db_data
def update_form_db_data():
    while True:
        temp = web_data.get_temperature()
        wet = web_data.get_wet()
        timestamp = web_data.get_time()
        if timestamp % 3600 == 0:
            c_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
            sql = '''INSERT INTO from_data(temperature, wet, Ctime) values(?, ?, ?)'''
            pare = (temp, wet, c_time)
            g.db.execute(sql, pare)
            print("temp:", temp)
            print("wet:", wet)
            print("ctime:", c_time)
            g.db.commit()


# 更新web_db数据库
def update_web_db_data():
    while True:
        temp = web_data.get_temperature()
        wet = web_data.get_wet()
        timestamp = web_data.get_time()
        c_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
        sql = '''INSERT INTO web_data(temperature, wet, Ctime) values(?, ?, ?)'''
        pare = (temp, wet, c_time)
        g.db.execute(sql, pare)
        print("temp:", temp)
        print("wet:", wet)
        print("ctime:", c_time)
        g.db.commit()
        sleep(5)


def Judge_on_off():
    global state
    global temp
    global wet
    global Pi_time
    if state > 0:
        return render_template('index.html', methods=['POST'], Temperature=temp[-1], Wet=wet[-1], Time=Pi_time[-1], Turn="turn off", State=state)
    else:
        return render_template('index.html', methods=['POST'], Temperature=temp[-1], Wet=wet[-1], Time=Pi_time[-1], Turn="turn on", State=state)


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
    rpi_control.IR_turn_up(state)
    state += 1
    return Judge_on_off()


@app.route('/IR_DOWN')
def ir_down():
    global state
    rpi_control.IR_turn_down(state)
    state -= 1
    return Judge_on_off()


@app.route('/LE_ON')
def led_on():
    rpi_control.LED_turn_on()
    return Judge_on_off()


@app.route('/LED_OFF')
def led_off():
    rpi_control.LED_turn_off()
    return Judge_on_off()


def run_app():
    app.run(host='0.0.0.0', port=80, threaded=True)


if __name__ == '__main__':
    os.system('sudo /etc/init.d/lircd restart')
    init_db()
    threads = []
    threads.append(threading.Thread(target=update_web_db_data))
    threads.append(threading.Thread(target=update_form_db_data))
    threads.append(threading.Thread(target=run_app))
    for t in threads:
        t.start()
