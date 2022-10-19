import hashlib

from db.EsConnector import EsConnector
from loguru import logger
import requests
from entity.DailyPriceOfCompany import *
from entity.IntradayPriceOfCompany import *
from entity.InfoOfCompany import *
import unittest
import json

from datetime import datetime


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
        data = IntradayPriceOfCompany('BABA', '15min', '2022-10-11')
        resp = es.indexIntraday('elk_project_index', data)

    def test21(self):
        es = EsConnector()
        data = InfoOfCompany('IBM')
        resp = es.indexCompany('elk_project_index', data)

    def test22(self):
        dd = '2022-10-10 15:26:00'
        dd = datetime.strptime(dd, "%Y-%m-%d %H:%M:%S")
        print(dd, dd.timestamp())

    def test23(self):
        es = EsConnector()
        data = IntradayPriceOfCompany('BABA', '15min', '2022-10-11').data
        #logger.info(data)
        for dt in data:
            resp = es.indexIntraday('elk_project_index', dt)
        #resp = es.indexIntraday('elk_project_index', data[0])
