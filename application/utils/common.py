# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 下午5:58
# @Author  : dalong
# @Site    : 
# @File    : common.py.py
# @Software: PyCharm

def md5(str=None):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()