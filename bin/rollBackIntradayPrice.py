import sys
sys.path.append('/home/lizehan/project/ElasticSearch')
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
    # 连接es
    es = EsConnector()
    range_date = RangeDate()
    start_date = sys.argv[1]
    end_date = sys.argv[2]
    dates = range_date.get_date_iter(start_date, end_date)
    # 获得配置
    config = YamlConfig().config
    pool = ThreadPoolExecutor(max_workers=4)
    api_list = config.get('alphavantage').get('apikey')
    index = 0  # 记录是第几个apikey

    for company in target_company:
        url = '{api}function=TIME_SERIES_INTRADAY&outputsize=full&symbol={company}&interval={interval}&apikey={apikey}' \
            .format(api=config.get('alphavantage').get('url'), company=company, interval=interval,
                    apikey=api_list[index])
        logger.info('Request forward alphavantage for intradaySeries of company:' + company + ' with url: ' + url)
        r = requests.get(url)
        data = r.json()

        while 'Note' in data.keys():
            index = (index + 1) % len(api_list)
            url = '{api}function=TIME_SERIES_INTRADAY&outputsize=full&symbol={company}&interval={interval}&apikey={apikey}' \
                .format(api=config.get('alphavantage').get('url'), company=company, interval=interval,
                        apikey=api_list[index])
            r = requests.get(url)
            data = r.json()
        data_per_gap = data.get('Time Series ({interval})'.format(interval=interval))
        for date in dates:
            pool.submit(insert_into_es, data_per_gap, es, company, interval, date)


def insert_into_es(data, es, company, interval, date):
    try:
        for key in data.keys():
            if key[:10] == date:
                intraday_company_data = IntradayPriceOfCompany.IntradayPriceOfCompanyData(key, data[key], company, interval, 'intraday_price')
                es.indexIntraday("stockmanager", intraday_company_data)
    except Exception as e:
        logger.warning(
            "Can not get the intraday price of " + company + " and date = " + date + " with the error: " + str(
                data.keys()))


if __name__ == '__main__':
    get_history_price()
