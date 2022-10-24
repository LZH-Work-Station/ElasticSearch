import time

import requests
from conf.YamlConfig import *
from loguru import logger


class DailyPriceOfCompany:

    def __init__(self, company, date):
        self.company = company
        self.date = date
        self.type = "daily_price"
        url = self.generate_request_url()
        self.data = None
        self.get_daily_price(url)

    def __init__(self, company, date, data):
        self.data = data
        self.type = "daily_price"
        self.company = company
        self.date = date

    def generate_request_url(self):
        config = YamlConfig().config
        api_list = config.get("alphavantage").get("apikey")
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol={company}&apikey={apikey}' \
            .format(company=self.company, apikey=api_list[index])
        logger.info("Request forward alphavantage for dailySeries of company: " + self.company + " with url: " + url)
        return url

    def get_daily_price(self, url):
        r = requests.get(url)
        data = r.json()
        try:
            while 'Note' in data.keys():
                index = index % len(api_list)
                r = requests.get(url)
                data = r.json()
            self.data = self.DailyPriceOfCompanyData(data.get("Time Series (Daily)").get(self.date))
        except Exception as e:
            logger.warning(
                "Can not get the daily price of " + self.company + " and date = " + self.date + " with the error: " + str(
                    data.keys()))

    class DailyPriceOfCompanyData:
        def __init__(self, data):
            self.open_price = float(data.get("1. open"))
            self.highest_price = float(data.get("2. high"))
            self.lowest_price = float(data.get("3. low"))
            self.close_price = float(data.get("4. close"))
            self.volume = int(data.get("5. volume"))
