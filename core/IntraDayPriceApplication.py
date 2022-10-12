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
    times = 0
    time.sleep(70)
    for company in target_company:
        times += 1
        data = IntradayPriceOfCompany(company, "15min", date)
        if data.data is not None:
            resp = es.indexIntraday("elk_project_index", data)
        if times == 5:
            time.sleep(70)
            times %= 5