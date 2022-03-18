# -*- coding:utf-8 -*-
"""
@author:CeiVH
@datetime:2022/2/22 18:25
@note:
"""
import pytest
from page_object.login_page import LoginPage
from com.readconfig import read_config

class TestLoginControl:

	@pytest.fixture(scope='function', autouse=True)
	def open_index(self, driver):
		"""打开首页"""
		loginpage = LoginPage(driver)
		loginpage.open_page()

	def test_login_case(self, driver):
		"""登录"""
		loginpage = LoginPage(driver)
		assert loginpage.get_title == '客群帮帮'
		loginpage.login_click()
		locator = loginpage.login_wrap_check()
		assert loginpage.element_is_visibility(locator)
		loginpage.login_send_username()
		loginpage.login_send_password()
		loginpage.loginbtn_click()
		# 检查流程
		locator = loginpage.to_home_button_check()
		assert loginpage.element_is_visibility(locator)
		locator = loginpage.username_display_check()
		assert loginpage.element_is_visibility(locator)
		account = loginpage.get_text(locator)
		assert account == read_config.account_username

