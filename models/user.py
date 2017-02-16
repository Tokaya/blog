from .import *



class User(db.Document, UserMixin):
    id = db.IntField()
    email = db.StringField(required=True)
    username = db.StringField(max_length=50)
    password = db.StringField(max_length=250)
    created_time = db.DateTimeField()

class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    username = StringField('Username', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                     'Usernames must have only letters, '
                                                                                     'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    # def validate_email(self, field):
    #     if User.objects.filter_by(email=field.data).first():
    #         raise ValidationError('Email already registered.')
    #
    # def validate_username(self, field):
    #     if User.objects.filter_by(username=field.data).first():
    #         raise ValidationError('Username already in use.')