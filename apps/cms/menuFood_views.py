from flask import request, url_for
from apps.cms import user_bp
from flask import render_template, redirect
from flask_login import login_required, current_user

from apps.forms.menuFood_forms import CateFoodForm
from apps.libs.tools import generate_merchant_uuid, form_add_model, is_delete_food
from apps.models import db
from apps.models.food_model import MenuFood


# 添加菜品
@user_bp.route('/add_food/', endpoint='add_food', methods=('GET', 'POST'))
@login_required
def add_food():
    form = CateFoodForm(request.form)
    if request.method == 'POST' and form.validate():
        food_model = MenuFood()
        food_model.set_attr(form.data)
        food_model.goods_id = generate_merchant_uuid()
        food_model.shop_id = current_user.id
        db.session.add(food_model)
        db.session.commit()
        return redirect(url_for('user_bp.profile'))
    return render_template('merchant_shop.html', form=form, titlt='菜品')


# 查看菜品
@user_bp.route('/look_food/', endpoint='look_food', methods=('GET', 'POST'))
@login_required
def look_food():
    stores = is_delete_food()
    return render_template('look_food.html', stores=stores)


# 更新菜品
@user_bp.route('/update_food/<goods_id>/', endpoint='update_food', methods=('GET', 'POST'))
@login_required
def update_food(goods_id):
    model = MenuFood.query.filter(MenuFood.goods_id == goods_id).first()
    form = CateFoodForm(request.form)
    if request.method == 'GET':
        form = CateFoodForm(data=dict(model))
    if request.method == 'POST' and form_add_model(form, model):
        return redirect(url_for('user_bp.look_food'))
    return render_template('merchant_shop.html', form=form, titlt='菜品更新')


# 删除菜品
@user_bp.route('/delete_food/<goods_id>/', endpoint='delete_food', methods=('GET', 'POST'))
@login_required
def delete_food(goods_id):
    model = MenuFood.query.filter(MenuFood.goods_id == goods_id)
    model.update({'is_delete': True})
    db.session.commit()
    return redirect(url_for('user_bp.look_food'))
