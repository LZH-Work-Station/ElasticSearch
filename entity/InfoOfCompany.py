import requests
from conf.YamlConfig import *
from loguru import logger


class InfoOfCompany:

    def __init__(self, company):
        self.type = 'info_of_company'
        self.company = company
        url_overview = self.generate_request_overview_url()
        #url_income = self.generate_request_income_url()
        #url_balance = self.generate_request_balance_url()
        #url_cash = self.generate_request_cash_url()
        #self.data = self.CompanyInfoData(url_overview, url_income, url_balance, url_cash, self.company)
        self.data = None
        self.get_overview(url_overview,self.company)


    def generate_request_overview_url(self):
        config = YamlConfig().config
        url = '{api}function=OVERVIEW&symbol={company}&apikey={apikey} ' \
            .format(api=config.get('alphavantage').get('url'), company=self.company,
                    apikey=config.get('alphavantage').get('apikey'))
        logger.info('Request forward alphavantage for companyOverview of company:' + self.company + 'with url' + url)
        return url

    def get_overview(self, url, company):
        r = requests.get(url)
        data = r.json()
        try:
            self.data= self.OverviewOfCompanyData(data)
        except Exception as e:
            logger.warning("Can not get the overview of " + company + " with the error: " + str(e))

    class OverviewOfCompanyData:
        def __init__(self, data):
            self.name = data.get('Name')
            self.description = data.get('Description')
            self.CIK = data.get('CIK')
            self.exchange = data.get('Exchange')
            self.currency = data.get('Currency')
            self.country = data.get('USA')
            self.sector = data.get('Sector')
            self.industry = data.get('Industry')
            self.weekHigh52 = data.get('52WeekHigh')
            self.weekLow52 = data.get('52WeekLow')
            self.dayMovingAverage50 = data.get('50DayMovingAverage')
            self.dayMovingAverage200 = data.get('200DayMovingAverage')
    # def generate_request_income_url(self):
    #     config = YamlConfig().config
    #     url = '{api}function=INCOME_STATEMENT&symbol={company}&apikey={apikey} ' \
    #         .format(api=config.get('alphavantage').get('url'), company=self.company,
    #                 apikey=config.get('alphavantage').get('apikey'))
    #     logger.info('Request forward alphavantage for incomeStatement of company:' + self.company + 'with url' + url)
    #     return url
    #
    # def generate_request_balance_url(self):
    #     config = YamlConfig().config
    #     url = '{api}function=BALANCE_SHEET&symbol={company}&apikey={apikey} ' \
    #         .format(api=config.get('alphavantage').get('url'), company=self.company,
    #                 apikey=config.get('alphavantage').get('apikey'))
    #     logger.info('Request forward alphavantage for balanceSheet of company:' + self.company + 'with url' + url)
    #     return url
    #
    # def generate_request_cash_url(self):
    #     config = YamlConfig().config
    #     url = '{api}function=CASH_FLOW&symbol={company}&apikey={apikey} ' \
    #         .format(api=config.get('alphavantage').get('url'), company=self.company,
    #                 apikey=config.get('alphavantage').get('apikey'))
    #     logger.info('Request forward alphavantage for cashFlow of company:' + self.company + 'with url' + url)
    #     return url
    #
    # class CompanyInfoData:
    #     def __init__(self, url_overview, url_income, url_balance, url_cash, company):
    #         self.data_overview = None
    #         self.data_income = None
    #         self.data_balance = None
    #         self.data_cash = None
    #         #self.get_overview(url_overview)
    #         self.get_income(url_income, company)
    #         #self.get_balance(url_balance)
    #         #self.get_cash(url_cash)
    #
    #     def get_overview(self, url, company):
    #         r = requests.get(url)
    #         data = r.json()
    #         try:
    #             self.data_overview = self.IncomeOfCompanyData(data)
    #         except Exception as e:
    #             logger.warning("Can not get the overview of " + company + " with the error: " + str(e))
    #
    #     def get_income(self, url, company):
    #         r = requests.get(url)
    #         data = r.json()
    #         try:
    #             logger.info(data)
    #             self.data_income = self.IncomeOfCompanyData(data)
    #         except Exception as e:
    #             logger.warning("Can not get the income of " + company + " with the error: " + str(e))
    #
    #     def get_balance(self, url, company):
    #         r = requests.get(url)
    #         data = r.json()
    #         try:
    #             self.data_balance = self.IncomeOfCompanyData(data)
    #         except Exception as e:
    #             logger.warning("Can not get the balance of " + company + " with the error: " + str(e))
    #
    #     def get_cash(self, url, company):
    #         r = requests.get(url)
    #         data = r.json()
    #         try:
    #             self.data_cash = self.IncomeOfCompanyData(data)
    #         except Exception as e:
    #             logger.warning("Can not get the cash of " + company + " with the error: " + str(e))
    #
    #     class IncomeOfCompanyData:
    #         def __init__(self, data):
    #             annual_reports = data.get('annualReports')
    #             quarterly_reports = data.get('quarterlyReports')
    #             self.annual_data = []
    #             for d in annual_reports:
    #                 self.annual_data.append({'ending_date': d.get('fiscalDateEnding'),
    #                                          'gross_profit': d.get('grossProfit'),
    #                                          'total_revenue': d.get('totalRevenue'),
    #                                          'cost_revenue': d.get('costOfRevenue'),
    #                                          'operating_income': d.get('operatingIncome'),
    #                                          'operating_expenses': d.get('operatingExpenses')})
    #             self.quarterly_reports = []
    #             for d in quarterly_reports:
    #                 self.quarterly_reports.append({'ending_data': d.get('fiscalDateEnding'),
    #                                                'gross_profit': d.get('grossProfit'),
    #                                                'total_revenue': d.get('totalRevenue'),
    #                                                'cost_revenue': d.get('costOfRevenue'),
    #                                                'operating_income': d.get('operatingIncome'),
    #                                                'operating_expenses': d.get('operatingExpenses')})
