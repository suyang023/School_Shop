from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField

from wtforms import validators, widgets
from app.models import User


class RegistForm(FlaskForm):
    """用户注册表单"""
    name = StringField(
        label='昵称',
        validators=[
            validators.DataRequired("请输入用户名！."),
            validators.DataRequired(message='用户名不能为空.'),
            validators.Length(min=4, message='用户名长度必须大于%(min)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'loginuser', "placeholder": "请输入用户名！"}
    )
    pwd = PasswordField(
        label='密码',
        validators=[
            validators.DataRequired("请输入密码！."),
            validators.DataRequired(message='密码不能为空.'),
            validators.Length(min=6, message='用户名长度必须大于%(min)d'),
            validators.Regexp(regex="^(?=.*[a-z])(?=.*\d){6,}",
                              message='密码至少6个字符，1个大小写字母和1个数字符')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'loginuser', "placeholder": "请输入密码！"}
    )
    repwd = PasswordField(
        label='确认密码',
        validators=[
            validators.DataRequired("请输入密码！."),
            validators.DataRequired(message='密码不能为空.'),
            validators.EqualTo('pwd', message="两次密码不是一致！"),
            validators.Length(min=6, message='用户名长度必须大于%(min)d'),
            validators.Regexp(regex="^(?=.*[A-Za-z])(?=.*\d){6,}",
                              message='密码至少6个字符，1个大小写字母和1个数字符')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'loginuser', "placeholder": "请确认密码！"}
    )
    submit = SubmitField(
        label='登录',
        render_kw={
            "class": "loginbtn"
        }
    )
    select1 = BooleanField(
        label='1',
    )
    select2 = BooleanField(
        label='2',
    )
    select3 = BooleanField(
        label='3',
    )

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise validators.ValidationError("用户名已存在")


class LoginFrom(FlaskForm):
    """用户登录表单"""
    account = StringField(
        label='用户名',
        validators=[
            validators.DataRequired("请输入用户名！."),
            validators.DataRequired(message='用户名不能为空.'),
            validators.Length(min=4, message='用户名长度必须大于%(min)')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'loginusername', "placeholder": "请输入用户名！"}
    )
    pwd = PasswordField(
        label='密码',
        validators=[
            validators.DataRequired("请输入密码！."),
            validators.DataRequired(message='密码不能为空.'),

        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'loginuserpassword', "placeholder": "请输入密码！"}
    )
    submit = SubmitField(
        label='登录',
        render_kw={
            "class": "loginbtn"
        }
    )


    def validate_account(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 0:
            raise validators.ValidationError("用户名错误！")
