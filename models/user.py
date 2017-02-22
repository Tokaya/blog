from . import *




class User(db.Document, UserMixin):
    name = db.StringField(unique=True, required=True)
    password = db.StringField(required=True)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def save(self):
        newUser = User(username=self.username, password=self.password)
        newUser.save()
        print("new user id = %s " % newUser.id)
        self.id = newUser.id
        return self.id
