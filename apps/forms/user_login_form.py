from wtforms import Form, StringField, validators, PasswordField

from apps.models.api_user_model import BuyerUser


class UserLogin(Form):
    name = StringField(validators=[validators.DataRequired(message="请填写用户名"),
                                   validators.Length(max=32, message="用户名过长"),
                                   validators.Length(min=3, message="用户名少于3个字符"),
                                   ])

    password = PasswordField(label="输入密码",
                             validators=[validators.DataRequired(message="请输入密码"),
                                         validators.Length(max=16, message="密码过长")
                                         ])

    # 校验用户名和密码
    def validate_name(self, value):
        u = BuyerUser.query.filter(BuyerUser.username == value.data).first()
        if not u:
            raise validators.ValidationError(message="该用户名不存在!")
        else:
            if not u.check_password(self.data['password']):
                raise validators.ValidationError(message="密码错误!")
