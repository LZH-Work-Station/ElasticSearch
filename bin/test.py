import json
import unittest

from db.EsConnector import EsConnector
from entity.DailyPrice import *


# 单元测试类测试代码
class TestCases(unittest.TestCase):
    def test01(self):
        pass

    def test02(self):
        es = EsConnector()
        data = DailyPrice("IBM", "2022-10-03")
        data_in_json = json.dumps(data, default=lambda obj: obj.__dict__)
        resp = es.index(index="test-index", id="13", document=data_in_json)



    def test03(self):
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=9Z5P8Q65555NYU47'
        r = requests.get(url)
        data = r.json()

        print(data)


