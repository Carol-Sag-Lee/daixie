# -*- coding: utf-8 -*-


from flask import Blueprint,  url_for, redirect, render_template, request
                            
from flask.ext.login import login_required, current_user
from flask.ext.sqlalchemy import Pagination

from daixie.utils.error import DaixieError, j_ok, j_err

from daixie.models.admin import Admin

from daixie.biz.admin import AdminBiz


mod = Blueprint('admin', __name__)

@mod.route('/cs_qq', methods=['GET'])
@login_required
def j_get_all_cs_qq():
    try:
        all_cs_qq = AdminBiz.get_all_cs_qq()
    except DaixieError as e:
        return j_err(e)

    return j_ok(u'获取所有客服QQ成功', all_cs_qq=all_cs_qq)
