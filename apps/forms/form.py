from wtforms import Form
from wtforms import StringField, validators, PasswordField

from apps.models.model import MerchantUser


class RegisterUserForm(Form):
    username = StringField(label="用户名",
                           validators=[validators.DataRequired(message="请填写用户名"),
                                       validators.Length(max=32, message="用户名过长"),
                                       validators.Length(min=3, message="用户名少于3个字符"),
                                       ],
                           )

    password = PasswordField(label="输入密码",
                             validators=[validators.DataRequired(message="请输入密码"),
                                         validators.Length(max=16, message="密码过长"),
                                         ],
                             )


class UserForm(RegisterUserForm):
    password1 = PasswordField(label="确认密码",
                              validators=[validators.EqualTo('password', message='输入2次一样密码')],
                              )

    # 校验用户名是否唯一
    def validate_username(self, value):
        u = MerchantUser.query.filter(MerchantUser.username == value.data).first()
        if u:
            raise validators.ValidationError(message="该用户名已经被注册了")
