import time
from concurrent.futures import ThreadPoolExecutor
import requests
from loguru import logger
from entity.IntradayPriceOfCompany import IntradayPriceOfCompany
from conf.YamlConfig import YamlConfig
from db.EsConnector import EsConnector
from lib.RangeDate import RangeDate


def get_history_price():
    target_company = YamlConfig().config.get("companys")
    interval = '5min'
    config = YamlConfig().config
    es = EsConnector()
    rangeDate = RangeDate()
    dates = rangeDate.get_date_iter("2022-09-22","2022-10-21")
    pool = ThreadPoolExecutor(max_workers=8)
    for company in target_company:
        url = '{api}function=TIME_SERIES_INTRADAY&outputsize=full&symbol={company}&interval={interval}&apikey={apikey}' \
            .format(api=config.get('alphavantage').get('url'), company=company, interval=interval,
                    apikey=config.get('alphavantage').get('apikey')[0])
        logger.info('Request forward alphavantage for intradaySeries of company:' + company + ' with url: ' + url)
        r = requests.get(url)
        data = r.json()
        #logger.info('continue')
        while 'Note' in data.keys():
            time.sleep(30)
            r = requests.get(url)
            data = r.json()
        data_per_gap = data.get('Time Series ({interval})'.format(interval=interval))
        for date in dates:
            pool.submit(insert_into_es, data_per_gap,es, company, interval, date)

def insert_into_es(data, es, company, interval, date):
    try:
        for key in data.keys():
            if key[:10] == date:
                intraday_company_data = IntradayPriceOfCompany.IntradayPriceOfCompanyData(key, data[key],
                                                                                          company, interval, 'intraday_price')
                es.indexIntraday("stockmanager", intraday_company_data)
    except Exception as e:
        logger.warning(
            "Can not get the intraday price of " + company + " and date = " + date + " with the error: " + str(
                data.keys()))

if __name__ == '__main__':
    get_history_price()