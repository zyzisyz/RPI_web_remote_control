# -*- coding: utf-8 -*-

from flask import Flask, request, session, g, redirect, url_for,\
    abort, render_template, flash


app = Flask(__name__)

@app.route('/')
def chart():
    return render_template("chart.html")


app.run(host='0.0.0.0', port=80)