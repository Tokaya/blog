from . import db
from . import timestamp
from flask_login import UserMixin


class User(db.Document, UserMixin):
    id = db.IntField()
    email = db.StringField(required=True)
    username = db.StringField(max_length=50)
    password = db.StringField(max_length=250)
    created_time = db.DateTimeField()

    def __init__(self, form):
        super(User, self).__init__()
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.created_time = timestamp()

    def valid_login(self, u):
        return u.username == self.username and u.password == self.password

    def valid(self):
        print('abc', User.objects())
        valid_username = User.objects(username=self.username)
        valid_username_len = len(self.username) >= 3
        valid_password_len = len(self.password) >= 3
        # valid_captcha = self.captcha == '3'
        msgs = []
        # if not valid_username:
        #     message = '用户名已经存在'
        #     msgs.append(message)
        # elif not valid_username_len:
        #     message = '用户名长度必须大于等于 3'
        #     msgs.append(message)
        # elif not valid_password_len:
        #     message = '密码长度必须大于等于 3'
        #     msgs.append(message)
        # elif not valid_captcha:
        #     message = '验证码必须输入 3'
        #     msgs.append(message)
        status = valid_username and valid_username_len and valid_password_len
        return status, msgs