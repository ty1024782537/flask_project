from flask import request, url_for
from apps.cms import user_bp
from flask import render_template, redirect
from flask_login import login_required, current_user

from apps.forms.food_forms import CateForm
from apps.libs.tools import generate_merchant_uuid, form_add_model, is_delete_food_category
from apps.models import db
from apps.models.food_model import MenuCategory


# 添加菜品分类
@user_bp.route('/menu_category/<pub_id>/', endpoint='menu_category', methods=('GET', 'POST'))
@login_required
def menu_category(pub_id):
    form = CateForm(request.form)
    # print(form)
    if request.method == 'POST' and form.validate():
        shop = MenuCategory()
        shop.set_attr(form.data)
        shop.pub_id = generate_merchant_uuid()
        shop.shop_id = pub_id
        db.session.add(shop)
        db.session.commit()
        return redirect(url_for('user_bp.profile'))
    return render_template('merchant_shop.html', form=form, titlt='菜品分类')


# 查看菜品分类
@user_bp.route('/look_category/<pub_id>/', endpoint='look_category', methods=('GET', 'POST'))
@login_required
def look_menu_category(pub_id):
    stores = is_delete_food_category(pub_id)
    return render_template('look_menu_category.html', stores=stores)


# 更新菜品分类
@user_bp.route('/update_category/<pub_id>/', endpoint='update_category', methods=('GET', 'POST'))
@login_required
def update_category(pub_id):
    menu_category = MenuCategory.query.filter(MenuCategory.pub_id == pub_id).first()
    if not menu_category:
        return redirect(url_for('user_bp.user'))
    form = CateForm(request.form)
    if request.method == 'GET':
        form = CateForm(data=dict(menu_category))
    elif request.method == 'POST' and form_add_model(form, menu_category):
        return redirect(url_for('user_bp.look_category'))
    return render_template('merchant_shop.html', form=form, titlt='菜品分类更新')


# 删除菜品分类
@user_bp.route('/delete_category/<type_accumulation>/', endpoint='delete_category', methods=('GET', 'POST'))
@login_required
def delete_category(type_accumulation):
    model = MenuCategory.query.filter(MenuCategory.type_accumulation == type_accumulation)
    model.update({'is_delete': True})
    db.session.commit()
    return redirect(url_for('user_bp.look_category'))
