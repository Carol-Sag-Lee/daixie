# -*- coding: utf-8 -*-

from threading import Thread

from flask import render_template
from flask_mail import Message

from daixie import app, mail

from daixie.utils.error_type import USER_ACTIVATE_TITLE, SEND_EMAIL_SUCCESS, SEND_EMAIL_FAIL
from daixie.utils.error import DaixieError

from daixie.biz import async

class EmailBiz:

	@staticmethod
	@async
	def send_async_email(msg):
		with app.app_context():
			mail.send(msg)
	
	@staticmethod
	def send_activate_email(id, email, url, duration):
		try:
			to = email
			title = USER_ACTIVATE_TITLE
			msg = Message(title, recipients=[to])
			msg.html = render_template('mail/register_active.html', id=str(id), duration=duration, url=url)
			EmailBiz.send_async_email(msg)
			return SEND_EMAIL_SUCCESS
		except:
			raise DaixieError(SEND_EMAIL_FAIL)