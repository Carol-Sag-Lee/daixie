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
