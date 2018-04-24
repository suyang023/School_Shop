from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# 数据库的地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:a123456@localhost:3306/test2?charset=utf8'

# 跟踪数据库动态的修改，不开启容易消耗大量内存
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '7a76e8d3d3214053b0ff1fbf972ee1e9'

app.debug = True

db = SQLAlchemy(app)

# app = Flask(__name__,static_url_path='',
#             static_folder='static',
#             template_folder='templates')
# app = Flask(__name__)

from app.home import home as home_blueprint
from app.admin import adminmax as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint,url_prefix = '/admin')


# @app.error_handlers('/404')
# def page_not_found(error):
#     return '<h1>404!</h1>'
#     # return render_template("")