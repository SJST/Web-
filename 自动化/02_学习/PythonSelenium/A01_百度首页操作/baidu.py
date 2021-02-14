# -*- coding: utf-8 -*-
# @Time    : 2021/2/11 15:59
# @Author  : SunJiaTong
# @Email   : SunJiaTong@
# @File    : baidu.py
# @Software: PyCharm
# @Info :
from Config import config as cf
import SeleniumTwoBase
from SeleniumTwoBase.SeleniumBasePage import BasePage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class BaiduPage(BasePage):
    # 打开页面入口  百度首页 在 Config 中配置
    cf.init()
    i_keyword = 'xpath,//input[@id="kw"]'
    b_search = 'id,su'

    def opera(self):
        self.open_homepage()
        self.input_keyword()
        self.click_search()
        time.sleep(6)
        self.driver.quit()

    def open_homepage(self):
        site = cf.get_value('site')  # 从全局变量取百度地址
        self.open(site)

        # 输入搜索关键字

    def input_keyword(self, keys=u'星空物语'):
        self.type(self.i_keyword, keys)

        # 点击搜索

    def click_search(self):
        self.click(self.b_search)


if __name__ == '__main__':
    baidu_class = BaiduPage()
    baidu_class.opera()
