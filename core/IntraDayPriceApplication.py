import sys
import time
from loguru import logger
sys.path.append('/home/lizehan/project/ElasticSearch')
from db.EsConnector import EsConnector
from conf.YamlConfig import YamlConfig
from entity.IntradayPriceOfCompany import IntradayPriceOfCompany

if __name__ == '__main__':
    target_company = YamlConfig().config.get("companys")
    date = sys.argv[1]
    es = EsConnector()
    for company in target_company:
        data = IntradayPriceOfCompany(company, "5min", date)
        if data.data is not None:
            resp = es.indexIntraday("stockmanager", data)