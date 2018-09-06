from flask import request, url_for, flash
from apps.cms import user_bp
from flask import render_template, redirect
from flask_login import login_required, current_user

from apps.forms.shop_forms import MerchantShopForm
from apps.libs.tools import generate_merchant_uuid
from apps.models import db
from apps.models.model import MerchantUser
from apps.models.shop_model import MerchantShop


# 添加商店


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
        return redirect(user_bp('user_bp.user'))
    return render_template('merchant_shop.html', form=form)
