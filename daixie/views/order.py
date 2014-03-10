# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, request, abort,send_from_directory

from flask_wtf import Form
from wtforms import TextField, PasswordField, SelectField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from flask_wtf.file import FileField, FileAllowed, FileRequired

from flask.ext.login import login_required, current_user
from daixie import app
from daixie.biz.order import OrderBiz
from daixie.utils.error import DaixieError, fail, success
from daixie.models.user import User
from daixie.views import j_login_required

mod = Blueprint('order', __name__)

@mod.route('/my_list')
@login_required
def my_list():
	'''
	查看我的所有订单
	'''
	if current_user.type == User.USER_TYPE.USER:
		order_list = OrderBiz.get_order_list_by_user_id(current_user.id)
	else:
		order_list = OrderBiz.get_order_list_by_solver_id(current_user.id)
	return render_template('order/list.html', order_list=order_list)

@mod.route('/more_info/<int:id>')
@login_required
def more_info(id):
	'''
	查看订单的详细信息
	'''
	order = OrderBiz.get_order_by_id(id)
	if current_user.type == User.USER_TYPE.USER:
		return render_template('order/more_info_for_user.html', order=order)
	else:
		return render_template('order/more_info_for_solver.html', order=order)

@mod.route('/pay')
@login_required
def pay():
	'''
	付款测试-https://stripe.com
	'''
	return render_template('order/pay.html')

@mod.route('/download/<int:id>', methods=['POST', 'GET'])
@j_login_required
def download_file(id):
    order = OrderBiz.get_order_by_id(id)
    filename = order.supp_info
    path = app.config['DIR_RESOURCES'] +'/'+ str(id) +'/'
    return send_from_directory(path, filename, as_attachment=True)