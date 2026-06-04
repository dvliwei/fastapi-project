#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:liwei 
@description
@license: Apache Licence 
@file: user.py 
@time: 2026/06/04
@contact: php.wei.li@gmail.com
@site:  
@software: PyCharm 
"""
from fastapi import APIRouter
from app.models.usermodel import UserResponseModel

# 创建路由实例

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

# 模拟数据库
fake_users_db = {
    1: {"user_id": 1, "username": "alice", "email": "alice@example.com"},
    2: {"user_id": 2, "username": "bob", "email": "bob@example.com"},
}


# 获取用户列表
@router.get("/list", response_model=list[UserResponseModel])
def get_user_list():
    """获取用户列表"""
    return [UserResponseModel(**user) for user in fake_users_db.values()]