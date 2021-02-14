# -*- coding: utf-8 -*-
# @Time    : 2021/2/14 19:06
# @Author  : SunJiaTong
# @Email   : SunJiaTong@
# @File    : 00_T3C场景自动化设计思路.py
# @Software: PyCharm
# @Info : 如何实现自动化
"""
    1.前期准备 封装 360 浏览器插件 driver
    2. 创建基础类 (基类)封装 selenium 方法
    3. 设置入口方法 config + home 对象
    4. 每个模块 为基类的一个子类 继承基类
    5. 每条用例 组合哥哥 子类 测试
"""
