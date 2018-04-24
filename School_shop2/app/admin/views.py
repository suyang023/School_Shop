from . import adminmax
from flask import render_template, redirect, url_for, request, flash, session
from app.admin.forms import LoginFrom
from functools import wraps
from app.models import Admin


# @adminmax.route('/',methods=['GET','POST'])
# def login():
#     form = LoginFrom
#
#     if request.method == 'POST':
#         # 2.获取请求的参数
#         username = request.form.get('username')
#         password = request.form.get('password')
#         print(username, password)
#         # flash(u'%s'%password)
#         return render_template('admin/admin.html')
#     else:
#         return render_template('admin/login.html')

def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # form = LoginFrom()

        #if 'admins' 是数据库表名
        if "admin" not in session:
            print("登录保护！")
            # return render_template('admin/login.html',form = form)
            return redirect(url_for("adminmax.login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@adminmax.route('/', methods=['GET', 'POST'])
@admin_login_req
def index():
    return render_template("admin/admin.html")


@adminmax.route('/login', methods=['GET', 'POST'])
# @admin_login_req
def login():
    form = LoginFrom()
    # if request.method == 'POST':
    #     # 2.获取请求的参数
    #     us = 'admin'
    #     pa = 'admin'
    #     username = request.form.get('account')
    #     password = request.form.get('pwd')
    #     print(username, password)
    #     flash(u'%s' % password)
    #     if username == us and password == pa:
    #         return render_template('admin/admin.html')
    #     else:
    #         return render_template('admin/login.html', form=form)

    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data["account"]).first()
        if not admin.check_pwd(data["pwd"]):
            # print(data['pwd'])
            flash("密码错误！")
            return redirect(url_for("adminmax.login"))
        else:
            session['admin'] = data['account']
            # return url_for('adminmax.index')
            return render_template('admin/admin.html')

    return render_template('admin/login.html', form=form)


@adminmax.route('/logout')
@admin_login_req
def logout():
    session.pop('admin', None)
    return redirect(url_for('adminmax.login'))


@adminmax.route('/max')
@admin_login_req
def admin():
    return render_template('admin/admin.html')


@adminmax.route('/tab')
@admin_login_req
def tab():
    return render_template('admin/tab.html')


@adminmax.route('/head')
@admin_login_req
def head():
    return render_template('admin/head.html')


@adminmax.route('/head2')
@admin_login_req
def head2():
    return render_template('admin/head2.html')


@adminmax.route('/left')
@admin_login_req
def left():
    return render_template('admin/left.html')


@adminmax.route('/main')
@admin_login_req
def main():
    return render_template('admin/main.html')


@adminmax.route('/p1')
def p1():
    return render_template('admin/p1.html')


@adminmax.route('/p2')
def p2():
    return render_template('admin/p2.html')


@adminmax.route('/p3')
@admin_login_req
def p3():
    return render_template('admin/p3.html')


@adminmax.route('/changepwd')
def changepwd():
    return render_template('admin/changepwd.html')
