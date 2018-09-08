from flask import Flask, render_template
from get_data import web_data as data
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
    IR_turn_on()
    return render_template('index.html')


@app.route('/IR_OFF')
def ir_off():
    IR_turn_off()
    return render_template('index.html')


@app.route('/IR_UP')
def ir_up():
    IR_turn_up()
    return render_template('index.html')


@app.route('/IR_DOWN')
def ir_DOWN():
    IR_turn_down()
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
    app.run(host='0.0.0.0', port=80,  debug=True)
