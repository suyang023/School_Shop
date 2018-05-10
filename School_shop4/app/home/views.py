from . import home
from flask import current_app as app, redirect, url_for, request, flash, session, render_template
from app.home.forms import LoginFrom, RegistForm
from app.models import Usershop as user_shop
from app.models import User
from app.models import shop

from app import db

uservalue = []


def uservalues(user):
    uservalue.append(user)

#首页模块
@home.route('/')
def index():
    try:

        username = uservalue[0]
        shopname = shop.query.all()

        # 获取usershops数据库数据
        shop2 = user_shop.query.filter_by(user=username).all()

        lei1 = lei2 = lei3 = lei4 = 0

        for v in shop2:
            if v.lei == 1:
                lei1 += v.number
            elif v.lei == 2:
                lei2 += v.number
            elif v.lei == 3:
                lei3 += v.number
            elif v.lei == 4:
                lei4 += v.number

        lei_end = []
        lei_value = (lei1, lei2, lei3, lei4)
        a = 0
        for i in lei_value:
            a+=1
            if max(lei_value) == i:
                print(max(lei_value),i)
                lei_end.append(a)

        print(lei1, lei2, lei3, lei4)
        print('最喜欢的商品种类是：%s%s'%(lei_end[0],lei_end))
        lei = lei_end[0]
        return render_template('home/index.html', name=app.name, username=username, shopname=shopname, lei=lei)
    # 首页异常处理程序
    except BaseException:

        shopname = shop.query.all()
        return render_template('home/index.html', name=app.name, shopname=shopname)

#用户登录模块
@home.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFrom()

    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=data["account"]).first()
        #用户登录判断语句
        if not user.check_pwd(data["pwd"]):
            print(data['pwd'])
            flash("密码错误！")
            return redirect(url_for("home.login"))
        else:
            session['user'] = data['account']
            alluser = data['account']
            uservalues(alluser)
            username = data['account']
            print(username)
            leibie = User.query.filter_by(name=username).first()
            lei = leibie.lei
            print(lei)
            shopname = shop.query.all()
            return render_template('home/index.html', username=username, lei=lei, shopname=shopname)
    return render_template('home/登录.html', form=form)

#用户注册模块
@home.route('/logup', methods=['GET', 'POST'])
def logup():
    form = RegistForm()
    #标签判断语句
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

        #将用户注册信息写入数据库中
        user = User(
            name=data["name"],
            pwd=data["pwd"],
            lei=lei
        )
        db.session.add(user)
        db.session.commit()
        flash("注册成功！", "ok")
        uservalues(username)
        shopname = shop.query.all()
        return render_template('home/index.html', username=username, lei=lei, shopname=shopname)

    return render_template('home/注册.html', form=form)


@home.route('/forgetpwd')
def forgetpwd():
    return render_template('home/找回密码.html')


@home.route('/logout')
def logout():
    session.pop('user', None)
    try:
        del uservalue[0]
        print('删除用户')
        print(uservalue)
        return redirect(url_for('home.login'))
    except BaseException:
        return redirect(url_for('home.login'))


@home.route('/usercent')
def usercent():
    session.pop('user', None)
    user = uservalue[0]
    shop = user_shop.query.filter_by(user=user).all()
    return render_template('home/用户中心.html', user=user, shop=shop)



#购物后台传递参数模块
@home.route('/addshop/<name>')
def addshop(name):
    session.pop('user', None)


    user = uservalue[0]

    shop_id = shop.query.filter_by(id=name).first()
    shop_name = shop_id.shop_name
    image_url = shop_id.image_url
    lei = shop_id.leibie_id
    print('商品名称：%s' % shop_name)

    shop2 = user_shop.query.filter_by(user=user).all()

    for v in shop2:
        if shop_name == v.shop_name:
            v.number += 1
            db.session.commit()
            break;
    else:
        Usershop = user_shop(
            user=user,
            shop_name=shop_name,
            number=1,
            image_url=image_url,
            lei=lei
        )
        db.session.add(Usershop)
        db.session.commit()

    print('添加商品成功！')
    return redirect(url_for('home.index'))
