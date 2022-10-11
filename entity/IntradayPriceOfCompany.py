import requests
from conf.YamlConfig import *
from loguru import logger
import json

class IntradayPriceOfCompany:

    def __init__(self,company,interval):
        self.company = company
        self.interval = interval
        self.type ='intraday_price'
        url = self.generate_request_url()
        self.data = None
        self.get_intraday_price(url)

    def generate_request_url(self):
        config = YamlConfig().config
        url = '{api}function=TIME_SERIES_INTRADAY&symbol={company}&interval={interval}&apikey={apikey}' \
              .format(api=config.get('alphavantage').get('url'),company = self.company,interval = self.interval, apikey=config.get('alphavantage').get('apikey'))
        logger.info('Request forward alphavantag4e for intradaySeries of company:' + self.company + 'with url' + url)
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
            self.date = data.get('Meta Data').get('3. Last Refreshed')[:10]
            self.data = self.IntradayPriceOfCompanyData(data.get('Time Series ({interval})'.format(interval=self.interval)),self.date)
        except Exception as e:
            logger.warning("Can not get the daily price of " + self.company + " and date = " + self.date + " with the error: " + str(e))

    class IntradayPriceOfCompanyData:
        def __init__(self, data, date):
            self.date = date
            self.price_with_interval_15min = []
            for key in data.keys():
                if key[:10] == self.date:
                    #增加算法优化数据
                    self.price_with_interval_15min.append({'time':key[11:],'price':data[key]['1. open']})
                else:
                    break

