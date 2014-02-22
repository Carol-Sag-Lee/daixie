# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, request, abort

from flask_wtf import Form
from wtforms import TextField, PasswordField, SelectField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from flask_wtf.file import FileField, FileAllowed, FileRequired

from flask.ext.login import login_required, current_user

from daixie.biz.order import OrderBiz
from daixie.utils.error import DaixieError, fail, success
from daixie.models.user import User

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
	order = OrderBiz.get_order_by_id(id)
	if current_user.type == User.USER_TYPE.USER:
		return render_template('order/more_info_for_user.html', order=order)
	else:
		return render_template('order/more_info_for_solver.html', order=order)