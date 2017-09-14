# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 下午5:24
# @Author  : dalong
# @Site    : 
# @File    : user.py.py
# @Software: PyCharm
from flask import session, render_template, request, redirect, url_for, \
    flash
from application.core.baseview import BaseView
from application.models.UserModel import UserModel
from application.utils.common import md5


class UserView(BaseView):
    methods = ['GET', 'POST']

    def __init__(self, action):
        super(UserView, self).__init__()
        self.action = action

    def dispatch_request(self):
        if not hasattr(self, self.action):
            raise Exception("请求的方法不存在！")
        return getattr(self, self.action)()

    def login(self):
        """
        登录
        :return:
        """
        self.page_title = u'登录'
        if request.method == 'POST':
            username = request.form['username']
            password = md5(request.form['password'])
            user = UserModel.query.filter(UserModel.name == username).first()
            if user is not None and user.password == password:
                session['username'] = username
            else:
                flash(u"用户名或密码错误")
        else:
            return render_template('user/login.html', page_title=self.page_title)

    def logout(self):
        """
        登出
        :return:
        """
        self.page_title = '登出'

        if 'username' in session:
            del session['username']
        return redirect(url_for('bp_admin.login'))