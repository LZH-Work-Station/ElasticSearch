import sys
import time
sys.path.append('/home/lizehan/project/ElasticSearch')
from conf.YamlConfig import YamlConfig
from db.EsConnector import EsConnector
from entity.DailyPriceOfCompany import DailyPriceOfCompany


if __name__ == '__main__':
    target_company = YamlConfig().config.get("companys")
    date = sys.argv[1]
    es = EsConnector()
    for company in target_company:
        data = DailyPriceOfCompany(company, date)
        if data.data is not None:
            resp = es.index("stockmanager", data)



