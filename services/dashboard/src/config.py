import os
import ssl

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MONGO_USERNAME = os.environ.get("MONGO_USERNAME")
    MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")
    MONGO_HOSTNAME = os.environ.get("MONGO_HOSTNAME")
    MONGO_PORT = int(os.environ.get("MONGO_PORT"))
    MONGO_DATABASE = os.environ.get("MONGODB_DATABASE")
    MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOSTNAME}:{MONGO_PORT}"
