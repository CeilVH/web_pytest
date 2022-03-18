# -*- coding:utf-8 -*-
"""
@author:CeiVH
@datetime:2022/2/22 17:28
@note:
"""
from selenium import webdriver
from com.readconfig import read_config
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import logging

logger = logging.getLogger(__name__)


class BasePage(object):

	def __init__(self, driver):
		# self.driver = webdriver.Chrome()
		self.driver = driver
		self.wait = WebDriverWait(self.driver, 3)

	def open_page(self, url=None):
		"""打开页面"""
		if not url:
			self.driver.get(read_config.url)
			logger.info('打开页面: {}'.format(read_config.url))
		else:
			self.driver.get(url)
			logger.info('打开页面: {}'.format(url))

	def inwait(self, time: int = None):
		"""隐式等待"""
		if not time:
			self.driver.implicitly_wait(2)
		else:
			if isinstance(time, int):
				self.driver.implicitly_wait(time)
			else:
				raise TypeError('time参数类型错误')

	def element_locator(self, *args):
		"""元素定位器"""
		try:
			name, path = list(*args)
			if name not in read_config.LOCATE_MODE.keys():
				raise ValueError(f'参数{name}不是有效的元素定位')
			else:
				locator = self.driver.find_element(read_config.LOCATE_MODE[name], path)
			return locator
		except Exception as e:
			print(e)

	def element_is_visibility(self, locator):
		"""判断元素是否可见"""
		try:
			self.wait.until(ec.visibility_of(locator))
		except Exception as e:
			print(e)
		else:
			return True

	def input_text(self, locator, text):
		"""(清空并)输入文本"""
		locator.clear()
		self.inwait(2)
		locator.send_keys(text)
		logger.info('输入文本: {}'.format(text))

	def is_click(self, locator):
		"""点击元素"""
		if not locator.is_enabled():
			logger.info('元素不可编辑或点击')
		else:
			locator.click()

	@property
	def get_title(self):
		"""获取网页title"""
		return self.driver.title

	def get_text(self, locator):
		"""获取元素文本"""
		return locator.text
