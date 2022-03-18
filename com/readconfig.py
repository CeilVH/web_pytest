# -*- coding:utf-8 -*-
"""
@author:CeiVH
@datetime:2022/2/22 17:25
@note:读写配置文件封装
"""
import configparser
import os
from selenium.webdriver.common.by import By


class ReadConfig(object):
	# 项目目录
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

	# 页面元素目录
	ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

	# 元素定位类型
	LOCATE_MODE = {
		'xpath': By.XPATH,
		'name': By.NAME,
		'id': By.ID,
		'class_name': By.CLASS_NAME,
		'css': By.CSS_SELECTOR,
		'link_text': By.LINK_TEXT,
		'tag_name': By.TAG_NAME
	}

	def __init__(self):
		curpath = os.path.abspath(os.getcwd())
		# curpath = os.path.abspath(os.path.join(os.getcwd(), '..'))
		self.config = configparser.ConfigParser()
		self.path = os.path.join(curpath, 'conf\\config.ini')
		if not os.path.exists(self.path):
			raise FileNotFoundError(f'配置文件{self.path}不存在!')
		self.config.read(self.path)

	def _get(self, section, option):
		"""获取"""
		return self.config.get(section, option)

	def _set(self, section, option, value):
		"""更新"""
		self.config.set(section, option, value)
		with open(self.path, 'w+') as f:
			self.config.write(f)

	@property
	def url(self):
		return self._get('test_url', 'url')

	@property
	def account_username(self):
		return self._get('test_account', 'phone_number')

	@property
	def account_password(self):
		return self._get('test_account', 'password')


read_config = ReadConfig()
