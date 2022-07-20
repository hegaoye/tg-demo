# coding=utf-8
"""
配置上下文 文件
注意配置文件变量必须大写否则错误
"""
import os

_basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.abspath(os.path.dirname(__file__))

# 数据库配置
# DATABASE_PATH = os.path.join(_basedir, '/app/data/data.db')
DATABASE_PATH = os.path.join(_basedir, 'data.db')


# 系統配置文件
# SYS_CONF = os.path.join(_basedir, '/app/sys.conf')
SYS_CONF = os.path.join(_basedir, 'sys.conf')

del os
