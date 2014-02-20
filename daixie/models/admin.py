# -*- coding: utf-8 -*-

from hashlib import md5

from daixie.models import enum

from flask.ext.login import UserMixin

from daixie import db

class Admin(db.Model, UserMixin):

    __tablename__ = 'admin'

    SEX = enum(MALE=0, FEMALE=1)
    USER_TYPE = enum(CS_LOW=0, CS_HIGH=1)

    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.String(45), unique=True, nullable=False)
    passwd = db.Column('passwd', db.String(45), nullable=False)
    type = db.Column('type', db.Integer, nullable=False)

    
    def __init__(self, email, passwd, type=USER_TYPE.USER):
        self.email = email
        self.passwd = md5(passwd).hexdigest()
        self.type = type


    def __repr__(self):
        return '<User %r>' % self.email
