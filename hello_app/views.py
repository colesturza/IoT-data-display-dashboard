from datetime import datetime
from flask import Flask, render_template, jsonify
import random
from . import app


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template("hello_there.html", name=name, date=datetime.now())


@app.route("/api/data")
def get_data():

    data = {
        "x": datetime.now(),
        "y": [round(random.random(), 3) for _ in range(3)]
    }

    return jsonify(data)