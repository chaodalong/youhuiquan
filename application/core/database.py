# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 下午5:39
# @Author  : dalong
# @Site    : 
# @File    : database.py.py
# @Software: PyCharm
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

BaseModel = db.Model