# -*- coding: utf-8 -*-

from datetime import datetime

from daixie.models import enum

from flask.ext.login import UserMixin

from daixie import db

class Order(db.Model, UserMixin):

    __tablename__ = 'order'

    SEX = enum(MALE=0, FEMALE=1)
    USER_TYPE = enum(CS_LOW=0, CS_HIGH=1)
    STATUS = enum(CREATED=0, PAID=1, SOLVEING=2, FINISHED=3)

    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    cs_id = db.Column('cs_id', db.Integer, db.ForeignKey('admin.id'))
    solver_id = db.Column('solver_id', db.Integer, db.ForeignKey('user.id'))
    status = db.Column('status', db.Integer)
    create_time = db.Column('create_time', db.DateTime)
    require_time = db.Column('require_time', db.DateTime)
    expect_time = db.Column('expect_time', db.DateTime)
    title = db.Column('title', db.String)
    description = db.Column('description', db.String)
    supp_info = db.Column('supp_info', db.String)
    log = db.Column('log', db.String)
    expect_hour = db.Column('expect_hour', db.FLOAT)
    actual_hour = db.Column('actual_hour', db.FLOAT)
    extra_item = db.Column('extra_item', db.String)
    extra_money = db.Column('extra_money', db.String)
    order_price = db.Column('order_price', db.FLOAT)

    
    def __init__(self, user_id, cs_id, solver_id, require_time, expect_time, title, expect_hour, \
             order_price, description=None, supp_info=None, extra_item=None, extra_money=None):
        self.user_id = user_id
        self.cs_id = cs_id
        self.solver_id = solver_id
        self.status = Order.STATUS.CREATED
        self.create_time = datetime.now()
        self.require_time = require_time
        self.expect_time = expect_time
        self.title = title
        self.description = description
        self.supp_info = supp_info
        self.log = ''
        self.expect_hour = expect_hour
        self.actual_hour = None
        self.extra_item = extra_item
        self.extra_money = extra_money
        self.order_price = self.order_price


    def __repr__(self):
        return '<Order %d %d %d %d>' % (self.id, self.user_id, self.cs_id, self.solver_id)
