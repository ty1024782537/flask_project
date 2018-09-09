from wtforms import Form, StringField, validators, BooleanField, DecimalField
from wtforms.widgets import HiddenInput


class MerchantShopForm(Form):
    shop_name = StringField(label="店铺名称", validators=[validators.DataRequired(message="请输入店铺名称"),
                                                      validators.Length(max=32, message="店铺名称不能超过32个字符"),
                                                      ],
                            render_kw={'class': 'form-control', 'placeholder': '请输入店铺名称'},
                            )
    brand = BooleanField(label="品 牌", default=False)
    on_time = BooleanField(label="准时送达", default=False)
    fengniao = BooleanField(label="蜂鸟快递", default=False)
    bao = BooleanField(label="提供保险", default=False)
    piao = BooleanField(label="提供发票", default=False)
    zhun = BooleanField(label="准标识", default=False)

    start_send = DecimalField(label="起送价格",
                              validators=[validators.DataRequired(message="填写起送价格")],
                              render_kw={'class': 'form-control', 'placeholder': '请输入起送价格'},
                              )
    send_cost = DecimalField(label="配送费用",
                             validators=[validators.InputRequired(message="填写配送费用")],
                             render_kw={'class': 'form-control', 'placeholder': '请输入配送费用'},
                             )

    notice = StringField(label="店铺公告",
                         validators=[validators.Length(max=210, message="不能超过128个字符")],
                         render_kw={'class': 'form-control', 'placeholder': '请输入店铺公告'},
                         )
    discount = StringField(label="优惠信息", validators=[validators.Length(max=210, message="不能超过128个字符")],
                           render_kw={'class': 'form-control', 'placeholder': '请输入优惠信息'},
                           )
    shop_img = StringField(label="店铺图片", id='image-input', widget=HiddenInput(),
                           )
