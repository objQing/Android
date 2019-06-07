# !/usr/src/python3
# -*- coding:utf-8 -*-
# Author: Humble test
# @Time: 2019/5/14/22:08

'''
description:手势操作
'''

import time

class GestureManipulation():

    def swipe_left(self, driver):
        '''左滑'''
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        time.sleep(2)
        driver.swipe(x*3/4, y/4, x/4, y/4, duration=500)


    def swipe_right(self, driver):
        '''右滑'''
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        time.sleep(2)
        driver.swipe(x/4, y/4, x*3/4, y/4, duration=500)

    def swipe_down(self, driver):
        '''下滑'''
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        time.sleep(2)
        driver.swipe(x/2, y*3/4, x/2, y/4, duration=500)

    def swipe_up(self,driver):
        '''上滑'''
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        time.sleep(2)
        driver.swipe(x/2, y/4, x/2, y*3/4, duration=1000)