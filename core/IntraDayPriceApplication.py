import sys
sys.path.append('/home/lizehan/project/ElasticSearch')
from db.EsConnector import EsConnector
from entity.IntradayPriceOfCompany import IntradayPriceOfCompany

if __name__ == '__main__':
    target_company = {"IBM"}
    date = sys.argv[1]
    es = EsConnector()
    for company in target_company:
        data = IntradayPriceOfCompany(company, "15min", date)
        if data.data is not None:
            resp = es.indexIntraday("test-intraday", data)
