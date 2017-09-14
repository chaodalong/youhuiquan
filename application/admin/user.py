# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 下午5:24
# @Author  : dalong
# @Site    : 
# @File    : user.py.py
# @Software: PyCharm
from flask import session, render_template, request, redirect, url_for, \
    flash, current_app, g
from application.core.baseview import BaseView
from application.models.UserModel import UserModel
from application.utils.common import md5


class UserView(BaseView):

    def __init__(self, action):
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
        data = {
            "page_title": self.page_title,
            "app": current_app
        }

        if request.method == 'POST':
            username = request.form['username']
            password = md5(request.form['password'])
            user = UserModel.query.filter(UserModel.username == username).first()
            if user is not None and user.password == password:
                session['username'] = username
                g.login_user = {"username": session['username']}
                data["g"] = g
                return redirect(url_for("bp_admin.dashboard"))
            else:
                flash(u"用户名或密码错误")
                return render_template('user/login.html', data=data)
        else:
            if "username" in session:
                return redirect(url_for("bp_admin.dashboard"))
            else:
                return render_template('user/login.html', data=data)

    def logout(self):
        """
        登出
        :return:
        """
        self.page_title = '登出'

        if 'username' in session:
            del session['username']
        return redirect(url_for('bp_admin.login'))

    @BaseView.checklogin
    def list(self):
        self.page_title = u'会员列表'
        page = int(request.args.get('page', 1))
        print page
        data = {
            "page_title": self.page_title,
            "app": current_app,
            "g": g
        }

        users = UserModel.query.paginate(page, per_page=10)
        data["users"] = users if users else {}

        return render_template('user/list.html', data=data)