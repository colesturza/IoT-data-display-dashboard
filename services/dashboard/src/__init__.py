from flask import Flask, jsonify
from src.config import Config
from flask_pymongo import PyMongo

pymongo = PyMongo()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    pymongo.init_app(app)

    from .main.routes import main
    from .errors.handlers import errors
    from .devices.routes import devices

    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(devices)

    return app
