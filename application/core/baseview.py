# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 下午5:26
# @Author  : dalong
# @Site    : 
# @File    : baseview.py
# @Software: PyCharm
from flask.views import View
from flask import session, url_for, redirect, g
from functools import wraps


class BaseView(View):
    methods = ['GET', "POST"]

    page_title = ''

    @classmethod
    def checklogin(cls, func):
        @wraps(func)
        def wrapper(self):
            # login check
            if "username" not in session:
                return redirect(url_for('bp_admin.login'))
            else:
                g.login_user = {"username": session['username']}

            # run func
            return func(self)
        return wrapper