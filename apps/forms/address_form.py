from wtforms import Form, StringField, validators, PasswordField


class Address(Form):
    name = StringField(validators=[validators.DataRequired(message="请填写收货人"),
                                   validators.Length(max=32, message="收货人过长"),
                                   ])
    tel = StringField(validators=[validators.DataRequired(message="请输入手机号码"),
                                  validators.Regexp("1[34578][0-9]{9}", message="手机号码格式不正确"),
                                  validators.Length(max=11, message="手机号码不能超过11位"),
                                  ])
    provence = StringField(validators=[validators.DataRequired(message="请填写省份")]
                           )
    city = StringField(validators=[validators.DataRequired(message="请填写城市")]
                       )
    area = StringField(validators=[validators.DataRequired(message="请填写县")]
                       )
    detail_address = StringField(validators=[validators.DataRequired(message="请填写具体地址")]
                                 )
