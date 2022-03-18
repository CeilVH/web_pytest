# -*- coding:utf-8 -*-
"""
@author:CeilVH
@date:2022/02/22 16:37
@note:全局参数
"""
import pytest
from selenium import webdriver


@pytest.fixture(scope='session', autouse=True)
def driver():
	option = webdriver.ChromeOptions()
	option.add_experimental_option('useAutomationExtension', False)
	option.add_experimental_option('excludeSwitches', ['enable-automation'])
	option.add_experimental_option('detach', True)
	driver = webdriver.Chrome(options=option)
	driver.maximize_window()
	return driver