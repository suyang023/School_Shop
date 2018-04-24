from flask_wtf import FlaskForm,Form
from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired
from wtforms import validators,widgets,ValidationError
from app.models import Admin

class LoginFrom(FlaskForm):
    """管理员登录表单"""
    account = StringField(
        label='用户名',
        validators=[
            validators.DataRequired("请输入用户名！."),
            validators.DataRequired(message='用户名不能为空.'),
            # validators.Length(min=6, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control',"placeholder": "请输入用户名！"}
    )

    pwd = PasswordField(
        label='密码',
        validators=[
            validators.DataRequired("请输入密码！."),
            validators.DataRequired(message='密码不能为空.'),
            # validators.Length(min=8, message='用户名长度必须大于%(min)d'),
            # validators.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
            #                   message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control',"placeholder": "请输入密码！"}
    )
    submit = SubmitField(
        label='登录',
        render_kw={
            "class":"logC"
        }
    )

    def validate_account(self,field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("帐号不存在！")

# from flask import Flask, render_template
# from flask_wtf import FlaskForm, Form
# from wtforms import StringField, SubmitField, FieldList, FormField
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'apple pie'
#
#
# class BookForm(FlaskForm):
#     book = StringField('book title')
#
#
# class LibraryForm(FlaskForm):
#     library = StringField('Library name')
#     books = FieldList(FormField(BookForm))
#     submit = SubmitField('Submit')
#
#
# @app.route('/book', methods=['GET', 'POST'])
# def book():
#     form = LibraryForm()
#     if form.validate_on_submit():
#         return 'aww yeah'
#     for i in range(6):
#         form.books.append_entry()
#
#     return render_template('books.html', form = form)



