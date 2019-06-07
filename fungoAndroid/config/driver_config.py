# !/usr/src/python3
# -*- coding:utf-8 -*-
# Author: Humble test
# @Time: 2019/5/12/15:23

"""
description: 设备配置文件
"""

from appium import webdriver


class DriverConfig():
    """ 获取driver """
    def get_driver(self):

        try:
            self.desired_caps = {
                "platformName": "Android",  # 指定测试设备
                "platformVersion": "8",  # 指定测试版本
                "deviceName": "xxx",  # 指定设备名字
                # "app":"path/app.apk",   # 如果没有则默认下载
                "appPackage": "com.mingbo.game",  # 测试应用包名
                "appActivity": ".common.SplashActivity",  # 测试应用起始启动页面
                # "unicodeKeyboard": True,  # 使用appium输入法
                "reseKeyboard": True,  # 还原输入法
                "noReset": True,  # 保存app使用情况
                "newCommandTimeout": 6000  # 延迟6000s
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
            return self.driver

        except Exception as e:
            raise e
