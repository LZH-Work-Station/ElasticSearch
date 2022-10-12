import sys
import time
from conf.YamlConfig import YamlConfig
sys.path.append('/home/lizehan/project/ElasticSearch')
from db.EsConnector import EsConnector
from entity.DailyPriceOfCompany import DailyPriceOfCompany


if __name__ == '__main__':
    target_company = YamlConfig().config.get("companys")
    date = sys.argv[1]
    es = EsConnector()
    times = 0
    time.sleep(70)
    for company in target_company:
        times += 1
        data = DailyPriceOfCompany(company, date)
        if (data.data is not None):
            resp = es.index("elk_project_index", data)
        if times == 5:
            time.sleep(70)
            times %= 5



