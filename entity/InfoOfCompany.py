import requests
from conf.YamlConfig import *
from loguru import logger
class InfoOfCompany:

    def __init__(self, company):
        self.company = company

    def generate_request_overview_url(self):
        config = YamlConfig().config
        url = '{api}function=OVERVIEW&symbol={company}&apikey={apikey} '\
            .format(api=config.get('alphavantage').get('url'), company=self.company, apikey=config.get('alphavantage').get('apikey'))
        logger.info('Request forward alphavantag4e for companyOverview of company:' + self.company + 'with url: ' + url)
        return url

    def generate_request_income_url(self):
        config = YamlConfig().config
        url = '{api}function=INCOME_STATEMENT&symbol={company}&apikey={apikey} '\
            .format(api=config.get('alphavantage').get('url'), company=self.company, apikey=config.get('alphavantage').get('apikey'))
        logger.info('Request forward alphavantag4e for incomeStatement of company:' + self.company + 'with url: ' + url)
        return url

    def generate_request_balance_url(self):
        config = YamlConfig().config
        url = '{api}function=BALANCE_SHEET&symbol={company}&apikey={apikey} '\
            .format(api=config.get('alphavantage').get('url'), company=self.company, apikey=config.get('alphavantage').get('apikey'))
        logger.info('Request forward alphavantag4e for balanceSheet of company:' + self.company + 'with url: ' + url)
        return url

    def generate_request_cash_url(self):
        config = YamlConfig().config
        url = '{api}function=CASH_FLOW&symbol={company}&apikey={apikey} '\
            .format(api=config.get('alphavantage').get('url'), company=self.company, apikey=config.get('alphavantage').get('apikey'))
        logger.info('Request forward alphavantag4e for cashFlow of company:' + self.company + 'with url: ' + url)
        return url