# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 下午5:36
# @Author  : dalong
# @Site    : 
# @File    : user.py.py
# @Software: PyCharm
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.dialects.mysql import (
    INTEGER, TINYINT, TIMESTAMP, VARCHAR, ENUM
)
from application.core.database import BaseModel


class UserModel(BaseModel):
    """
    用户模型类
    """
    __tablename__ = 'user'

    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    username = Column(VARCHAR(64), nullable=False, server_default="")
    password = Column(VARCHAR(32), nullable=False, server_default="")
    roles_id = Column(INTEGER(unsigned=True), nullable=False, server_default=text("2"))

    created_at = Column(
        TIMESTAMP, nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at = Column(
        TIMESTAMP, nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )