from flask import request, url_for, flash, abort, jsonify
from qiniu import Auth

from apps.cms import user_bp
from flask import render_template, redirect
from flask_login import login_required, current_user

from apps.forms.shop_forms import MerchantShopForm
from apps.libs.tools import generate_merchant_uuid, form_add_model
from apps.models import db
from apps.models.model import MerchantUser
from apps.models.shop_model import MerchantShop


def check_shop_pid(shop_pid):
    # 当前用户下是否有这个店铺
    shop = MerchantShop.query.filter(MerchantShop.seller == current_user, MerchantShop.pub_id == shop_pid).first()
    if not shop:
        return abort(redirect(url_for('cms.index')))
    return shop


@user_bp.route('/get_uptoken/')
def get_token():
    q = Auth(access_key="aocX5v6o2-3looKLWzbTWxTRfcVLfDqeJVSkWH6k",
             secret_key="hLeCcp-5TfPRjNKcAS-mboBjjRPDKAT0U-vDsmab")

    token = q.upload_token(bucket='flask-elm')

    return jsonify({"uptoken": token})


# 添加店铺
@user_bp.route('/merchant_shop/', endpoint='merchant_shop', methods=('GET', 'POST'))
@login_required
def merchant_shop():
    form = MerchantShopForm(request.form)
    if request.method == 'POST' and form.validate():
        shop = MerchantShop()
        shop.set_attr(form.data)
        shop.pub_id = generate_merchant_uuid()
        shop.merchant = current_user
        db.session.add(shop)
        db.session.commit()
        return redirect(url_for('user_bp.user'))
    return render_template('merchant_shop.html', form=form, titlt='添加')


# 查看个人中心
@user_bp.route('/profile/', endpoint='profile', methods=('GET',))
@login_required
def profile():
    stores = current_user.shop
    return render_template('profile.html', stores=stores)


# 更新商店
@user_bp.route('/updates_shop/<food_uid>/', endpoint='updates_shop', methods=('GET', 'POST'))
@login_required
def updates_shop(food_uid):
    shop_model = db.session.query(MerchantShop).filter(MerchantShop.merchant == current_user,
                                                       MerchantShop.pub_id == food_uid).first()
    if not shop_model:
        return redirect(url_for('user_bp.user'))
    form = MerchantShopForm(request.form)
    if request.method == 'GET':
        form = MerchantShopForm(data=dict(shop_model))
    elif request.method == 'POST' and form_add_model(form, shop_model):
        return redirect(url_for('user_bp.profile'))
    return render_template('update_shop.html', form=form, titlt='更新')
