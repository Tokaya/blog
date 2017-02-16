from flask import Flask
from flask_mongoengine import MongoEngine
from flask_script import Manager
from routes.user import main as routes_user

app = Flask(__name__)
db = MongoEngine()
db.init_app(app)
manager = Manager(app)


def register_routes(app):
    app.register_blueprint(routes_user)


def configure_app():
    app.config['MONGODB_SETTINGS'] = {'db': 'blog'}
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'flask + mongodb =<3'
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
    configure_app()
    manager.run()
