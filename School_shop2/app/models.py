import datetime
from app import db


# from flask import Flask,render_template
# from flask_sqlalchemy import SQLAlchemy
#
#
# app = Flask(__name__)
#
# # 数据库的地址
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:a123456@localhost/test2?charset=utf8'
#
# # 跟踪数据库动态的修改，不开启容易消耗大量内存
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
# app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = '7a76e8d3d3214053b0ff1fbf972ee1e9'
#
# db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, unique=True)
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    pwd = db.Column(db.String(16))
    lei = db.Column(db.Integer)

    # shop = db.Column(db.Integer, db.ForeignKey('shops.id'))
    # addtime = db.Column(db.DateTime, index=True, default=datetime)

    # db.ForeignKey('roles.id')表示外键

    def __repr__(self):
        return '<User %r>' % self.name

    def check_pwd(self, pwd):
        # from werkzeug.security import check_password_hash
        # return check_password_hash(self.pwd, pwd)
        # print(self.pwd, pwd)
        if self.pwd == pwd:
            return 1;
        return 0


# 数据库模型，需要继承db.Model
class shop(db.Model):
    # 定义表名
    __tablename__ = 'shops'
    # 定义字段
    # db.Column(db.Inter)
    id = db.Column(db.Integer, primary_key=True)

    leibie_id = db.Column(db.Integer, db.ForeignKey('leibies.id'))
    # leibie = db.relationship('leibie', backref='shops')

    shop_name = db.Column(db.String(16), unique=True)
    money_m = db.Column(db.Float(16))
    money_c = db.Column(db.Float(16))

    def __repr__(self):
        return '<shop %r>' % self.name


class leibie(db.Model):
    # 定义表名
    __tablename__ = 'leibies'
    # 定义字段
    # db.Column(db.Inter)
    id = db.Column(db.Integer, primary_key=True)
    leibie_name = db.Column(db.String(32), unique=True)
    shop = db.relationship('shop', backref='leibies')

    # leibie_id = db.Column(db.Integer, db.ForeignKey('shops'))
    def __repr__(self):
        return '<Clothe %r>' % self.name


class Admin(db.Model):
    # 定义表名
    __tablename__ = 'admins'
    # 定义字段
    # db.Column(db.Inter)
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(16), unique=True)
    pwd = db.Column(db.String(16))

    def __repr__(self):
        return '<admin %r>' % self.name

    def check_pwd(self, pwd):
        # 哈兮密码验证
        # from werkzeug.security import check_password_hash
        # print(self.pwd, pwd)
        # return check_password_hash(self.pwd,pwd)
        # 普通密码验证
        print(self.pwd, pwd)
        if self.pwd == pwd:
            return 1;
        return 0


if __name__ == '__main__':  # 直接执行models.py文件来生成数据库表
    # db.drop_all()
    db.create_all()
