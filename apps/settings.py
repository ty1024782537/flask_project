from redis import Redis
from datetime import timedelta


class BaseConfig(object):
    pass


class DevConfig(BaseConfig):
    DEBUG = True
    # 数据库注册
    SQLALCHEMY_DATABASE_URI = 'sqlite:///E:\\dj_prj\\flask_project\\my.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Session注册
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis(host='192.168.23.128', port=6380)


class ProductConfig(BaseConfig):
    DEBUG = False


class DevApiConfig(BaseConfig):
    DEBUG = True

    # 数据库注册
    SQLALCHEMY_DATABASE_URI = 'sqlite:///E:\\dj_prj\\flask_project\\my.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOKEN_EXPIRES = 24 * 3600
    SECRET_KEY = 'api_user'
    SMS_LIFETIME = timedelta(seconds=5 * 60)  # 验证码过期时间为5分钟
