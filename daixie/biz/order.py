# -*- coding: utf-8 -*-

from daixie.models.order import Order
from daixie.biz.user import UserBiz

from daixie.utils.error import DaixieError

from daixie.data.db import db_session

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
		try:
			#从账户扣钱
			amount = int(order.expect_order_price)*100
			UserBiz.refund(order.user_id, amount)
			order.status = Order.STATUS.PAID
			db_session.add(order)
			db_session.commit()
		except DaixieError as e:
			raise e

	@staticmethod
	def refund(id):
		order = OrderBiz.get_order_by_id(id)
		if not order:
			raise DaixieError(u'订单不存在')
		elif order.status != Order.STATUS.CREATED:
			raise DaixieError(u'该订单已付款')
		try:
			#订单付款失败，偿还从账户中扣除的钱
			amount = int(order.expect_order_price)*100
			UserBiz.recharge(order.user_id, amount)
			order.status = Order.STATUS.CREATED
			db_session.add(order)
			db_session.commit()
		except DaixieError as e:
			raise e