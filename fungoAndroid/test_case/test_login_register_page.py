# !/usr/src/python3
# -*- coding:utf-8 -*-
# Author: Humble test
# @Time: 2019/5/19/14:02

from src.pages.login_register_page import LoginRegisterPage
from config.driver_config import DriverConfig
import unittest
import time

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverConfig().get_driver()
        cls.LRC = LoginRegisterPage(cls.driver)
        time.sleep(2)
        cls.LRC.click_my(cls.driver)

    def test_015_login_register_page(self):
        """测试手机号码是否注册"""
        self.LRC.click_login_register(self.driver)
        self.LRC.click_phone_input(self.driver)
        self.LRC.input_phone(self.driver, "18739470419")
        self.assertEqual(r"手机号码已注册，点击确定直接登录", self.LRC.get_whether_register_text(self.driver))
        for i in range(2):
            time.sleep(0.5)
            self.driver.keyevent(4)

    def test_016_login_register_page(self):
        """测试进入验证码页面"""
        self.LRC.click_login_register(self.driver)
        self.LRC.click_phone_input(self.driver)
        self.LRC.input_phone(self.driver, "18739470419")
        self.LRC.click_confirm(self.driver)
        self.assertTrue(r"请输入密码", self.LRC.get_pwd_input_text(self.driver))
        for i in range(3):
            time.sleep(0.5)
            self.driver.keyevent(4)

    def test_017_login_register_page(self):
        """测试输入错误的密码"""
        self.LRC.click_login_register(self.driver)
        self.LRC.click_phone_input(self.driver)
        self.LRC.input_phone(self.driver, "18739470419")
        self.LRC.click_confirm(self.driver)
        self.LRC.input_pwd(self.driver, "123456")
        self.LRC.click_confirm(self.driver)
        time.sleep(1)
        self.assertTrue(r"密码错误，请重新输入", self.LRC.get_pwd_error_text(self.driver))
        for i in range(3):
            time.sleep(0.5)
            self.driver.keyevent(4)

    def test_018_login_register_page(self):
        """测试进入输入验证码页面"""
        self.LRC.click_login_register(self.driver)
        self.LRC.click_phone_input(self.driver)
        self.LRC.input_phone(self.driver, "18739470419")
        self.LRC.click_confirm(self.driver)
        self.LRC.click_register_code_login(self.driver)
        self.assertTrue(r"输入验证码", self.LRC.get_input_register_text(self.driver))
        for i in range(4):
            time.sleep(0.5)
            self.driver.keyevent(4)

    def test_019_login_register_page(self):
        """测试输入无效的验证码"""
        self.LRC.click_login_register(self.driver)
        self.LRC.click_phone_input(self.driver)
        self.LRC.input_phone(self.driver, "18739470419")
        self.LRC.click_confirm(self.driver)
        time.sleep(10)
        self.LRC.click_register_code_login(self.driver)
        self.LRC.click_register_code_input(self.driver)
        self.LRC.input_register_code(self.driver, "122345")
        self.assertTrue(self.LRC.get_invalid_register_code_text(self.driver), r"无效的短信验证码")
        for i in range(4):
            time.sleep(0.5)
            self.driver.keyevent(4)

    def test_020_login_register_page(self):
        """测试输入正确的密码"""
        self.LRC.click_login_register(self.driver)
        self.LRC.click_phone_input(self.driver)
        self.LRC.input_phone(self.driver, "18739470419")
        self.LRC.click_confirm(self.driver)
        self.LRC.input_pwd(self.driver, "xm131400")
        self.LRC.click_confirm(self.driver)
        self.assertTrue(r"编辑", self.LRC.get_edit_text(self.driver))

    @classmethod
    def  tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
