# -*- coding: utf-8 -*-

from flask import render_template
from flask_mail import Message

from daixie import mail

from daixie.utils.error_type import USER_ACTIVATE_TITLE, SEND_EMAIL_SUCCESS, SEND_EMAIL_FAIL
from daixie.utils.error import DaixieError

class EmailBiz:
	@staticmethod
	def send_activate_email(id, email):
		try:
			to = email
			title = USER_ACTIVATE_TITLE
			msg = Message(title, recipients=[to])
			msg.html = render_template('mail/register_active.html', id=str(id))
			mail.send(msg)
			return SEND_EMAIL_SUCCESS
		except:
			raise DaixieError(SEND_EMAIL_FAIL)