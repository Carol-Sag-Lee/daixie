# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, request, abort, \
get_template_attribute, session

from flask_wtf import Form
from wtforms import TextField, PasswordField, SelectField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from flask_wtf.file import FileField, FileAllowed, FileRequired

from flask.ext.login import login_required, current_user

from daixie.biz.user import UserBiz
from daixie.utils.error import DaixieError, fail, success, j_err, j_ok

import stripe

mod = Blueprint('user', __name__)

@mod.route('/home')
@login_required
def home():
	'''
	主页
	'''
	return render_template('user/home.html', nav_home='active')

@mod.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
	'''
	个人信息
	'''
	form = ProfileForm(obj=current_user)
	if not form.validate_on_submit():
		return render_template('user/setting.html', form=form, nav_profile='active')
	user = current_user
	form.populate_obj(user)
	#修改个人信息
	try:
		ret = UserBiz.edit_user_profile(user)
		success(ret)
	except DaixieError as e:
		fail(e)
	return redirect(url_for('.profile'))

@mod.route('/recharge', methods=['GET', 'POST'])
@login_required
def recharge():
	'''
	充值
	'''
	stripe.api_key = "sk_test_xPY1IwP3MgiPkMlaV8Q76tgt"

	amount = session['data_amount']

	customer = stripe.Customer.create(
		email=current_user.email,
		card=request.form['stripeToken']
	)

	try:
		ret = UserBiz.recharge(current_user.id, amount)
		stripe.Charge.create(
			customer=customer.id,
			amount=amount,
			currency='usd',
			description='账户充值'
			)
	except DaixieError as e:
		fail(e)
	except stripe.CardError as e:
		UserBiz.refund(current_user.id, amount)
		raise e

	success(ret)

	session.pop('data_amount', None)
	session.pop('amount', None)

	return redirect(url_for('.home'))

@mod.route('/charge_amount', methods=['POST'])
@login_required
def charge_amount():
	'''
	选择充值金额
	'''
	form = ChargeAmountForm()
	if not form.validate_on_submit():
		html = get_template_attribute('import/tools.html', 'select_recharge_amount_modal')(form)
		return j_err(u'请选择金额', html=html)
	amount = form.amount.data
	data_amount = int(amount)*100

	session['amount'] = amount
	session['data_amount'] = data_amount
	return render_template('user/recharge.html', nav_recharge='active', amount=amount, data_amount=data_amount)

@mod.route('/view_balance', methods=['POST'])
@login_required
def j_view_balance():
	'''
	查看余额
	'''
	msg = u'您的余额为%d' % current_user.account
	return j_ok(msg)


class ProfileForm(Form):
	sex_choices = [('0', u'男'), ('1', u'女')]
	email = TextField(u'邮箱', validators=[DataRequired(), Email(message=u'请填写正确的邮箱地址')])
	nickname = TextField(u'昵称',[Regexp('[\s|\S]')])
	qq = TextField(u'QQ')
	sex = SelectField(u'性别', choices=sex_choices, default='0')
	description = TextAreaField(u'自我介绍',[Regexp('[\s|\S]')])

class ChargeAmountForm(Form):
	amount_choices = [('10', 10), ('20', 20), ('30', 30)]
	amount = SelectField(u'充值金额($)', choices=amount_choices, default='30')