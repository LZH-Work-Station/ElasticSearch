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

    def generate_request_url(self):
        config = YamlConfig().config
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol={company}&apikey={apikey}' \
            .format(company=self.company, apikey=config.get("alphavantage").get("apikey"))
        logger.info("Request forward alphavantage for dailySeries of company: " + self.company + " with url: " + url)
        return url

    def get_daily_price(self, url):
        r = requests.get(url)
        data = r.json()
        try:
            while 'Note' in data.keys():
                time.sleep(30)
                r = requests.get(url)
                data = r.json()
            self.data = self.DailyPriceOfCompanyData(data.get("Time Series (Daily)").get(self.date))
        except Exception as e:
            logger.warning(
                "Can not get the daily price of " + self.company + " and date = " + self.date + " with the error: " + str(
                    e))

    class DailyPriceOfCompanyData:
        def __init__(self, data):
            self.open_price = float(data.get("1. open"))
            self.highest_price = float(data.get("2. high"))
            self.lowest_price = float(data.get("3. low"))
            self.close_price = float(data.get("4. close"))
            self.volume = int(data.get("5. volume"))
