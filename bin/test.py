import json
import unittest
import hashlib

from db.EsConnector import EsConnector
from entity.DailyPrice import *


# 单元测试类测试代码
class TestCases(unittest.TestCase):
    def test01(self):
        pass

    def test02(self):
        es = EsConnector()
        data = DailyPrice("IBM", "2022-09-27")
        resp = es.index("test-index", data)

    def test03(self):
        print("abc")

    def test04(self):
        password = 'abc123'
        SALE = password[:4]  # 取密码的前4位

