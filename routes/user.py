from models.user import User
from routes import *

main = Blueprint('user', __name__)

Model = User

def current_user():
    uid = session.get('user_id')
    if uid is not None:
        u = User.objects