# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 下午5:24
# @Author  : dalong
# @Site    :
# @File    : user.py.py
# @Software: PyCharm
from flask import render_template, current_app, g, redirect
from application.core.baseview import BaseView


class DashboardView(BaseView):

    def __init__(self):
        pass


    @BaseView.checklogin
    def dispatch_request(self):
        data = {
            "page_title": self.page_title,
            "app": current_app,
            "g": g
        }
        return render_template('dashboard/index.html', data=data)