from flask import Flask
from flask_script import Manager
from routes.user import main as routes_user
from models import db

app = Flask(__name__)
manager = Manager(app)


def register_routes(app):
    app.register_blueprint(routes_user)


def configure_app():
    app.config['MONGODB_SETTINGS'] = {'db': 'blog'}
    app.config["SECRET_KEY"] = "secret_key"
    db.init_app(app)
    register_routes(app)


def configured_app():
    configure_app()
    return app


@manager.command
def server():
    print('server run')
    config = dict(
        debug=True,
        host='',
        port=8888,
    )
    app.run(**config)


if __name__ == '__main__':
    configured_app()
    manager.run()
