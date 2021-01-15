#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 10:15
# @Author  : CoderCharm
# @File    : production_config.py
# @Software: PyCharm
# @Desc    :
"""

生产环境

我这种是一种方式，简单直观

还有一种是服务一个固定路径放一个配置文件如 /etc/conf 下 xxx.ini 或者 xxx.py文件
然后项目默认读取 /etc/conf 目录下的配置文件，能读取则为生产环境，
读取不到则为开发环境，开发环境配置可以直接写在代码里面(或者配置ide环境变量)

服务器上设置 ENV 环境变量


"""
import os

from typing import Union, Optional
from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Config(BaseSettings):
    # 文档地址 成产环境可以关闭 None
    DOCS_URL: Optional[str] = "/api/v1/docs"
    # # 文档关联请求数据接口 成产环境可以关闭 None
    OPENAPI_URL: Optional[str] = "/api/v1/openapi.json"
    # 禁用 redoc 文档
    REDOC_URL: Optional[str] = None

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 天
    SECRET_KEY: str = '-*&^)()sd(*A%&^aWEQaasda_asdasd*&*)(asd%$#'

    MYSQL_USERNAME: str = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", "admin")
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = os.getenv("MYSQL_HOST", "127.0.0.1")
    MYSQL_DATABASE: str = 'Mall'

    # Mysql地址
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"


config = Config()
