# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, request, abort

from flask_wtf import Form
from wtforms import TextField, PasswordField, SelectField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from flask_wtf.file import FileField, FileAllowed, FileRequired

from flask.ext.login import login_required, current_user

from daixie.biz.user import UserBiz
from daixie.utils.error import DaixieError, fail, success

mod = Blueprint('user', __name__)

@mod.route('/home')
@login_required
def home():
	'''
	主页
	'''
	return render_template('user/home.html')

@mod.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
	'''
	个人信息
	'''
	form = ProfileForm(obj=current_user)
	if not form.validate_on_submit():
		return render_template('user/setting.html', form=form)
	user = current_user
	form.populate_obj(user)
	#修改个人信息
	try:
		ret = UserBiz.edit_user_profile(user)
		success(ret)
	except DaixieError as e:
		fail(e)
	return redirect(url_for('.profile'))

class ProfileForm(Form):
	sex_choices = [('0', u'男'), ('1', u'女')]
	email = TextField(u'登录邮箱', validators=[DataRequired(), Email()])
	nickname = TextField(u'昵称',[Regexp('[\s|\S]')])
	sex = SelectField(u'性别', choices=sex_choices, default='0')
	description = TextAreaField(u'自我介绍',[Regexp('[\s|\S]')])