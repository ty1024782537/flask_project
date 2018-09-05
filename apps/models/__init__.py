from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

    def set_attr(self, attr):
        for k, v in attr.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)


from . import model
from . import shop_model
from . import food_model


