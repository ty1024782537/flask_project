from flask import request, url_for
from apps.forms.form import RegisterUserForm
from apps.cms import user_bp
from flask import render_template, redirect
from flask_login import login_user,logout_user

from apps.models import db
from apps.models.model import MerchantUser


@user_bp.route('/user/', endpoint='user')
def create_user():
    return render_template('todo_main.html')


@user_bp.route('/logan_user/', endpoint='logan_user', methods=('GET', 'POST'))
def logan_user():
    form = RegisterUserForm(request.form)
    if request.method == 'POST' and form.validate():
        # 写入数据库
        mu1 = MerchantUser()
        mu1.set_attr(form.data)
        db.session.add(mu1)
        db.session.commit()
        return redirect(url_for('user_bp.enter_user'))
    # print(form.errors)
    print(form.errors)
    return render_template('todo_add.html', form=form)


@user_bp.route('/enter_user/', endpoint='enter_user', methods=('GET', 'POST'))
def enter_user():
    form = RegisterUserForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.data['username']
        password = form.data['password']
        u1 = MerchantUser.query.filter(MerchantUser.username == username).first()
        if u1 is not None and u1.verify_password(password):
            login_user(u1)
            return redirect(url_for('user_bp.user'))
        else:
            form.password.errors = ['用户名或密码出错']
    return render_template('todo_enter.html', form=form)


@user_bp.route('/out_user/', endpoint='out_user', methods=('GET', 'POST'))
def out_user():
    logout_user()
    return redirect(url_for('user_bp.user'))
