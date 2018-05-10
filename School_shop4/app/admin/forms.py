from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators,widgets,ValidationError
from app.models import Admin
class LoginFrom(FlaskForm):
    """管理员登录表单"""
    account = StringField(
        label='用户名',
        validators=[
            validators.DataRequired("请输入用户名！."),
            validators.DataRequired(message='用户名不能为空.'),

        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control',"placeholder": "请输入用户名！"}
    )

    pwd = PasswordField(
        label='密码',
        validators=[
            validators.DataRequired("请输入密码！."),
            validators.DataRequired(message='密码不能为空.'),

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
    #帐号查询语句
    def validate_account(self,field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("帐号不存在！")



