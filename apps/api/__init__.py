from flask import Blueprint

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

from apps.api import api_shop_view, api_user_view, api_cart_view, api_order_view
