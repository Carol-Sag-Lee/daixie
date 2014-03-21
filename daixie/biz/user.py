# -*- coding: utf-8 -*-

import time

from flask import url_for

from flask.ext.login import login_user, logout_user, make_secure_token

from daixie.data.db import db_session
from daixie.models.user import User

from daixie.utils.error_type import USER_DUPLICATE, USER_REGISTER_OK, USER_LOGOUT_OK, \
    USER_ACTIVATE_OK, USER_NOT_EXIST, USER_LOGIN_OK, USER_LOGOUT_FAIL, EDIT_USER_PROFILE_OK, \
    EDIT_USER_PROFILE_FAIL, USER_PASSWORD_FAIL, USER_IS_NOT_ACTIVATED, LINK_OVERDUE, \
    LINK_INVALID, DELETE_USER_OK, RECHARGE_FAIL, RECHARGE_SUCCESS, REFUND_FAIL, REFUND_SUCCESS \
    

from daixie.utils.error import DaixieError
from daixie.biz.email import EmailBiz

class UserBiz:
    @staticmethod
    def get_user_by_id(id):
        user = db_session.query(User).get(id)
        return user

    @staticmethod
    def get_user_by_email(email):
        user = db_session.query(User).filter_by(email=email).first()
        return user

    @staticmethod
    def register(user):
        if UserBiz.get_user_by_email(user.email):
            raise DaixieError(USER_DUPLICATE)

        db_session.add(user)
        db_session.commit()

        login_user(user, remember=True)
        
        return USER_REGISTER_OK

    @staticmethod
    def send_activate_email(id, email):
        timestamp = '%d' % time.time()
        token = make_secure_token(email, timestamp)
        url = url_for('general.activate', id=id, email=email, timestamp=timestamp, token=token, _external=True)
        return EmailBiz.send_activate_email(id, email, url, u'30分钟')

    @staticmethod
    def check_link(email, timestamp, token):
        try:
            timestamp = int(timestamp)
        except:
            timestamp = 0

        diff = time.time() - timestamp
        if diff > 60:
            UserBiz.delete_unactivated_user(email)
            raise DaixieError(LINK_OVERDUE)

        if token != make_secure_token(email, str(timestamp)):
            raise DaixieError(LINK_INVALID)

        return True

    @staticmethod
    def delete_unactivated_user(email):
        user = UserBiz.get_user_by_email(email)
        if not user:
            raise DaixieError(USER_NOT_EXIST)
        db_session.delete(user)
        db_session.commit()
        return DELETE_USER_OK

    @staticmethod
    def check_is_activated(user):
        u = db_session.query(User).filter_by(email=user.email).first()
        if u.activate == User.ACTIVATE.NO:
            raise DaixieError(USER_IS_NOT_ACTIVATED)
        return USER_ACTIVATE_OK

    @staticmethod
    def user_login(user, remember):
        u = db_session.query(User).filter_by(email=user.email).first()
        if not u:
            raise DaixieError(USER_NOT_EXIST)
        if u.passwd != user.passwd:
            raise DaixieError(USER_PASSWORD_FAIL)
        user.id = u.id
        login_user(u, remember=remember)

        return USER_LOGIN_OK

    @staticmethod
    def user_logout():
        try:
            logout_user()
        except:
            raise DaixieError(USER_LOGOUT_FAIL)
        return USER_LOGOUT_OK

    @staticmethod
    def activate_user(user):
        user.activate = User.ACTIVATE.YES
        db_session.commit()

        login_user(user, remember=True)

        return USER_ACTIVATE_OK

    @staticmethod
    def edit_user_profile(user):
        try:
            db_session.add(user)
            db_session.commit()
            login_user(user, remember=True)
        except:
            raise DaixieError(EDIT_USER_PROFILE_FAIL)
        return EDIT_USER_PROFILE_OK

    @staticmethod
    def recharge(id, amount):
        user = UserBiz.get_user_by_id(id)
        if not user:
            raise DaixieError(USER_NOT_EXIST)
        try:
            user.account += int(amount)
            db_session.add(user)
            db_session.commit()
        except:
            raise DaixieError(RECHARGE_FAIL)
        return RECHARGE_SUCCESS

    @staticmethod
    def refund(id, amount):
        user = UserBiz.get_user_by_id(id)
        if not user:
            raise DaixieError(USER_NOT_EXIST)
        try:
            user.account -= int(amount)
            db_session.add(user)
            db_session.commit()
        except:
            raise DaixieError(REFUND_FAIL)
        return REFUND_SUCCESS
