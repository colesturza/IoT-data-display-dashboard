from flask import Flask
from src.config import Config
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config["MONGO_URI"] = "mongodb://dev:dev@localhost:27017/dev?authSource=admin"

    mongo.init_app(app)

    from .main.routes import main
    from .errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
