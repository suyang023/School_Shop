from . import home
from flask import current_app as app, redirect, url_for, request, flash, session, render_template
from app.home.forms import LoginFrom, RegistForm
from app.models import Usershop as user_shop
from app.models import User
from app.models import shop

from werkzeug.security import generate_password_hash
import uuid

from app import db

uservalue = []


def uservalues(user):
    uservalue.append(user)


@home.route('/')
def index():
    try:
        # if request.method == 'POST':
        #     shop_name = request.values.post('shop_name')
        #     print('商品名称！')
        #     print(shop_name)
        # else:
        username = uservalue[0]
        # 获取shops数据库中所有数据
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
        uservalues(username)
        shopname = shop.query.all()
        return render_template('home/index.html', username=username, lei=lei, shopname=shopname)
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

    # lei1 = lei2 = lei3 = lei4 = 0
    #
    # for v in shop:
    #     if v.lei == 1:
    #         lei1 += v.number
    #     elif v.lei == 2:
    #         lei2 += v.number
    #     elif v.lei == 3:
    #         lei3 += v.number
    #     elif v.lei == 4:
    #         lei4 += v.number
    #
    # print(lei1, lei2, lei3, lei4)
    # sum = lei1 + lei2 + lei3 + lei4
    #
    # lei = []
    # lei_value = (lei1, lei2, lei3, lei4)
    # for i in range(len(lei_value)):
    #     if max(lei_value) == lei_value[i]:
    #         lei.append(1)
    #     elif max(lei_value) == lei_value[i]:
    #         lei.append(2)
    #     elif max(lei_value) == lei_value[i]:
    #         lei.append(3)
    #     else:
    #         lei.append(4)
    #
    # username = User.query.filter_by(name=user).first()
    #
    # # del uservalue[0]
    # print(username)
    #
    # print("购买数据量为%s" % sum)
    # print("购买商品最多的是：%s" % lei[0])

    return render_template('home/用户中心.html', user=user, shop=shop)


# @home.route('/addshop/<name>')
# def addshop(name):
#     session.pop('user', None)
#     # shop_name = request.form.post('shop_name')
#     user = uservalue[0]
#     username = User.query.filter_by(name=user).first()
#     #静态数据库加1
#     # lei = username.lei
#     # lei2 = lei + 1
#     # username.lei = lei2
#     #动态修改数据库数据
#     username.lei = name
#     db.session.commit()
#     # del uservalue[0]
#     # print(username)
#     print('此时数量为：%s' % name)
#     return redirect(url_for('home.index'))


@home.route('/addshop/<name>')
def addshop(name):
    session.pop('user', None)
    # shop_name = request.form.post('shop_name')

    user = uservalue[0]

    shop_id = shop.query.filter_by(id=name).first()
    shop_name = shop_id.shop_name
    image_url = shop_id.image_url
    lei = shop_id.leibie_id
    print('商品名称：%s' % shop_name)
    # user_name = user_shop.query.filter(user_shop.user.endswith(user=user)).all()
    # user_name = user_shop.query.filter(user=user).first()

    # number = user_name.number

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
