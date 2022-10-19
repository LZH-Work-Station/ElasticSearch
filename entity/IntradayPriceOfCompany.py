import time

import requests
from conf.YamlConfig import *
from loguru import logger
import json
from datetime import datetime

class IntradayPriceOfCompany:

    def __init__(self, company, interval, date):
        self.company = company
        self.interval = interval
        self.type = 'intraday_price'
        self.date = date
        url = self.generate_request_url()
        self.data = []
        self.get_intraday_price(url)


    def generate_request_url(self):
        config = YamlConfig().config
        url = '{api}function=TIME_SERIES_INTRADAY&outputsize=full&symbol={company}&interval={interval}&apikey={apikey}' \
            .format(api=config.get('alphavantage').get('url'), company=self.company, interval=self.interval,
                    apikey=config.get('alphavantage').get('apikey')[1])
        logger.info('Request forward alphavantage for intradaySeries of company:' + self.company + ' with url: ' + url)
        return url

    def get_intraday_price(self, url):
        logger.info('before get_intraday_price')
        r = requests.get(url)
        data = r.json()
        logger.info('get_intraday_price')
        try:
            # 代表一分鐘内請求次數過多，導致問題出現，需要等待60s
            while 'Note' in data.keys():
                time.sleep(30)
                r = requests.get(url)
                data = r.json()
            data_per_gap = data.get('Time Series ({interval})'.format(interval=self.interval))
            logger.info('Got the intraday price of company'+self.company+'and date'+self.date+'from Api')
            for key in data_per_gap.keys():
                if key[:10] == self.date:
                    #logger.info(key)
                    self.data.append(self.IntradayPriceOfCompanyData(key, data_per_gap[key],
                                                                     self.company, self.interval, self.type))
        except Exception as e:
            logger.warning(
                "Can not get the intraday price of " + self.company + " and date = " + self.date + " with the error: " + str(data.keys()))

    class IntradayPriceOfCompanyData:
        def __init__(self, time, data, company, interval, type):
            self.company = company
            self.interval = interval
            self.type = type

            const = 2*60*60*1000
            dd = datetime.strptime(time, "%Y-%m-%d %H:%M:%S").timestamp()
            self.date = dd*1000+const

            self.data = self.BasicIntradayPriceOfCompanyData(data)

        class BasicIntradayPriceOfCompanyData:
            def __init__(self,data):
                self.open_price = float(data['1. open'])
                self.high_price = float(data['2. high'])
                self.low_price = float(data['3. low'])
                self.close_price = float(data['4. close'])


# class IntradayPriceOfCompany:
#
#     def __init__(self, company, interval, date):
#         self.company = company
#         self.interval = interval
#         self.type = 'intraday_price'
#         self.date = date
#         url = self.generate_request_url()
#         self.data = None
#         self.get_intraday_price(url)
#
#     def generate_request_url(self):
#         config = YamlConfig().config
#         url = '{api}function=TIME_SERIES_INTRADAY&outputsize=full&symbol={company}&interval={interval}&apikey={apikey}' \
#             .format(api=config.get('alphavantage').get('url'), company=self.company, interval=self.interval,
#                     apikey=config.get('alphavantage').get('apikey')[1])
#         logger.info('Request forward alphavantag4e for intradaySeries of company:' + self.company + ' with url: ' + url)
#         return url
#
#     '''
#     def generate_request_history_url(self):
#         config = YamlConfig().config
#         url = '{api}function=TIME_SERIES_INTRADAY&symbol={company}&interval={interval}&apikey={apikey}' \
#               .format(api=config.get('alphavantage').get('url'),company = self.company,interval = self.interval, apikey=config.get('alphavantage').get('apikey'))
#         logger.info('Request forward alphavantag4e for intradaySeries of company:' + self.company + 'with url' + url)
#         return url
#     '''
#
#     def get_intraday_price(self, url):
#         r = requests.get(url)
#         data = r.json()
#         try:
#             # 代表一分鐘内請求次數過多，導致問題出現，需要等待60s
#             while 'Note' in data.keys():
#                 time.sleep(30)
#                 r = requests.get(url)
#                 data = r.json()
#             self.data = self.IntradayPriceOfCompanyData(
#                 data.get('Time Series ({interval})'.format(interval=self.interval)), self.date)
#         except Exception as e:
#             logger.warning(
#                 "Can not get the intraday price of " + self.company + " and date = " + self.date + " with the error: " + str(data.keys()))
#
#     class IntradayPriceOfCompanyData:
#         def __init__(self, data, date):
#             self.price_per_gap = []
#             const = 2*60*60*1000
#             for key in data.keys():
#                 if key[:10] == date:
#                     # 增加算法优化数据
#                     dd = datetime.strptime(key, "%Y-%m-%d %H:%M:%S").timestamp()
#                     self.time.append(dd*1000+const)
#                     self.price_per_gap.append({'open_price': float(data[key]['1. open']),
#                                                'high_price': float(data[key]['2. high']),
#                                                'low_price': float(data[key]['3. low']),
#                                                'close_price': float(data[key]['4. close'])})

