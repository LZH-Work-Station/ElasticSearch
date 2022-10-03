import requests
from conf.YamlConfig import *
from loguru import logger


class DailyPrice:

    def __init__(self, company, date):
        self.company = company
        self.date = date
        self.type = "daily_price"
        url = self.generate_request_url()
        self.get_daily_price(url)

    def generate_request_url(self):
        config = YamlConfig().config
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={company}&apikey={apikey}' \
            .format(company=self.company, apikey=config.get("alphavantage").get("apikey"))
        logger.info("Request forward alphavantage for dailySeries of company: " + self.company + " with url: " + url)
        return url

    def get_daily_price(self, url):
        r = requests.get(url)
        data = r.json()
        self.daily_price_data = self.DailyPriceData(data.get("Time Series (Daily)").get(self.date))

    class DailyPriceData:
        def __init__(self, data):
            self.open_price = float(data.get("1. open"))
            self.highest_price = float(data.get("2. high"))
            self.lowest_price = float(data.get("3. low"))
            self.close_price = float(data.get("4. close"))
            self.volume = int(data.get("5. volume"))
