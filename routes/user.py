from models.user import RegistrationForm, User
from routes import *

main = Blueprint('user', __name__)


def current_user():
    uid = session.get('user_id')
    if uid is not None:
        u = User.objects.first()
        return u


@main.route('/login')
def login_view():
    u = current_user()
    if u is not None:
        return redirect('/index')
    return render_template('login.html')


@main.route('/user/register', methods=['POST'])
def register():
    form = RegistrationForm()
    print(form.username)
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password.data)
        user.save()

    # 蓝图中的 url_for 需要加上蓝图的名字，这里是 user
    return redirect(url_for('.login_view', form=form))
    # return render_template()

# @main.route('/user/login', methods=['POST'])
# def login():
#     form = request.form
#     u = User(form)
#     # 检查 u 是否存在于数据库中并且 密码用户 都验证合格
#     user = User.query.filter_by(username=u.username).first()
#     if user is not None and user.valid_login(u):
#         print('登录成功')
#         session['user_id'] = user.id
#     else:
#         print('登录失败')
#     # 蓝图中的 url_for 需要加上蓝图的名字，这里是 user
#     return redirect(url_for('.login_view'))
