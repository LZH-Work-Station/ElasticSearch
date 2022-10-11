from db.EsConnector import EsConnector
from entity.DailyPriceOfCompany import DailyPriceOfCompany
import sys
sys.path.append('/home/lizehan/project/ElasticSearch')

if __name__ == '__main__':
    target_company = {"IBM", "NNND.FRK", "TCEHY", "TCTZF", "0Z4S.LON", "NNN1.FRK", "TME", "63TA.FRK"}
    date = sys.argv[1]
    es = EsConnector()
    for company in target_company:
        data = DailyPriceOfCompany(company, date)
        if (data.data is not None):
            resp = es.index("test-index", data)



