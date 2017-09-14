#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 下午5:50
# @Author  : dalong
# @Site    : 
# @File    : app.py.py
# @Software: PyCharm
from application import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
