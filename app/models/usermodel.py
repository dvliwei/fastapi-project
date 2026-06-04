#!/usr/bin/env python
# -*- coding:utf-8 _*-
""" 
@author:liwei 
@description
@license: Apache Licence 
@file: usermodel.py 
@time: 2026/06/04
@contact: php.wei.li@gmail.com
@site:  
@software: PyCharm 
"""
from pydantic import BaseModel


# 定义用户模型类
class UserModel(BaseModel):
    user_id: int
    username: str
    email: str
    password: str = None



# 定义用户创建模型类，继承自用户模型类
class UserCreateModel(UserModel):
    password: str

# 定义用户响应模型类，继承自用户模型类
class UserResponseModel(UserModel):
    pass