from datetime import timedelta
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import request, jsonify, current_app, g
import random
from apps.api import api_bp
from apps.forms.address_form import Address
from apps.forms.buyer_form import BuyerUserForm
from apps.forms.user_login_form import UserLogin
from apps.libs.api_token import token_require
from apps.libs.help import api_redis
from apps.models import db
from apps.models.api_user_model import BuyerUser, BuyerAddressModel


# 买家注册
@api_bp.route('/register/', endpoint='register', methods=['POST'])
def register():
    form = BuyerUserForm(request.form)
    if form.validate():
        buyer_user = BuyerUser()
        buyer_user.set_attr(form.data)
        db.session.add(buyer_user)
        db.session.commit()
        return jsonify({'status': 'true', 'message': '注册成功'})
    else:
        return jsonify({'status': 'false', 'message': '注册失败'})


# 验证码
@api_bp.route('/sms/', endpoint='sms', methods=['GET'])
def sms():
    tel = request.args.get('tel')
    if tel:
        code = random.randint(1000, 9999)
        print(code)
        try:
            api_redis.setex(tel, code, timedelta(seconds=2 * 60))
            return jsonify({'status': 'true', 'message': '验证码发送成功!'})
        except:
            return jsonify({'status': 'false', 'message': '验证码发送失败!'})
    else:
        return jsonify({'status': 'false', 'message': '手机号码已失效!!'})


# 买家登录
@api_bp.route('/login/', endpoint='login', methods=['POST'])
def login():
    form = UserLogin(request.form)
    if form.validate():
        s = Serializer(secret_key=current_app.config['SECRET_KEY'],
                       expires_in=current_app.config['TOKEN_EXPIRES'])
        user = BuyerUser.query.filter(BuyerUser.username == form.data['name']).first()
        data = s.dumps({'user_id': user.id})
        res = jsonify({'status': 'true', 'message': '登录成功!', 'user_id': user.id, 'username': form.data['name']})
        res.set_cookie('token', data.decode('utf-8'))
        return res
    else:
        return jsonify({'status': 'false', 'message': '登录失败!'})


# 地址
@api_bp.route('/address/', endpoint='address', methods=['GET'])
@token_require
def get_address_list():
    id = request.args.get('id')
    user_id = g.current_user.id
    if id:
        address = BuyerAddressModel.query.filter(BuyerAddressModel.user_id == user_id).all()[int(id) - 1]
        data = dict(address)
    else:
        address = BuyerAddressModel.query.filter(BuyerAddressModel.user_id == user_id).all()
        data = list()
        if address:
            data = [{**dict(i), 'id': x + 1} for x, i in enumerate(address)]
    return jsonify(data)


# 新增地址API
@api_bp.route('/address/', methods=['POST'])
@token_require
def add_address():
    address_id = request.form.get('id')
    address = Address(request.form)
    if address.validate():
        buyer_address = BuyerAddressModel()
        if address_id:
            buyer_address = BuyerAddressModel.query.filter(BuyerAddressModel.id == address_id).first()
        buyer_address.set_attr(address.data)
        buyer_address.user_id = g.current_user.id
        db.session.add(buyer_address)
        db.session.commit()
        data = {
            "status": "true",
            "message": "成功"
        }
        return jsonify(data)
    return jsonify({'status': 'false', 'message': '失败!'})
