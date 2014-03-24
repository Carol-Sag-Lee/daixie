# -*- coding: utf-8 -*-

from daixie.data.db import db_session
from daixie.models.transaction import Transaction

from daixie.utils.error import DaixieError

class TransactionBiz:

    @staticmethod
    def get_transaction_by_id(id):
        transaction = db_session.query(Transaction).get(id)
        return transaction

    @staticmethod
    def get_transaction_by_user_id(user_id):
        transaction_list = db_session.query(Transaction).filter_by(user_id=user_id).order_by(Transaction.id.asc()).all()
        return transaction_list

    @staticmethod
    def get_all_transaction():
        all_transaction_list = db_session.query(Transaction).order_by(Transaction.id.desc()).all()
        return all_transaction_list

    @staticmethod
    def create(user_id, amount, account, type, description):
        try:
            transaction = Transaction(user_id, amount, account, type, description)
            db_session.add(transaction)
            db_session.commit()
        except:
            raise DaixieError(u'生成交易记录失败')
