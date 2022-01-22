import random

from datetime import datetime
from datetime import timedelta, timezone
from flask import render_template, jsonify, Blueprint
from src import mongo

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

    data = mongo.db.telemetry.find(
        {"timestamp": {"$gt": datetime.utcnow() - timedelta(seconds=2)}}
    )

    raw_data = list(data)

    data = {
        "x": str(raw_data[0]["timestamp"].replace(tzinfo=timezone.utc).isoformat()),
        "y": [raw_data[0]["value"]],
    }

    return jsonify(data)
