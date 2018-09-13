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


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/index/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
