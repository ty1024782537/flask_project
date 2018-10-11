from wtforms import Form, StringField, validators, PasswordField
# from flask_wtf import Form
from apps.libs.help import api_redis
from apps.models.api_user_model import BuyerUser


class BuyerUserForm(Form):
    username = StringField(validators=[validators.DataRequired(message="请填写用户名"),
                                       validators.Length(max=32, message="用户名过长"),
                                       validators.Length(min=3, message="用户名少于3个字符"),
                                       ])

    tel = StringField(validators=[validators.DataRequired(message="请输入手机号码"),
                                  validators.Regexp("1[34578][0-9]{9}", message="手机号码格式不正确"),
                                  validators.Length(max=11, message="手机号码不能超过11位"),
                                  ])

    password = PasswordField(label="输入密码",
                             validators=[validators.DataRequired(message="请输入密码"),
                                         validators.Length(max=16, message="密码过长"),
                                         ],
                             )
    sms = StringField(validators=[validators.DataRequired(message="请输入验证码")])

    # 校验用户名是否唯一
    def validate_username(self, value):
        u = BuyerUser.query.filter(BuyerUser.username == value.data).first()
        if u:
            raise validators.ValidationError(message="该用户名已经被注册了")

    # 校验手机号是否唯一
    def validate_tel(self, value):
        u = BuyerUser.query.filter(BuyerUser.tel == value.data).first()
        if u:
            raise validators.ValidationError(message="该手机号已经被存在了")

    # 验证验证码是否正确
    def validate_sms(self, value):
        sms_no = api_redis.get(self.tel.data).decode(encoding='utf-8', errors='strict')
        if not sms_no:
            raise validators.ValidationError(message="没有验证码,请点击获取验证码!")
        if sms_no != value.data:
            raise validators.ValidationError(message="验证码不正确!")
