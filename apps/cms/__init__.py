from flask import Blueprint

user_bp = Blueprint('user_bp', __name__, url_prefix='/user')

from . import views
from apps.cms import shop_views
from apps.cms import food_views
from apps.cms import menuFood_views