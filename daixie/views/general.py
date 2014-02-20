# -*- coding: utf-8 -*-

import StringIO

from flask import Blueprint, url_for, redirect, render_template, Response
from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Email, Regexp, EqualTo, DataRequired, Required
                            
from flask.ext.login import login_required, current_user

from daixie.utils.form import Captcha
from daixie.utils.captcha import get_captcha
from daixie.utils.error import DaixieError, fail, success

from daixie.models.user import User
from daixie.biz.user import UserBiz
from daixie.biz.email import EmailBiz


mod = Blueprint('general', __name__)

@mod.route('/', methods=['GET', 'POST'])
def index():
    '''
    网站首页
    '''
    if current_user.is_authenticated():
        return redirect(url_for('user.home'))
    return render_template('general/index.html')

@mod.route('/register', methods=['GET', 'POST'])
def register():
    '''
    注册成为普通用户
    '''
    form = RegisterForm()
    if not form.validate_on_submit():
        print form.errors
        return render_template('general/register.html', form=form, hide_login_link=True)
    user = User(form.email.data, form.passwd.data)

    try:
    	ret = UserBiz.register(user)
    except DaixieError as e:
        fail(e)
    	return render_template('general/register.html', form=form, hide_login_link=True)        
    success(ret)
    #send email to user for validating
    user = UserBiz.get_user_by_email(user.email)
    return redirect(url_for('.send_activate_email', id=user.id, email=user.email))

@mod.route('/login', methods=['GET','POST'])
def login():
    '''
    登录
    '''
    form = LoginForm()
    if not form.validate_on_submit():
        return render_template('general/login.html', form=form)
    email = form.email.data
    passwd = form.passwd.data
    auto = form.auto.data

    user = User(email, passwd)
    try:
        ret = UserBiz.user_login(user, auto)
    except DaixieError as e:
        fail(e)
        return render_template('general/login.html', form=form)
    success(ret)
    return redirect(url_for('user.home'))

@mod.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    '''
    注销
    '''
    try:
        UserBiz.user_logout()
    except DaixieError as e:
        fail(e)
    return redirect(url_for('.index'))

@mod.route('/send_activate_email/<id>&<email>', methods=['GET', 'POST'])
def send_activate_email(id, email):
    '''
    发送验证邮件
    '''
    try:
        ret = EmailBiz.send_activate_email(id, email)
        success(ret)
    except DaixieError as e:
        fail(e)    
    return render_template('general/wait_for_activate.html', id=id, email=email)

@mod.route('/activate/<int:id>')
def activate(id):
    '''
    激活账号
    '''
    #以下需要根据id从数据库中取出相应的user，并更新activate字段
    user = UserBiz.get_user_by_id(id)
    ret = UserBiz.activate_user(user)
    url = url_for("user.home")
    success(ret)
    return render_template("general/activate_ok.html", url=url)

@mod.route('/daixie_rule')
@login_required
def daixie_rule():
    return render_template("general/daixie_rule.html");

@mod.route('/captcha')
def captcha():
    '''
    获取验证码图片
    '''
    captcha_img = get_captcha()
    buf = StringIO.StringIO()
    captcha_img.save(buf, 'jpeg', quality=70)
    return Response(buf.getvalue(), mimetype='image/jpg')

class LoginForm(Form):
    email = TextField(u'邮箱', validators=[DataRequired(), Email()])
    passwd = PasswordField(u'密码', validators=[DataRequired(),Regexp('[\w\d-]{5,20}')])
    auto = BooleanField(u'自动登录', default=False)

class RegisterForm(Form):
    email = TextField(u'邮箱地址*', validators=[DataRequired(), Email()])
    passwd = PasswordField(u'密码*', validators=[DataRequired(),Regexp('[\w\d-]{5,20}', message=u'5-20位')])
    passwd_confirm = PasswordField(u'确认密码*', validators=[DataRequired(), EqualTo('passwd', message=u'密码不一致')])
    captcha = TextField(u'输入验证码*', validators=[Required(message=u'验证码为必填'), Captcha(message=u'验证码错误')])