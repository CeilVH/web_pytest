# -*- coding:utf-8 -*-
"""
@author:CeiVH
@datetime:2022/4/1 15:57
@description: 配置项
"""
import os
from os.path import dirname, join

# 项目根目录
BASE_PATH = dirname(__file__).replace(r'\/'.replace(os.sep, ''), os.sep)
# BASE_PATH = dirname(__file__)
# 日志保存目录
LOG_PATH = join(BASE_PATH, 'logs')

