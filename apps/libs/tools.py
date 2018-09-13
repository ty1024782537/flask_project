import uuid
import datetime

# 产生16位的UUID字符串
from flask_login import current_user

from apps.models import db
from apps.models.food_model import MenuCategory, MenuFood
from apps.models.shop_model import MerchantShop


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


def is_delete_food_category(pub_id):
    store = current_user.shop
    u = []
    for x in store:
        if x.categories and x.pub_id == pub_id:
            u.append(x)
    if u:
        stors = u[0].categories
        stores = []
        for x in stors:
            if not x.is_delete:
                stores.append(x)
        return stores
    return None


def is_delete_food_category_form():
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


# 过滤菜品(查看功能)
def is_delete_food_category_form_l(pub_id):
    store = current_user.shop
    u = []
    for x in store:
        if x.categories and x.pub_id == pub_id:
            u.append(x)
    if u:
        stors = u[0].categories
        stores = []
        for x in stors:
            t = x.foods
            for i in t:
                if not i.is_delete:
                    stores.append(i)
        return stores
    return None


def food(shop):
    menu_food = MenuCategory.query.filter(MenuCategory.shop_id == shop.pub_id)
    data = [dict(dict(shop), **{'goods_list': shop_food(shop)}) for shop in menu_food]
    return data


# 查看当前店铺的食品
def shop_food(shop):
    menu_food = MenuFood.query.filter(MenuFood.category_id == shop.id)
    data = [dict(dict(food), **{'goods_id': food.goods_id}) for food in menu_food]
    return data


# 查看当前店铺
def food_category_api(pub_id):
    store = MerchantShop.query.filter(MerchantShop.pub_id == pub_id).first()
    date = {**dict(store), 'commodity': food(store), 'id': store.pub_id}
    return date
