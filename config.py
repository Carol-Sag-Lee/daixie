# -*- coding: utf-8 -*-

from os.path import dirname,abspath

DIR_CUR = dirname(abspath(__file__))
DIR_CONFS = DIR_CUR + '/../confs'
DIR_LOGS = DIR_CUR + '/../logs'
DIR_RESOURCES = DIR_CUR + '/resources'

#global
PORT = 6666
HOST = 'localhost'
DEBUG = True
ASSETS_DEBUG = True
SITE_NAME = u'代写'
TESTING = True

#secret key
SECRET_KEY = r"42a3e1376f8852d1c0620a3235886bcd712879a3"

# db
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:@localhost/daixie?charset=utf8'
SQLALCHEMY_ECHO = False

# email server
MAIL_ADDR_MY = u'代写 <noreply@daixie.com>'
MAIL_ADDR_ADMINS = ['weirdfishbk201@gmail.com']

MAIL_SERVER = '127.0.0.1'
MAIL_DEFAULT_SENDER = MAIL_ADDR_MY
MAIL_SUPPRESS_SEND = False