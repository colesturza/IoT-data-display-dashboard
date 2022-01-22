import random

from datetime import datetime
from flask import render_template, jsonify, Blueprint
from src import pymongo

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/about/")
def about():
    return render_template("about.html")


@main.route("/contact/")
def contact():
    return render_template("contact.html")


@main.route("/api/data")
def get_data():

    data = {
        "x": int(round(datetime.now().timestamp() * 1000)),
        "y": [
            (1.0 if random.random() > 0.5 else -1.0) * round(random.random() * 100)
            for _ in range(2)
        ],
    }

    return jsonify(data)
