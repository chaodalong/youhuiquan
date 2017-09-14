# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 下午5:39
# @Author  : dalong
# @Site    : 
# @File    : database.py.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def init_db(app):
    """
    初始化数据库连接
    :param app:
    :return:
    """

    database_config = app.config.get('DATABASE')
    engine = create_engine(database_config, convert_unicode=True, echo=False)

    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    Base.db_session = db_session
    Base.query = db_session.query_property()

    Base.metadata.create_all(bind=engine)