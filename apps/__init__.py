from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'user_bp.user_login'


def user_bp(app):
    from apps.cms import user_bp
    app.register_blueprint(user_bp)


def user_db(app):
    from apps.models import db
    db.init_app(app)


def bootstrap(app):
    from flask_bootstrap import Bootstrap
    Bootstrap(app)


def session(app):
    from flask_session import Session
    Session(app)


def create_app():
    # 初始化
    app = Flask(__name__)
    # 设置配置文件
    app.config.from_object('apps.settings.DevConfig')
    # 初始化
    bootstrap(app)
    # session初始化
    session(app)
    # 设置数据库
    user_db(app)
    # 蓝图注册
    user_bp(app)
    # flask-login插件注册
    login_manager.init_app(app)

    return app


def api_create_app():
    app = Flask(__name__, static_url_path='', static_folder='./web_client')
    # 设置配置文件
    app.config.from_object('apps.settings.DevApiConfig')
    # 设置数据库
    user_db(app)

    from apps.api import api_bp
    app.register_blueprint(api_bp)

    return app
