from flask import Flask
from models import db
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


def configure_app():
    app.config['MONGODB_SETTINGS'] = {'DB': 'testing'}
    app.config['TESTING'] =True
    app.config['SECRET_KEY'] = 'flask+mongoengine=<3'
    # db.init_app(app)


def configured_app():
    configure_app()
    return app


@manager.command
def server():
    app = configured_app()
    config = dict(
        debug=True,
        host='',
        port=8888,
    )
    app.run(**config)


if __name__ == '__main__':
    configure_app()
    manager.run()
