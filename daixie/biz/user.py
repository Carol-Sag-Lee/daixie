# -*- coding: utf-8 -*-

from flask.ext.login import login_user, logout_user

from daixie.data.db import db_session
from daixie.models.user import User

from daixie.utils.error_type import USER_DUPLICATE, USER_REGISTER_OK, USER_LOGOUT_OK, \
    USER_ACTIVATE_OK, USER_NOT_EXIST, USER_LOGIN_OK, USER_LOGOUT_FAIL, EDIT_USER_PROFILE_OK, \
    EDIT_USER_PROFILE_FAIL
from daixie.utils.error import DaixieError

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
        
        return USER_REGISTER_OK

    @staticmethod
    def user_login(user, remember):
        u = db_session.query(User).filter_by(email=user.email, passwd=user.passwd).first()
        if not u:
            raise DaixieError(USER_NOT_EXIST)
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