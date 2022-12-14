import time

import requests
from conf.YamlConfig import *
from loguru import logger
import json


class IntradayPriceOfCompany:

    def __init__(self, company, interval, date):
        self.company = company
        self.interval = interval
        self.type = 'intraday_price'
        self.date = date
        url = self.generate_request_url()
        self.data = None
        self.get_intraday_price(url)

    def generate_request_url(self):
        config = YamlConfig().config
        url = '{api}function=TIME_SERIES_INTRADAY&outputsize=full&symbol={company}&interval={interval}&apikey={apikey}' \
            .format(api=config.get('alphavantage').get('url'), company=self.company, interval=self.interval,
                    apikey=config.get('alphavantage').get('apikey')[1])
        logger.info('Request forward alphavantag4e for intradaySeries of company:' + self.company + ' with url: ' + url)
        return url

    '''
    def generate_request_history_url(self):
        config = YamlConfig().config
        url = '{api}function=TIME_SERIES_INTRADAY&symbol={company}&interval={interval}&apikey={apikey}' \
              .format(api=config.get('alphavantage').get('url'),company = self.company,interval = self.interval, apikey=config.get('alphavantage').get('apikey'))
        logger.info('Request forward alphavantag4e for intradaySeries of company:' + self.company + 'with url' + url)
        return url
    '''

    def get_intraday_price(self, url):
        r = requests.get(url)
        data = r.json()
        try:
            # 代表一分鐘内請求次數過多，導致問題出現，需要等待60s
            while 'Note' in data.keys():
                time.sleep(30)
                r = requests.get(url)
                data = r.json()
            self.data = self.IntradayPriceOfCompanyData(
                data.get('Time Series ({interval})'.format(interval=self.interval)), self.date)
        except Exception as e:
            logger.warning(
                "Can not get the intraday price of " + self.company + " and date = " + self.date + " with the error: " + str(data.keys()))

    class IntradayPriceOfCompanyData:
        def __init__(self, data, date):
            # self.date = date
            self.price_per_gap = []
            for key in data.keys():
                if key[:10] == date:
                    # 增加算法优化数据
                    self.price_per_gap.append({'time': key[11:], 'price': data[key]['1. open']})
