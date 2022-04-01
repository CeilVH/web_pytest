# -*- coding:utf-8 -*-
"""
@author:CeiVH
@datetime:2022/4/1 15:26
@description: 时间工具类
"""
import datetime
import time

class DateTimeTool:

	@classmethod
	def get_now_time(cls, format='%Y-%m-%d %H:%M:%S'):
		"""
		获取当前时间，可指定格式
		:param format: 时间格式
		:return: 当前时间
		"""
		return datetime.datetime.now().strftime(format)

	@classmethod
	def get_now_date(cls, format='%Y-%m-%d'):
		"""
		获取当前日期，可指定格式
		:param format: 日期格式
		:return: 当前日期
		"""
		return datetime.datetime.date().strftime(format)

	@classmethod
	def get_now_timestamp_by_second(cls):
		"""
		获取当前时间戳（秒）
		:return: int
		"""
		return int(time.time())

	@classmethod
	def get_now_timestamp_by_millisecond(cls):
		"""
		获取当前时间戳（毫秒）
		:return: int
		"""
		return int(round(time.time() * 1000))

