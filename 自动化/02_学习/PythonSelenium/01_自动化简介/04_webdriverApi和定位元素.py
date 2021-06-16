# -*- coding: utf-8 -*-
# @Time    : 2021/2/9 20:15
# @Author  : SunJiaTong
# @Email   : SunJiaTong
# @File    : 04_webdriverApi和定位元素.py
# @Software: PyCharm
# @Info :
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, JsonMethod
from JsonMethod import JsonClass


class WebDriverApi(object):
    CookieList = None
    Title = None

    def __init__(self, address, element_key, element_value):
        self.driver = webdriver.Chrome360()
        self.address = address
        self.key = element_key
        self.value = element_value

    def driver_main(self):
        self.driver_get()
        self.driver_get_by_id()
        self.driver_quit()
        pass

    # @Info: 模拟发送get请求
    def driver_get(self):
        self.driver.get(self.address)

    # @Info: 根据id 定位元素
    def driver_get_by_id(self):
        self.driver.find_element_by_id(self.key).send_keys(self.value + Keys.RETURN)
        self.get_cookies()
        self.get_title()

    # @Info: find_element find_element_by 的回调方法 这里就不赘述了

    # @Info 获取 title
    def get_title(self):
        self.Title = self.driver.title
        if self.Title:
            print(self.Title)

    # @Info 获取cookie列表
    def get_cookies(self):
        cl = self.driver.get_cookies()
        if cl:
            self.CookieList = JsonClass.JsonCommonMethod(cl).change_to_json()

    # @Info: 关闭浏览器
    def driver_quit(self):
        """
        关闭浏览器
        """
        time.sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    get_address = 'http://www.baidu.com'
    get_key = 'kw'
    value = '杨晨晨图片'
    WebDriverApiClass = WebDriverApi(get_address, get_key, value)
    WebDriverApiClass.driver_main()
