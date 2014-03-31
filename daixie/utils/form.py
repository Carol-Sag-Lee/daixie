# -*- coding: utf-8 -*-

from wtforms import ValidationError

from daixie.utils.captcha import check_captcha

#
# validators
#
class Captcha(object):
    '''
    验证码
    '''
    def __init__(self, message=u'验证码错误'):
        self.message = message

    def __call__(self, form, field):
        if not check_captcha(field.data):
            raise ValidationError(self.message)

class PayAllow(object):
	'''
	客服填写订单实际价格，
	确保用户账户余额能够进行支付
	'''
	def __init__(self, message=u'用户账户余额不足,无法填写订单实际价格'):
		self.message = message

	def __call__(self, form, field):
		if not True:
			raise ValidationError(self.message)
