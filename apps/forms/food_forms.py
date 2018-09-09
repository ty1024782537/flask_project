from wtforms import Form, StringField, BooleanField, validators, HiddenField


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

