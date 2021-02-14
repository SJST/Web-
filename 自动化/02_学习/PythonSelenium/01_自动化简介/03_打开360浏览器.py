# -*- coding: utf-8 -*-
# @Time    : 2021/2/9 10:35
# @Author  : SunJiaTong
# @Email   : SunJiaTong@
# @File    : 03_打开360浏览器.py
# @Software: PyCharm
# @Info : 打开360浏览器

# Opera : 打开360浏览器
"""
    1 . 调用封装的360Chrome方法 打开 360浏览器
    2. 调用get方法 访问百度
    3. 定位元素 输入 查询条件 查询结果
    4. 十秒后 关闭浏览器
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome360()
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys("李智恩图片" + Keys.RETURN)
time.sleep(10)
driver.quit()
