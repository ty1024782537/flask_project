from wtforms import Form, StringField, BooleanField, validators


class CateForm(Form):
    name = StringField(label="菜品分类名",
                       validators=[
                           validators.InputRequired(message="请输入菜品分类名"),
                           validators.Length(max=32, message="不能超过32字符"),
                       ],
                       render_kw={'class': 'form-control', 'placeholder': '请输入菜品分类名'},
                       )
    # 分类描述
    description = StringField(label="菜品分类描述",
                              validators=[
                                  validators.Length(max=128, message="不能超过128字符"),
                              ],
                              render_kw={'class': 'form-control', 'placeholder': '请输入菜品分类描述'},
                              )
    # 分类编号
    type_accumulation = StringField(label="菜品分类编号",
                                    validators=[
                                        validators.Length(max=16, message="不能超过16字符"),
                                    ],
                                    render_kw={'class': 'form-control', 'placeholder': '请输入菜品分类编号'},
                                    )
    # 是否默认
    is_default = BooleanField(label="是否默认")
    # # 进行外键选择
    # shop_id = SelectField(label="店铺信息",
    #                       validators=[validators.DataRequired(message="请选择分类")],
    #                       render_kw={'class': 'form-control'},
    #                       )
    #
    # def __init__(self, *args, **kwargs):
    #     super(CateForm, self).__init__(*args, **kwargs)
    #     self.shop_id.choices = [(x.pub_id, x.shop_name) for x in current_user.shop]
