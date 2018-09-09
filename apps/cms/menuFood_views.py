from flask import request, url_for
from apps.cms import user_bp
from flask import render_template, redirect
from flask_login import login_required, current_user

from apps.forms.menuFood_forms import CateFoodForm
from apps.libs.tools import generate_merchant_uuid, form_add_model, is_delete_food, is_delete_food_category, \
    is_delete_food_category_form_l
from apps.models import db
from apps.models.food_model import MenuFood


# 添加菜品
@user_bp.route('/add_food/<pub_id>/', endpoint='add_food', methods=('GET', 'POST'))
@login_required
def add_food(pub_id):
    pubid = is_delete_food_category(pub_id)
    if pubid:
        form = CateFoodForm(request.form, pubid)
        if request.method == 'POST' and form.validate():
            food_model = MenuFood()
            food_model.set_attr(form.data)
            food_model.goods_id = generate_merchant_uuid()
            food_model.shop_id = current_user.id
            db.session.add(food_model)
            db.session.commit()
            return redirect(url_for('user_bp.profile'))
        return render_template('merchant_shop.html', form=form, titlt='菜品添加')
    else:
        return redirect(url_for('user_bp.menu_category', pub_id=pub_id))


# 查看菜品
@user_bp.route('/look_food/<pub_id>/', endpoint='look_food', methods=('GET', 'POST'))
@login_required
def look_food(pub_id):
    stores = is_delete_food_category_form_l(pub_id)
    return render_template('look_food.html', stores=stores, pub_id=pub_id)


# 更新菜品
@user_bp.route('/update_food/<goods_id>/<pub_id>/', endpoint='update_food', methods=('GET', 'POST'))
@login_required
def update_food(goods_id, pub_id):
    # 过滤菜品
    pubid = is_delete_food_category(pub_id)
    model = MenuFood.query.filter(MenuFood.goods_id == goods_id).first()
    goodsimg = {'goods_img':model.goods_img}
    print(goodsimg)
    form = CateFoodForm(request.form, pubid)
    if request.method == 'GET':
        form = CateFoodForm(data=dict(dict(model),**goodsimg), pub_id=pubid)
    if request.method == 'POST' and form_add_model(form, model):
        return redirect(url_for('user_bp.look_food', pub_id=pub_id))
    return render_template('merchant_shop.html', form=form, titlt='菜品更新')


# 删除菜品
@user_bp.route('/delete_food/<goods_id>/', endpoint='delete_food', methods=('GET', 'POST'))
@login_required
def delete_food(goods_id):
    model = MenuFood.query.filter(MenuFood.goods_id == goods_id)
    model.update({'is_delete': True})
    db.session.commit()
    return redirect(url_for('user_bp.look_food'))
