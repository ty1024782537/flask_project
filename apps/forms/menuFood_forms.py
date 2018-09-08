from wtforms import Form, StringField, validators, DecimalField, SelectField,IntegerField

from apps.libs.tools import is_delete_food_category


class CateFoodForm(Form):
    goods_name = StringField(label="菜品名称",
                               validators=[
                                   validators.InputRequired(message="请输入菜品名称"),
                                   validators.Length(max=32, message="不能超过32字符"),
                               ],
                               render_kw={'class': 'form-control', 'placeholder': '请输入菜品名称'},
                               )
    # 进行外键选择
    category_id = SelectField(label="分类信息",
                                validators=[validators.InputRequired(message="请选择分类")],
                                render_kw={'class': 'form-control'},
                                coerce=int
                              # choices=[(1,'甜点'),(2 ,'饮料')]
                          )
    # 菜品价钱
    goods_price = DecimalField(label="菜品价钱",
                             validators=[validators.DataRequired(message="填写菜品价钱")],
                             render_kw={'class': 'form-control', 'placeholder': '请输入菜品价钱'},
                             )
    # 菜品描述
    description = StringField(label="菜品描述",
                         validators=[validators.Length(max=128, message="不能超过128个字符")],
                         render_kw={'class': 'form-control', 'placeholder': '请输入菜品描述'},
                         )
    # 菜品提示信息
    tips = StringField(label="菜品提示信息",
                         validators=[validators.Length(max=128, message="不能超过128个字符")],
                         render_kw={'class': 'form-control', 'placeholder': '请输入菜品提示信息'},
                         )

    def __init__(self, *args, **kwargs):
        super(CateFoodForm, self).__init__(*args, **kwargs)
        self.category_id.choices = [(x.id, x.name) for x in is_delete_food_category()]
