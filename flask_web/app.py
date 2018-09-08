from flask import Flask, render_template
from get_data import web_data as data
import os
from rpi_control import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/IR_ON')
def ir_on():
    print('ir_on')
    os.system('irsend SEND_ONCE AIR KEY_OPEN')
    return render_template('index.html')


@app.route('/IR_OFF')
def ir_off():
    print('ir_off')
    IR_turn_off()
    os.system('irsend SEND_ONCE AIR KEY_OFF')
    return render_template('index.html')


@app.route('/IR_UP')
def ir_up():
    print('ir_up')
    os.system('irsend SEND_ONCE AIR KEY_UP')
    return render_template('index.html')


@app.route('/IR_DOWN')
def ir_DOWN():
    print('ir_down')
    os.system('irsend SEND_ONCE AIR KEY_DOWN')
    return render_template('index.html')


@app.route('/LE_ON')
def led_on():
    LED_turn_on()
    return render_template('index.html')


@app.route('/LED_OFF')
def led_off():
    LED_turn_off()
    return render_template('index.html')


@app.route('/LED_SHINE')
def led_shine():
    LED_shine()
    return render_template('index.html')


if __name__ == '__main__':
    os.system('sudo /etc/init.d/lircd restart')
    app.run(host='0.0.0.0', port=80,  debug=True)
