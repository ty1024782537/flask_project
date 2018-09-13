from functools import wraps

from flask import request, jsonify, current_app, g
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from apps.models.api_user_model import BuyerUser


def token_require(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return jsonify({'status': 'false', 'message': 'token不存在!'})
        try:
            s = Serializer(secret_key=current_app.config['SECRET_KEY'])
            data = s.loads(token)
        except BadSignature:
            return jsonify({'status': 'false', 'message': 'token已失效!!'})
        except SignatureExpired:
            return jsonify({'status': 'false', 'message': 'token过期!!'})
        current_user = BuyerUser.query.get(data['user_id'])
        # print(current_user)
        if not current_user:
            return jsonify({'status': 'false', 'message': '用户不合法!!!'})
        g.current_user = current_user
        return f(*args, **kwargs)

    return decorated
