from . import home
from flask import current_app as app, redirect, url_for, request, flash, session, render_template
from app.home.forms import LoginFrom, RegistForm
from app.models import User
from app import db


@home.route('/')
def index():
    return render_template('home/index.html', name=app.name)

@home.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        data = form.data

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

        user = User(

            name=data["name"],
            pwd=data["pwd"],
            lei=lei
        )
        db.session.add(user)
        db.session.commit()
        flash("注册成功！", "ok")
        return render_template('home/index.html', username=username, lei=lei)
    return render_template('home/注册.html', form=form)


@home.route('/forgetpwd')
def forgetpwd():
    return render_template('home/找回密码.html')


@home.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home.login'))

