# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 下午5:24
# @Author  : dalong
# @Site    :
# @File    : user.py.py
# @Software: PyCharm
from flask.blueprints import Blueprint
from .user import UserView

# blue print
bp_admin = Blueprint('bp_admin', __package__)

# login
bp_admin.add_url_rule('/login', view_func=UserView.as_view('login', action='login'))