# -*- coding: utf-8 -*-
# @Time    : 2021/2/9 20:53
# @Author  : SunJiaTong
# @Email   : SunJiaTong@
# @File    : JsonClass.py
# @Software: PyCharm
# @Info :
import json


class JsonCommonMethod(object):

    def __init__(self,data):
        self.data = data
        self.result = None

    def change_to_json(self):
        self.result = json.dumps(self.data, indent=2, sort_keys=True)
        return self.result

