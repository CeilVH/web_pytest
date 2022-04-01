# -*- coding:utf-8 -*-
"""
@author:CeiVH
@datetime:2022/4/1 15:31
@description: 日志记录工具类
"""

import logging
import setting
from colorlog import ColoredFormatter
from tool.datetime_tool import DateTimeTool


def log_file(output=None):
	"""
	:param output: 默认都输出 只输出控制台 1  只输出日志文件 2
	:return: logger
	"""

	# 路径设置
	now_time = DateTimeTool.get_now_time()
	file_path = setting.LOG_PATH + r'\log_{}.log'.format(now_time)
	file_name = r'\log_{}.log'.format(now_time)
	log = logging.getLogger()
	log.setLevel(logging.DEBUG)

	_console_formatter = ColoredFormatter(
		fmt='%(log_color)s%(asctime)s %(log_color)s%(levelname)s %(log_color)s%(module)s [line:%(log_color)s%(lineno)d]: %(log_color)s%(message)s',
		datefmt="%Y-%m-%d %H:%M:%S",
		reset=True
	)

	# 设置控制台处理器
	_console_handler = logging.StreamHandler()
	_console_handler.setLevel(logging.DEBUG)
	_console_handler.setFormatter(_console_formatter)
	# 设置文件处理器
	_file_handler = logging.FileHandler(filename=file_name, encoding='utf-8')
	_file_handler.setLevel(logging.INFO)
	_file_handler.setFormatter(_console_formatter)

	if not output:
		# 控制台输出
		log.addHandler(_console_handler)
		# 文件输出
		log.addHandler(_file_handler)
		return log
	elif output == 1:
		log.addHandler(_console_handler)
		return log
	elif output == 2:
		log.addHandler(_file_handler)
		return log
	else:
		raise ValueError('output参数错误')


logger = log_file()
