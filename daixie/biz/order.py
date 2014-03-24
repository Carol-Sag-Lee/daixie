# -*- coding: utf-8 -*-

from daixie.models.order import Order
from daixie.biz.user import UserBiz
from daixie.biz.transaction import TransactionBiz

from daixie.utils.error import DaixieError

from daixie.utils.error_type import PAY_ORDER_SUCCESS

from daixie.data.db import db_session

from flask.ext.login import current_user

from daixie.models.transaction import Transaction


class OrderBiz:

	@staticmethod
	def get_order_by_id(id):
		return Order.query.filter_by(id=id).first()

	@staticmethod
	def get_order_list_by_user_id(user_id):
		return Order.query.filter_by(user_id=user_id).all();

	@staticmethod
	def get_order_list_by_solver_id(solver_id):
		return Order.query.filter_by(solver_id=solver_id).all();

	@staticmethod
	def pay(id):
		order = OrderBiz.get_order_by_id(id)
		if not order:
			raise DaixieError(u'订单不存在')
		elif order.status != Order.STATUS.CREATED:
			raise DaixieError(u'该订单已付款')
		elif order.expect_order_price > current_user.account:
			raise DaixieError(u'账户余额不足')

		try:
			#从账户扣钱
			amount = int(order.expect_order_price)
			UserBiz.refund(order.user_id, amount, Transaction.TYPE.PAY, u'用户对订单进行付款')
			order.status = Order.STATUS.PAID
			db_session.add(order)
			db_session.commit()
		except DaixieError as e:
			OrderBiz.refund(id)
			raise e
		return PAY_ORDER_SUCCESS

	@staticmethod
	def refund(id):
		order = OrderBiz.get_order_by_id(id)
		if not order:
			raise DaixieError(u'订单不存在')
		elif order.status != Order.STATUS.CREATED:
			raise DaixieError(u'该订单已付款')
		try:
			#订单付款失败，偿还从账户中扣除的钱
			amount = int(order.expect_order_price)
			UserBiz.recharge(order.user_id, amount, Transaction.TYPE.REFUND, u'用户付款失败，返回付款金额')
			order.status = Order.STATUS.CREATED
			db_session.add(order)
			db_session.commit()
		except DaixieError as e:
			raise e