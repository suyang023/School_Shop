from . import home
from flask import current_app as app, redirect, url_for, request, flash, session, render_template
from app.home.forms import LoginFrom, RegistForm
from app.models import User
from werkzeug.security import generate_password_hash
import uuid
from app import db


@home.route('/')
def index():
    return render_template('home/index.html', name=app.name)


# @home.route('/login',methods=['GET','POST'])
# def login():
#     form = LoginFrom()
#     if request.method == 'POST':
#         # 2.获取请求的参数
#         username = request.form.get('username')
#         password = request.form.get('password')
#         print(username, password)
#         # flash(u'%s'%password)
#         return render_template('home/index.html')
#     else:
#         return render_template('home/登录.html',form = form)

@home.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    # print('进入登录页面！')
    if form.validate_on_submit():
        data = form.data
        # print('进入密码验证')
        # print(data['pwd'])
        user = User.query.filter_by(name=data["account"]).first()
        if not user.check_pwd(data["pwd"]):
            print(data['pwd'])
            flash("密码错误！")
            return redirect(url_for("home.login"))
        else:
            session['user'] = data['account']
            username = data['account']
            print(username)
            leibie = User.query.filter_by(name=username).first()
            lei = leibie.lei
            print(lei)
            return render_template('home/index.html', username=username, lei=lei)
    return render_template('home/登录.html', form=form)


@home.route('/logup', methods=['GET', 'POST'])
def logup():
    form = RegistForm()
    if form.validate_on_submit():
        data = form.data
        username = data["name"]
        if 0 != data['select1']:
            sele1 = 1
        else:
            sele1 = 0
        if 0 != data['select2']:
            sele2 = 2
        else:
            sele2 = 0
        if 0 != data['select3']:
            sele3 = 4
        else:
            sele3 = 0

        lei = sele3 + sele2 + sele1
        print(username)
        print(sele1, sele2, sele3)
        print(lei)
        # print(data['select2'])
        # print(data['select2'])
        # print(data['select2'])

        user = User(
            # id=10002,
            name=data["name"],
            # pwd=generate_password_hash(data["pwd"]),
            pwd=data["pwd"],
            lei=lei
            # user_id = 1002,
            # shop = uuid.uuid4().hex
            # shop = 11
        )
        db.session.add(user)
        db.session.commit()
        flash("注册成功！", "ok")
        return render_template('home/index.html', username=username, lei=lei)
    # if request.method == 'POST':
    #     # 2.获取请求的参数
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     fashion = request.form.get('Fruit1')
    #     life = request.form.get('Fruit2')
    #     food = request.form.get('Fruit3')
    #     print(username, password,fashion,life,food)
    #     # flash(u'%s'%password)
    #     return render_template('home/index.html')
    # else:
    return render_template('home/注册.html', form=form)


@home.route('/forgetpwd')
def forgetpwd():
    return render_template('home/找回密码.html')


@home.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home.login'))
# def home():
#     return render_template('home/admin.html',name = app.name)
