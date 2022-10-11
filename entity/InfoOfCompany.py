import requests
from conf.YamlConfig import *
from loguru import logger

class InfoOfCompany:

    def __init__(self, company):
        self.company = company

    def generate_request_url(self):
        config = YamlConfig().config
        url = '{api}function=OVERVIEW&symbol={company}&apikey={apikey} '\
            .format(api=config.get('alphavantage').get('url'), company=self.company, apikey=config.get('alphavantage').get('apikey'))
        logger.info('Request forward alphavantag4e for companyOverview of company:' + self.company + 'with url' + url)
        return url
