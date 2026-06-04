#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:liwei 
@description
@license: Apache Licence 
@file: config.py 
@time: 2026/06/04
@contact: php.wei.li@gmail.com
@site:  
@software: PyCharm 
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """应用配置类"""
    APP_NAME: str = "FastAPI Project"
    APP_VERSION: str = "1.0"

    HOST: str = "127.0.0.1"
    RELOAD: bool = False
    PORT: int = 8000
    LOG_LEVEL: str = "debug"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

#单例默认 全局使用一份配置
settings = Settings()