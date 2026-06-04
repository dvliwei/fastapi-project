#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:liwei 
@description
@license: Apache Licence 
@file: main.py 
@time: 2026/06/04
@contact: php.wei.li@gmail.com
@site:  
@software: PyCharm 
"""
import os
from fastapi import FastAPI
import uvicorn
from app.core.config import settings
from app.api.v1 import user

def create_app()->FastAPI:
    """创建 FastAPI 应用实例"""

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="FastAPI Project",
        debug=settings.RELOAD,
        log_level=settings.LOG_LEVEL,
    )

    app.include_router(user.router)

    # 在这里可以添加中间件、路由等
    return app

app = create_app()



def show_routes(app: FastAPI) -> None:
    """打印所有已注册路由（路径、名称、HTTP 方法）"""
    for route in app.routes:
        # APIRoute / Route 都可能存在，APIRoute 有 .methods 属性
        methods = getattr(route, "methods", None)
        name = getattr(route, "name", "<unknown>")
        path = getattr(route, "path", getattr(route, "matcher", "<unknown>"))
        if methods:
            methods_str = ",".join(sorted(methods))
            print(f"{methods_str:10s}  {path}  -> {name}")
        else:
            print(f"{'':10s}  {path}  -> {name}")
#启动前打印路由信息
show_routes(app)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
    )
