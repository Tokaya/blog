from . import db
from . import timestamp
from flask_login import UserMixin


class User(db.document, UserMixin):
    email = db.StringField(required=True)
    username = db.StringField(max_length=50)
    password = db.StringField(max_length=250)
    created_time = db.DateTimeField()

    def __init__(self, form):
        super(User, self).__init__()
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.created_time = timestamp()