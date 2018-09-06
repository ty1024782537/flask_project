from flask import request, url_for, flash
from apps.forms.form import RegisterUserForm, UserForm
from apps.cms import user_bp
from flask import render_template, redirect
from flask_login import login_user, logout_user, login_required, current_user

from apps.models import db
from apps.models.model import MerchantUser


@user_bp.route('/user/', endpoint='user')
def create_user():
    return render_template('todo_main.html')


@user_bp.route('/register_user/', endpoint='register_user', methods=('GET', 'POST'))
def register_user():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        # 写入数据库
        mu1 = MerchantUser()
        mu1.set_attr(form.data)
        db.session.add(mu1)
        db.session.commit()
        return redirect(url_for('user_bp.login_user'))
    # print(form.errors)
    return render_template('todo_register.html', form=form)


@user_bp.route('/user_login/', endpoint='user_login', methods=('GET', 'POST'))
def user_login():
    form = RegisterUserForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.data['username']
        password = form.data['password']
        u1 = MerchantUser.query.filter(MerchantUser.username == username).first()
        if u1 is not None and u1.verify_password(password):
            try:
                login_user(u1)
                print(current_user.id)
                return redirect(url_for('user_bp.user'))
            except:
                form.password.errors = ['出错了!!']
        else:
            form.password.errors = ['用户名或密码出错']
        # flash('Invalid username or password.')
    return render_template('todo_login.html', form=form)


@user_bp.route('/out_user/', endpoint='out_user', methods=('GET', 'POST'))
def out_user():
    logout_user()
    return redirect(url_for('user_bp.user'))


# 添加菜品
@user_bp.route('/menu_food/', endpoint='menu_food', methods=('GET', 'POST'))
@login_required
def menu_food():
    if request.method == 'GET':
        return '{}正在添加菜品'.format(current_user.username)
