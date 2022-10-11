from db.EsConnector import EsConnector
from entity.IntradayPriceOfCompany import IntradayPriceOfCompany
import sys

if __name__ == '__main__':
    target_company = {"IBM"}
    date = sys.argv[1]
    es = EsConnector()
    for company in target_company:
        data = IntradayPriceOfCompany(company, "15min", date)
        if data.data is not None:
            resp = es.index("test-intraday", data)

