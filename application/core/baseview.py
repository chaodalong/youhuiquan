# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 下午5:26
# @Author  : dalong
# @Site    : 
# @File    : baseview.py
# @Software: PyCharm
from flask.views import View
from flask import session, url_for, redirect

class BaseView(View):
    page_title = ''

    def __init__(self):
        self._checklogin()

    def _checklogin(self):
        if 'username' not in session:
            return redirect(url_for('bp_admin.login'))
