from datetime import datetime

from pymongo.collection import Collection

from flask import abort, Blueprint, flash, redirect, render_template

from .forms import DeviceForm

from src.models import Device
from src import pymongo

devices = Blueprint("devices", __name__)
devices_collection: Collection = pymongo.db.devices


@devices.route("/devices/", methods=["GET"])
def list_devices():

    all_devices = devices_collection.find().sort("name")

    return render_template("devices.html", devices=all_devices)


@devices.route("/devices/new", methods=["GET", "POST"])
def new_device():
    form = DeviceForm()

    if form.validate_on_submit():

        raw_device = {
            "name": form.name.data, 
            "make": form.make.data,
            "model": form.model.data
        }
        raw_device["date_added"] = datetime.utcnow()
        raw_device["date_updated"] = raw_device["date_added"]
        raw_device["slug"] = f"{raw_device['name']}-{raw_device['make']}-{raw_device['model']}".lower()
        device = Device(**raw_device)
        devices_collection.insert_one(device.to_bson())
        flash("Your device has been created!", "success")
        return redirect(f"/devices/{device.slug}")

    return render_template(
        "create_device.html", form=form
    )


@devices.route("/devices/<string:slug>", methods=["GET"])
def get_device(slug):
    recipe = devices_collection.find_one_or_404({"slug": slug})
    return Device(**recipe).to_json()


@devices.route("/devices/<string:slug>", methods=["DELETE"])
def delete_device(slug):
    deleted_device = devices_collection.find_one_and_delete(
        {"slug": slug},
    )
    if deleted_device:
        return Device(**deleted_device).to_json()
    else:
        abort(404, "device not found")
