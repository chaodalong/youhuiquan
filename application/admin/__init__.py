# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 下午5:24
# @Author  : dalong
# @Site    :
# @File    : user.py.py
# @Software: PyCharm
from flask.blueprints import Blueprint
from .user import UserView
from .dashboard import DashboardView

# blue print
bp_admin = Blueprint('bp_admin', __package__)

# login
bp_admin.add_url_rule('/login', view_func=UserView.as_view('login', action='login'))
# logout
bp_admin.add_url_rule('/logout', view_func=UserView.as_view('logout', action='logout'))
# user list(会员列表)
bp_admin.add_url_rule('/list', view_func=UserView.as_view('user_list', action='list'))

# dashboard
bp_admin.add_url_rule('/dashboard', view_func=DashboardView.as_view('dashboard'))