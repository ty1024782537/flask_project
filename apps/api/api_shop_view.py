import random
from flask import jsonify, request
from apps.api import api_bp
from apps.libs.tools import food_category_api

from apps.models.shop_model import MerchantShop


@api_bp.route('/shop_list/', methods=['GET'])
def shop_list():
    shop_list = MerchantShop.query.all()
    data = [dict(dict(shop), **{"id": shop.pub_id}, **{"distance": random.randint(100, 9999)},
                 **{'estimate_time': random.randint(10, 100)}) for shop in shop_list]
    return jsonify(data)


@api_bp.route('/shop/', methods=['GET'])
def shop():
    pub_id = request.args.get('id')
    data = food_category_api(pub_id)
    return jsonify(data)

