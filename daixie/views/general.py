# -*- coding: utf-8 -*-

import StringIO

from flask import Blueprint, url_for, redirect, render_template, Response, request
from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Email, Regexp, EqualTo, DataRequired, Required, ValidationError
from flask.ext.login import login_required, current_user

from daixie.utils.form import Captcha
from daixie.utils.captcha import get_captcha
from daixie.utils.error import DaixieError, fail, success

from daixie.models.user import User
from daixie.biz.user import UserBiz


mod = Blueprint('general', __name__)

@mod.route('/', methods=['GET', 'POST'])
def index():
    '''
    网站首页
    '''
    if current_user.is_authenticated():
        return redirect(url_for('.check_is_activated', id=current_user.id))
    return redirect(url_for('.login'))

@mod.route('/register', methods=['GET', 'POST'])
def register():
    '''
    注册成为普通用户
    '''
    form = RegisterForm()
    if not form.validate_on_submit():
        print form.errors
        return render_template('general/register.html', form=form, nav_register='active')
    user = User(form.email.data, form.passwd.data)

    try:
    	ret = UserBiz.register(user)
    except DaixieError as e:
        fail(e)
    	return render_template('general/register.html', form=form, nav_register='active')        
    success(ret)
    return redirect(url_for('.index'))

    #send email to user for validating
    #user = UserBiz.get_user_by_email(user.email)
    #return redirect(url_for('.send_activate_email', id=user.id, email=user.email))

@mod.route('/login', methods=['GET','POST'])
def login():
    '''
    登录
    '''
    form = LoginForm()
    if not form.validate_on_submit():
        return render_template('general/login.html', form=form, nav_login='active')
    email = form.email.data
    passwd = form.passwd.data
    #auto = form.auto.data
    auto = True

    user = User(email, passwd)

    try:
        ret = UserBiz.user_login(user, auto)
    except DaixieError as e:
        fail(e)
        return render_template('general/login.html', form=form, nav_login='active')
    success(ret)
    return redirect(url_for('.check_is_activated', id=user.id))

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
        ret = UserBiz.send_activate_email(id, email)
        success(ret)
    except DaixieError as e:
        fail(e)    
    return render_template('general/wait_for_activate.html', id=id, email=email)

@mod.route('/check_is_activated/<id>', methods=['GET', 'POST'])
def check_is_activated(id, flash_msg=False):
    try:
        user = UserBiz.get_user_by_id(id)
        ret = UserBiz.check_is_activated(user)
    except DaixieError as e:
        fail(e)
        UserBiz.user_logout()
        return redirect(url_for('.send_activate_email', id=user.id, email=user.email))
    if flash_msg:
        success(ret)
    return redirect(url_for('user.home'))

@mod.route('/activate', methods=['GET', 'POST'])
def activate():
    '''
    激活账号
    '''

    email = request.args.get('email')
    timestamp = request.args.get('timestamp')
    token = request.args.get('token')
    id = request.args.get('id')

    try:
        UserBiz.check_link(email, timestamp, token)
    except DaixieError as e:
        return render_template('error.html', message=e.message)

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

@mod.route('/protocal')
def protocal():
    '''
    协议
    '''
    return render_template('general/protocal.html')

@mod.route('/captcha')
def captcha():
    '''
    获取验证码图片
    '''
    captcha_img = get_captcha()
    buf = StringIO.StringIO()
    captcha_img.save(buf, 'jpeg', quality=70)
    return Response(buf.getvalue(), mimetype='image/jpg')

# forms
def BeTrue(msg):
    def _BeTrue(form, field):
        if not field.data:
            raise ValidationError(msg)
    return _BeTrue

class LoginForm(Form):
    email = TextField(u'邮箱', validators=[DataRequired(), Email()])
    passwd = PasswordField(u'密码', validators=[DataRequired(),Regexp('[\w\d-]{5,20}')])
    auto = BooleanField(u'自动登录', default=False)

class RegisterForm(Form):
    email = TextField(u'邮箱地址*', validators=[DataRequired(), Email(message=u'请填写正确的邮箱地址')])
    passwd = PasswordField(u'密码*', validators=[DataRequired(),Regexp('[\w\d-]{6,20}', message=u'密码必须为6-20位')])
    passwd_confirm = PasswordField(u'确认密码*', validators=[DataRequired(), EqualTo('passwd', message=u'密码不一致')])
    captcha = TextField(u'输入验证码*', validators=[Required(message=u'验证码为必填'), Captcha(message=u'验证码错误')])
    agree = BooleanField(u'我已经认真阅读并同意', default=True, validators=[BeTrue(u'同意此协议才能注册')])