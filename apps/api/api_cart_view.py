from flask import jsonify, request, g, json
from apps.libs.help import api_redis
from apps.api import api_bp
from apps.libs.api_token import token_require
from apps.models.food_model import MenuFood


@api_bp.route('/cart/', methods=['POST'])
@token_require
def addcart():
    gids = request.form.getlist('goodsList[]')
    counts = request.form.getlist('goodsCount[]')
    ty = zip(gids, counts)
    key = 'cart_{}'.format(g.current_user.id)
    uu = api_redis.hgetall(key)
    if uu:
        api_redis.delete(key)
    for gid, count in ty:
        food = MenuFood.query.filter(MenuFood.goods_id == gid).first()
        info = {
            'goods_id': food.goods_id,
            'goods_name': food.goods_name,
            'goods_price': food.goods_price,
            'goods_img': food.goods_img,
            'amount': count,
        }
        api_redis.hset(key, 'g_{}'.format(gid), json.dumps(info))
    api_redis.expire(key, 24 * 60 * 60)
    return jsonify({'status': 'true', 'message': '添加成功'})


@api_bp.route('/cart/', methods=['GET'])
@token_require
def cart():
    key = 'cart_{}'.format(g.current_user.id)
    cart_order = api_redis.hgetall(key)
    total = 0
    list = []
    for k, v in cart_order.items():
        v = json.loads(v)
        list.append(v)
        total += (v['goods_price'] * int(v['amount']))
    data = {
        "goods_list": list,
        "totalCost": total
    }
    return jsonify(data)
