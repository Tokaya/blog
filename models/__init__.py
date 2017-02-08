from flask_mongoengine import MongoEngine
import time

db = MongoEngine()


def timestamp():
    return int(time.time())
