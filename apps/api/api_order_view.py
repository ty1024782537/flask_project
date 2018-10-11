from flask import jsonify

from apps.api import api_bp
from apps.libs.api_token import token_require


@api_bp.route('/order/', methods=['POST'])
@token_require
def orderList():
    data = {
        "status": "true",
        "message": "添加成功",
        "order_id": 1
    }
    return jsonify(data)


# 得到指定订单
@api_bp.route('/order/', methods=['GET'])
@token_require
def order():
    data = [
        {
            "id": "1",
            "order_code": "0000001",
            "order_birth_time": "2017-02-17 18:36",
            "order_status": "已完成",
            "shop_id": "1",
            "shop_name": "上沙麦当劳",
            "shop_img": "/images/shop-logo.png",
            "goods_list": [{
                "goods_id": "1",
                "goods_name": "汉堡",
                "goods_img": "/images/slider-pic2.jpeg",
                "amount": 6,
                "goods_price": 10
            }, {
                "goods_id": "1",
                "goods_name": "汉堡",
                "goods_img": "/images/slider-pic2.jpeg",
                "amount": 6,
                "goods_price": 10
            }],
            "order_price": 120,
            "order_address": "北京市朝阳区霄云路50号 距离市中心约7378米北京市朝阳区霄云路50号 距离市中心约7378米"
        },
        {
            "id": "1",
            "order_code": "0000001",
            "order_birth_time": "2017-02-17 18:36",
            "order_status": "已完成",
            "shop_id": "1",
            "shop_name": "上沙麦当劳",
            "shop_img": "/images/shop-logo.png",
            "goods_list": [{
                "goods_id": "1",
                "goods_name": "汉堡",
                "goods_img": "/images/slider-pic2.jpeg",
                "amount": 6,
                "goods_price": 10
            }, {
                "goods_id": "1",
                "goods_name": "汉堡",
                "goods_img": "/images/slider-pic2.jpeg",
                "amount": 6,
                "goods_price": 10
            }],
            "order_price": 120,
            "order_address": "北京市朝阳区霄云路50号 距离市中心约7378米北京市朝阳区霄云路50号 距离市中心约7378米"
        }
    ]
    return jsonify(data)


# 获取订单列表
@api_bp.route('/orders/', methods=['GET'])
def get_order_list():
    data = [
        {
            "id": "1",
            "order_code": "0000001",
            "order_birth_time": "2017-02-17 18:36",
            "order_status": "已完成",
            "shop_id": "1",
            "shop_name": "上沙麦当劳",
            "shop_img": "/images/shop-logo.png",
            "goods_list": [{
                "goods_id": "1",
                "goods_name": "汉堡",
                "goods_img": "/images/slider-pic2.jpeg",
                "amount": 6,
                "goods_price": 10
            }, {
                "goods_id": "1",
                "goods_name": "汉堡",
                "goods_img": "/images/slider-pic2.jpeg",
                "amount": 6,
                "goods_price": 10
            }],
            "order_price": 120,
            "order_address": "北京市朝阳区霄云路50号 距离市中心约7378米北京市朝阳区霄云路50号 距离市中心约7378米"
        },
        {
            "id": "1",
            "order_code": "0000001",
            "order_birth_time": "2017-02-17 18:36",
            "order_status": "已完成",
            "shop_id": "1",
            "shop_name": "上沙麦当劳",
            "shop_img": "/images/shop-logo.png",
            "goods_list": [{
                "goods_id": "1",
                "goods_name": "汉堡",
                "goods_img": "/images/slider-pic2.jpeg",
                "amount": 6,
                "goods_price": 10
            }, {
                "goods_id": "1",
                "goods_name": "汉堡",
                "goods_img": "/images/slider-pic2.jpeg",
                "amount": 6,
                "goods_price": 10
            }],
            "order_price": 120,
            "order_address": "北京市朝阳区霄云路50号 距离市中心约7378米北京市朝阳区霄云路50号 距离市中心约7378米"
        }
    ]
    return jsonify(data)