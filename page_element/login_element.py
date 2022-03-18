# -*- coding:utf-8 -*-
"""
@author:CeiVH
@datetime:2022/2/23 17:27
@note:登录页元素
"""


class LoginElement:
	"""首页登录流程元素"""
	# 导航栏登录
	login_title = ('link_text', '登录')
	# 手机号输入框
	username = ('xpath', '//*[@placeholder="请输入手机号码"]')
	# 密码输入框
	password = ('xpath', '//*[@placeholder="请输入密码"]')
	# 弹窗登录按钮
	login_button = ('xpath', '//*[@class="index-module_loginBtn_2764V"]')
	# 登录弹窗浮层
	login_wrap = ('xpath', '//*[@class="index-module_loginWrap_2kpfQ"]')
	# 进入后台按钮
	to_home_button = ('xpath', '//*[@class="go-to-home"]')
	# 账号名称显示
	username_display = ('xpath', '//*[@class="member-phone"]')


