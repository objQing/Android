# !/usr/src/python3
# -*- coding:utf-8 -*-
# Author: Humble test
# @Time: 2019/5/15/23:26

"""
description:登录注册页
"""

class LoginRegisterPage():

    my = ("//android.widget.FrameLayout[@content-desc='我的']")
    login_register = ("com.mingbo.game:id/my_login_text") # “点击登录/注册”
    phone_input = ("com.mingbo.game:id/login_phone_input") # “请输入手机号”
    confirm = ("com.mingbo.game:id/login_next") # 确定
    pwd_input = ("com.mingbo.game:id/password_login_input") # “请输入密码”
    whether_register = ("com.mingbo.game:id/login_phone_msg") # 是否登录
    register_code_login = ("com.mingbo.game:id/menu_text") # 验证码登录
    register_code_input = ("com.mingbo.game:id/code_edit_text") # 验证码输入框
    invalid_code = ("com.mingbo.game:id/code_error_msg") # 无效验证码
    pwd_error = ("com.mingbo.game:id/password_login_msg") # 错误密码文本
    register_input = ("com.mingbo.game:id/toolbar_title") # 输入验证码文本
    edit = ("com.mingbo.game:id/my_info_edit_tv") # 登录成功后编辑

    def __init__(self, driver):
        driver.implicitly_wait(15)

    def click_my(self, driver):
        """点击“我的”"""
        driver.find_element_by_xpath(self.my).click()

    def click_login_register(self, driver):
        """点击“点击登录/注册”"""
        driver.find_element_by_id(self.login_register).click()

    def click_phone_input(self, driver):
        """点击“请输入手机号”"""
        driver.find_element_by_id(self.phone_input).click()

    def input_phone(self, driver, phone):
        """输入手机号"""
        driver.find_element_by_id(self.phone_input).send_keys(phone)

    def click_confirm(self, driver):
        """点击“确定”"""
        driver.find_element_by_id(self.confirm).click()

    def get_pwd_input_text(self, driver):
        """获取“请输入密码文本”"""
        return  driver.find_element_by_id(self.pwd_input).text

    def click_pwd_input(self, driver):
        """点击“请输入密码”"""
        driver.find_element_by_id(self.pwd_input).click()

    def input_pwd(self, driver, pwd):
        """输入密码"""
        driver.find_element_by_id(self.pwd_input).send_keys(pwd)

    def get_whether_register_text(self, driver):
        """手机号是否注册文本"""
        return driver.find_element_by_id(self.whether_register).text

    def click_register_code_login(self, driver):
        """点击验证码登录"""
        driver.find_element_by_id(self.register_code_login).click()

    def click_register_code_input(self, driver):
        """点击验证码输入框"""
        driver.find_element_by_id(self.register_code_input).click()

    def input_register_code(self, driver, register):
        """输入验证码"""
        driver.find_element_by_id(self.register_code_input).send_keys(register)

    def get_invalid_register_code_text(self, driver):
        """获取无效验证码"""
        return driver.find_element_by_id(self.invalid_code).text

    def get_pwd_error_text(self, driver):
        """获取密码错误文本"""
        return  driver.find_element_by_id(self.pwd_error).text

    def get_input_register_text(self, driver):
        """获取输入验证码文本"""
        return driver.find_element_by_id(self.register_input).text

    def get_edit_text(self, driver):
        """获取登录成功后编辑文本"""
        return driver.find_element_by_id(self.edit).text