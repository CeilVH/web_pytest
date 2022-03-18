# -*- coding:utf-8 -*-
"""
@author:CeiVH
@datetime:2022/2/23 17:10
@note:首页登录
"""
from com.base_page import BasePage
from page_element.login_element import LoginElement
from com.readconfig import read_config


class LoginPage(BasePage):

	def login_click(self):
		"""点击导航栏登录按钮"""
		try:
			locator = self.element_locator(LoginElement.login_title)
		except Exception as e:
			print(e)
		else:
			self.is_click(locator)
			self.inwait(3)

	def login_wrap_check(self):
		"""检查登录弹窗出现"""
		try:
			locator = self.element_locator(LoginElement.login_wrap)
		except Exception as e:
			print(e)
			return False
		else:
			self.inwait(3)
			return locator

	def login_send_username(self):
		"""输入手机号"""
		try:
			locator = self.element_locator(LoginElement.username)
		except Exception as e:
			print(e)
		else:
			self.input_text(locator, read_config.account_username)
			self.inwait(3)

	def login_send_password(self):
		"""输入密码"""
		try:
			locator = self.element_locator(LoginElement.password)
		except Exception as e:
			print(e)
		else:
			self.input_text(locator, read_config.account_password)
			self.inwait(3)

	def loginbtn_click(self):
		"""点击弹窗登录按钮"""
		try:
			locator = self.element_locator(LoginElement.login_button)
		except Exception as e:
			print(e)
		else:
			self.is_click(locator)
			self.inwait(3)

	def to_home_button_check(self):
		"""检查进入后台按钮出现"""
		try:
			locator = self.element_locator(LoginElement.to_home_button)
		except Exception as e:
			print(e)
			return False
		else:
			return locator

	def username_display_check(self):
		"""账号显示检查"""
		try:
			locator = self.element_locator(LoginElement.username_display)
		except Exception as e:
			print(e)
			return False
		else:
			return locator

