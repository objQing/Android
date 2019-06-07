# !/usr/src/python3
# -*- coding:utf-8 -*-
# Author: Humble test
# @Time: 2019/6/6/20:10

from appium import webdriver

desired_caps = {
    "platformName":"Android", # 测试设备
    "platformVersion":"7.1.2", # 测试版本
    "deviceName":"123456790",  # 设备号
    # "app":r"E:\apl\toutiao.apk",  # apk文件在的目录 如果没有下载就下载 下载后可不指定此参数
    "appPackage":"com.tmall.wireless", # 应用包名
    "appActivity":"splash.TMSplashActivity",# 起始的启动页面
    "unicodeKeyboard":False, # 使用 appium输入法
    "reseKeyboard":True, # 还原输入法
    "noReset":True, # 保存app的使用情况
    "newCommandTimeout":6000 # 延迟6000s
}
driver_app = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver_app.implicitly_wait(10)

