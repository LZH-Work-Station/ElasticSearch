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




