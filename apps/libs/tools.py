import uuid
import datetime

# 产生16位的UUID字符串
from flask_login import current_user

from apps.models import db


def generate_merchant_uuid():
    tre = str(uuid.uuid4())
    tt = str(datetime.date.today())
    oo = ''.join(tre.split('-')[2:4])
    cc = ''.join(tt.split('-')[0:3])
    num = cc + oo
    # print(num)
    return num


# if __name__ == '__main__':
#     generate_merchant_uuid()


def form_add_model(form, model):
    if form.validate():
        for k, v in form.data.items():
            if hasattr(model, k):
                setattr(model, k, v)
        db.session.add(model)
        db.session.commit()
        return True


def is_delete_food_category():
    store = current_user.shop
    stors = store[0].categories
    stores = []
    for x in stors:
        if not x.is_delete:
            stores.append(x)
    return stores


def is_delete_food():
    store = current_user.shop
    stors = store[0].categories
    stores = []
    for x in stors:
        t = x.foods
        for e in t:
            if not e.is_delete:
                stores.append(e)
    return stores
