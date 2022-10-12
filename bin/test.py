import hashlib

from db.EsConnector import EsConnector
from loguru import logger
import requests
from entity.DailyPriceOfCompany import *
from entity.IntradayPriceOfCompany import *
import unittest
import json


# 单元测试类测试代码
class TestCases(unittest.TestCase):
    def test01(self):
        pass

    def test02(self):
        es = EsConnector()
        data = DailyPriceOfCompany("IBM", "2022-09-27")
        resp = es.index("test-index", data)

    def test03(self):
        print("abc")

    def test04(self):
        password = 'abc123'
        SALE = password[:4]  # 取密码的前4位

    def test20(self):
        es = EsConnector()
        data = IntradayPriceOfCompany('IBM', '15min', '2022-10-11')
        resp = es.indexIntraday('test-intraday', data)
