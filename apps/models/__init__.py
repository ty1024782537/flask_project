from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    is_delete = db.Column(db.Boolean, default=False)

    def set_attr(self, attr):
        for k, v in attr.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)

    # def __getitem__(self, item):
    #     if hasattr(self, item):
    #         return getattr(self, item)

    def __getitem__(self, item):
        if hasattr(self, str(item)):
            return getattr(self, item)


from . import model
from . import shop_model
from . import food_model
