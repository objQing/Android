# !/usr/src/python3
# -*- coding:utf-8 -*-
# Author: Humble test
# @Time: 2019/5/13/23:14

"""
description：debug
"""

from config.driver_config import DriverConfig
import time
from src.common.gesture_manipulation import GestureManipulation

class Swipt():
    swipt = GestureManipulation()

    driver = DriverConfig().get_driver()

    def swipe_banner_img(self):
        """ 滑动 banner """
        self.driver.implicitly_wait(10)
        banner = self.driver.find_element_by_id("com.mingbo.game:id/banner_image")
        location = banner.location
        size = banner.size
        start_x = location['x'] + int(size['width'] * 0.8)
        end_x = location['x'] + int(size['width'] * 0.2)
        y = location['y'] + int(size['height'] * 0.5)
        self.driver.swipe(start_x, y, end_x, y, duration=500)

    def click_game_detail_back(self):
        """ 游戏首页回退上级 """
        time.sleep(2)
        self.driver.keyevent(4)

    def swipes(self):
        time.sleep(3)
        self.swipt.swipe_down(self.driver)

    def click_article_recommend(self):
        """ 点击文章推荐 """
        self.driver.find_element_by_xpath("//*[@resource-id='com.mingbo.game:id/main_recyclerView']//android.view.ViewGroup[1]").click()
    def click_card_type_more_icon(self):
        """点击安利墙icon"""
        self.driver.find_element_by_id("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[2]/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView").click()


# if __name__ == '__main__':
#
#     obj = Swipt()
#     obj.swipes()
#     obj.swipes()
#     obj.click_card_type_more_icon()

import re

r = "test。。。， tess。。。page，离开了的方式， page"
file = re.match(".+page",r)
print(file)