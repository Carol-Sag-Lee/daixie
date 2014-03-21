# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, request, abort

from flask_wtf import Form
from wtforms import TextField, PasswordField, SelectField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from flask_wtf.file import FileField, FileAllowed, FileRequired

from flask.ext.login import login_required, current_user

from daixie.biz.order import OrderBiz
from daixie.utils.error import DaixieError, fail, success, j_err, j_ok
from daixie.models.user import User

import stripe

mod = Blueprint('order', __name__)

@mod.route('/my_list', methods=['GET', 'POST'])
@login_required
def my_list():
	'''
	查看我的所有订单
	'''
	if current_user.type == User.USER_TYPE.USER:
		order_list = OrderBiz.get_order_list_by_user_id(current_user.id)
	else:
		order_list = OrderBiz.get_order_list_by_solver_id(current_user.id)
	return render_template('order/list.html', order_list=order_list, nav_order='active')

@mod.route('/more_info/<int:id>', methods=['GET', 'POST'])
@login_required
def more_info(id):
	'''
	查看订单的详细信息
	'''
	order = OrderBiz.get_order_by_id(id)
	if current_user.type == User.USER_TYPE.USER:
		return render_template('order/more_info_for_user.html', order=order, nav_order='active')
	else:
		return render_template('order/more_info_for_solver.html', order=order, nav_order='active')

@mod.route('/pay', methods=['POST'])
@login_required
def j_pay():
	'''
	订单付款
	'''
	order_id = request.form['order_id']
	try:
		ret = OrderBiz.pay(order_id)
	except DaixieError as e:
		OrderBiz.refund(order_id)
		j_err(e)

	success(ret)
	return redirect(url_for('user.home'))

@mod.route('/charge', methods=['POST'])
@login_required
def charge():
	'''
	付款测试-https://stripe.com
	付款表单处理
	invalid
	'''

	stripe.api_key = "sk_test_xPY1IwP3MgiPkMlaV8Q76tgt"

	amount = 600

	customer = stripe.Customer.create(
		email='customer@example.com',
		card=request.form['stripeToken']
	)

	stripe.Charge.create(
		customer=customer.id,
		amount=amount,
		currency='usd',
		description='《火鸡总动员》电影票'
	)

	return render_template('order/charge.html', amount=amount, nav_order='active')