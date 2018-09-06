from apps.models import BaseModel, db


# 商家店铺信息表
class MerchantShop(BaseModel):
    # 店铺外部ID
    pub_id = db.Column(db.String(16), unique=True, index=True)
    # 店铺名称
    shop_name = db.Column(db.String(32), nullable=False, unique=True)
    # 店铺logo图片
    shop_img = db.Column(db.String(128), default='')
    # 店铺评分
    shop_rating = db.Column(db.Float, default=5.0)
    # 是否是品牌
    brand = db.Column(db.Boolean, default=False)
    # 是否准时送达
    on_time = db.Column(db.Boolean, default=True)
    # 是否蜂鸟配送
    fengniao = db.Column(db.Boolean, default=True)
    # 是否保险
    bao = db.Column(db.Boolean, default=False)
    # 是否有发票
    piao = db.Column(db.Boolean, default=True)
    # 是否准标识
    zhun = db.Column(db.Boolean, default=False)
    # 起送价格
    start_send = db.Column(db.Float, default=0.0)
    # 配送费
    send_cost = db.Column(db.Float, default=0.0)
    # 店铺公告
    notice = db.Column(db.String(210), default='')
    # 优惠信息
    discount = db.Column(db.String(210), default='')
    # 店铺和商家的关系
    merchant_uid = db.Column(db.Integer, db.ForeignKey('merchant_user.id'))
    # 建立反向查询关系
    merchant = db.relationship("MerchantUser", backref="shop")

    def __repr__(self):
        return '<Shop {} --- {}>'.format(self.shop_name, self.merchant)
