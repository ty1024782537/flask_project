from apps.models import db, BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from apps import login_manager


class MerchantUser(BaseModel, UserMixin):
    username = db.Column(db.String(32), unique=True, nullable=False)
    _password = db.Column('password', db.String(128))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, val):
        self._password = generate_password_hash(val)

    def verify_password(self, password):
        return check_password_hash(self._password, password)


# 加载用户的回调函数
@login_manager.user_loader
def load_user(user_id):
    return MerchantUser.query.get(user_id)
