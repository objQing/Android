# !/usr/src/python3
# -*- coding:utf-8 -*-
# Author: Humble test
# @Time: 2019/5/12/15:30

"""
description: 首页
"""

from config.driver_config import DriverConfig
import time

class HomePage():
    driver = DriverConfig().get_driver()
    # 元素属性
    tab_recommend = ("tab_recommend")
    card_name = ("//*[@resource-id='com.mingbo.game:id/card_name']")
    menu_recommend_search = ("com.mingbo.game:id/menu_recommend_search")
    top_search = ("//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]")
    search_back = ("//android.widget.ImageButton")
    banner_image = ("com.mingbo.game:id/banner_image")
    game_detail = ("com.mingbo.game:id/game_detail_community_panel")
    banner_title = ("com.mingbo.game:id/banner_title")
    card_cover_s = ("com.mingbo.game:id/card_cover")
    post_detail_attention = ("com.mingbo.game:id/post_detail_attention")
    card_recyclerView = ("//*[@resource-id='com.mingbo.game:id/card_recyclerView']/android.view.ViewGroup[1]")
    game_download = ("com.mingbo.game:id/game_detail_download")
    card_recyclerView_s = ("//*[@resource-id='com.mingbo.game:id/card_recyclerView']/android.view.ViewGroup")
    article_recommend_s = ("//*[@resource-id='com.mingbo.game:id/main_recyclerView']//android.view.ViewGroup[1]")
    card_type_more = ("com.mingbo.game:id/card_type_more")
    card_type_more_title = ("com.mingbo.game:id/toolbar_title")
    card_type_more_img = ("//android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[2]/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[4]")
    player_home_page_text = ("com.mingbo.game:id/toolbar_title")
    in_card_type_more_img = ("com.mingbo.game:id/wall_author_avatar")
    card_type_more_icon = ("//android.support.v7.widget.RecyclerView/android.view.ViewGroup[2]/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView")
    in_card_type_more_icon = ("//android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView")
    card_type_more_comments = ("//android.view.ViewGroup[2]/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[3]")
    card_type_more_comments_text = ("com.mingbo.game:id/toolbar_title")
    in_card_type_more_comments = ("//android.view.ViewGroup[1]/android.widget.TextView[3]")
    # 点击进入游戏社区
    enter_game_community = ("com.mingbo.game:id/game_detail_game")

    def __init__(self):
        self.driver.implicitly_wait(15)
    # 元素操作
    def click_tab_recommend(self):
        ''' 点击首页 '''
        self.driver.find_element_by_id(self.tab_recommend).click()

    def get_card_name(self):
        """ 获取每周精选文本 """
        return self.driver.find_element_by_xpath(self.card_name).text

    def click_menu_recommend_search(self):
        """ 点击搜索 """
        self.driver.find_element_by_id(self.menu_recommend_search).click()

    def get_top_search_text(self):
        """ 获取热门搜索 文本"""
        return self.driver.find_element_by_xpath(self.top_search).text

    def click_search_back(self):
        """ 搜索页点击回退 """
        self.driver.find_element_by_xpath(self.search_back).click()

    def click_banner_image(self):
        """ 点击页首推荐 """
        self.driver.find_element_by_id(self.banner_image).click()

    def get_game_detail_text(self):
        """ 获取点击进入游戏社区文本"""
        return self.driver.find_element_by_id(self.enter_game_community).text

    def physical_back(self):
        """ 物理返回按键 """
        time.sleep(1.5)
        self.driver.keyevent(4)

    def swipe_banner_img(self):
        """ 滑动 banner """
        time.sleep(1.5)
        banner = self.driver.find_element_by_id(self.banner_image)
        location = banner.location
        size = banner.size
        start_x = location['x'] + int(size['width']*0.8)
        end_x = location['x'] + int(size['width']*0.2)
        y = location['y'] + int(size['height']*0.5)
        self.driver.swipe(start_x, y, end_x, y, duration=500)

    def get_banner_title_text(self):
        """获取banner title 文本"""
        return self.driver.find_element_by_id(self.banner_title).text

    def click_card_cover(self):
        """ 点击本周精选上方图片 """
        self.driver.find_element_by_id(self.card_cover_s).click()

    def get_post_detail_attention(self):
        """ 获取文章详情关注 """
        return self.driver.find_element_by_id(self.post_detail_attention).text

    def click_card_recyclerView(self):
        """点击本周精选的游戏"""
        self.driver.find_element_by_xpath(self.card_recyclerView).click()

    def game_download_text(self):
        """ 获取游戏下载文本"""
        return self.driver.find_element_by_id(self.game_detail).text

    def count_card_recyclerView(self):
        """ 统计本周精选游戏 """
        count = self.driver.find_elements_by_xpath(self.card_recyclerView_s)
        return len(count)

    def click_article_recommend(self):
        """ 点击文章推荐 """
        self.driver.find_element_by_xpath(self.article_recommend_s).click()

    def click_card_type_more(self):
        """ 点击安利墙更多 """
        self.driver.find_element_by_id(self.card_type_more).click()

    def get_card_type_more_title_text(self):
        """获取安利墙的文本"""
        return self.driver.find_element_by_id(self.card_type_more_title).text

    def click_card_type_more_img(self):
        """ 点击安利墙玩家头像 """
        self.driver.find_element_by_xpath(self.card_type_more_img)

    def get_player_home_page_text(self):
        """玩家首页文本"""
        return self.driver.find_element_by_id(self.player_home_page_text).text

    def click_in_card_type_more_img(self):
        """点击安利墙中玩家头像"""
        self.driver.find_element_by_id(self.in_card_type_more_img).click()

    def click_card_type_more_icon(self):
        """点击安利墙icon"""
        self.driver.find_element_by_id(self.card_type_more_icon).click()

    def click_in_card_type_more_icon(self):
        """点击安利墙中icon"""
        self.driver.find_element_by_xpath(self.in_card_type_more_icon).click()

    def click_card_type_more_comments(self):
        """ 点击安利墙评论"""
        self.driver.find_element_by_xpath(self.card_type_more_comments).click()

    def get_card_type_more_comments(self):
        """ 获取评论详情文本"""
        return self.driver.find_element_by_id(self.card_type_more_comments_text).text