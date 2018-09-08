from flask import Flask
from get_data import web_data as data
from rpi_control import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index')
def index():
    pass


@app.route('/LED_ON')
def led_on():
    LED_turn_on()


@app.route('/LED_OFF')
def led_off():
    LED_turn_off()


@app.route('/LED_SHINE')
def led_shine():
    LED_shine()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000,  debug=True)
