import os
import json
import paho.mqtt.client as mqtt

from datetime import datetime
from jsonschema import validate, ValidationError
from pymongo import MongoClient


MONGO_USERNAME = os.environ.get("MONGO_USERNAME")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")
MONGO_HOSTNAME = os.environ.get("MONGO_HOSTNAME")
MONGO_PORT = int(os.environ.get("MONGO_PORT"))
# MONGO_DATABASE = os.environ.get("MONGODB_DATABASE")
MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOSTNAME}:{MONGO_PORT}"
MQTT_BROKER_URL = "localhost"  # os.environ.get("MQTT_BROKER_URL")
MQTT_BROKER_PORT = 1883  # int(os.environ.get("MQTT_BROKER_PORT"))
# MQTT_USERNAME = os.environ.get("MQTT_USERNAME")
# MQTT_PASSWORD = os.environ.get("MQTT_PASSWORD")
MQTT_REFRESH_TIME = os.environ.get("MQTT_REFRESH_TIME")  # refresh time in seconds
MQTT_KEEPALIVE = 60
# MQTT_TLS_ENABLED = True
# MQTT_TLS_CA_CERTS = None
# MQTT_TLS_CERTFILE = None
# MQTT_TLS_KEYFILE = None
# MQTT_TLS_CERT_REQS = ssl.CERT_REQUIRED
# MQTT_TLS_VERSION = ssl.PROTOCOL_TLSv1_2
# MQTT_TLS_CIPHERS = None


schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Telemetry",
    "description": "Data collected by a device at a specified timestamp.",
    "type": "object",
    "properties": {
        "device": {"type": "string"},
        "timestamp": {"type": "integer"},
        "measurements": {
            "type": "array",
            "items": {
                "type": "object",
                "patternProperties": {
                    "^.*$": {"type": "number"},
                },
            },
        },
    },
    "required": ["device", "timestamp", "measurements"],
}

client = MongoClient(MONGO_URI)
db = client.dev
telemetry_collection = db.telemetry
device_collection = db.device


def on_connect(client, userdata, flags, rc, properties=None):
    client.subscribe("/telemetry/#")


def on_message(client, userdata, msg):
    telemetry = json.loads(str(msg.payload.decode()))
    try:
        validate(instance=telemetry, schema=schema)
        if device_collection.find_one({"name": telemetry["device"]}) is None:
            device_collection.telemetry.insert_one(
                {
                    "name": telemetry["device"],
                    "make": None,
                    "model": None,
                    "date_added": datetime.now(),
                    "date_updated": datetime.now(),
                }
            )
        telemetry_collection.telemetry.insert_one(telemetry)
    except ValidationError as e:
        print(telemetry)
        print(e)


def main():

    client = mqtt.Client()
    client.connect(MQTT_BROKER_URL, MQTT_BROKER_PORT)

    client.on_connect = on_connect
    client.on_message = on_message

    client.loop_forever()


if __name__ == "__main__":
    main()
