# !/usr/src/python3
# -*- coding:utf-8 -*-
# Author: Humble test
# @Time: 2019/5/12/15:33

"""
description: 测试首页
"""

import unittest
import time

from src.pages.home_page import HomePage
from src.common.gesture_manipulation import GestureManipulation


class TestHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.sw = GestureManipulation()
        home_page = HomePage()
        cls.home_page = home_page

    def test_01home_page(self):
        """ 测试点击首页 """
        self.home_page.click_tab_recommend()
        self.assertTrue(r"本周精选", self.home_page.get_card_name())

    def test_02home_page(self):
        """ 测试进入搜索页 """
        self.home_page.click_menu_recommend_search()
        self.assertTrue(r"热门搜索", self.home_page.get_top_search_text())
        self.home_page.click_search_back()

    def test_03home_page(self):
        """ 测试进入游戏详情 """
        self.home_page.click_banner_image()
        self.assertTrue(r"点击进入游戏社区", self.home_page.get_game_detail_text())
        self.home_page.physical_back()

    def test_04home_page(self):
        """测试banner是否可滑动"""
        self.home_page.swipe_banner_img()
        self.assertTrue(r"梦幻模拟战", self.home_page.get_banner_title_text())

    def test_05home_page(self):
        """测试“本周精选”上方图片点击"""
        self.home_page.click_card_cover()
        self.assertTrue(r"关注", self.home_page.get_post_detail_attention())
        self.home_page.physical_back()

    def test_06home_page(self):
        """测试点击精选栏游戏"""
        self.home_page.click_card_recyclerView()
        self.assertTrue(r"下载", self.home_page.game_download_text())
        self.home_page.physical_back()

    def test_07home_page(self):
        """测试本周精选游戏数量"""
        self.assertTrue(2, self.home_page.count_card_recyclerView())

    def test_08home_page(self):
        """测试进入文章详情"""
        self.sw.swipe_down(self.home_page.driver)
        self.home_page.click_article_recommend()
        self.assertTrue(r"关注", self.home_page.get_post_detail_attention())
        self.home_page.physical_back()

    def test_09home_page(self):
        """测试点击更多进入安利墙"""
        self.home_page.click_card_type_more()
        self.assertTrue(r"安利墙", self.home_page.get_card_type_more_title_text())
        self.home_page.physical_back()

    def test_11home_page(self):
        """测试点击安利墙中玩家头像"""
        self.home_page.click_card_type_more()
        self.home_page.click_in_card_type_more_img()
        self.assertTrue(r"Ta的主页", self.home_page.get_player_home_page_text())
        self.home_page.physical_back()
        self.home_page.physical_back()

    def test_13home_page(self):
        """测试点击安利墙里面icon"""
        self.home_page.click_card_type_more()
        self.home_page.click_in_card_type_more_icon()
        self.assertTrue(r"预约", self.home_page.game_download_text())
        self.home_page.physical_back()
        self.home_page.physical_back()

    def test_14home_page(self):
        """测试点击安利墙评论"""
        self.home_page.click_card_type_more_comments()
        self.assertTrue(r"评论详情", self.home_page.get_card_type_more_comments())
        self.home_page.physical_back()

    @classmethod
    def tearDownClass(cls):
        pass