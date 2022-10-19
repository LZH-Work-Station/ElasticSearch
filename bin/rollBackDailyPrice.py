import time
from concurrent.futures import ThreadPoolExecutor
import requests
from loguru import logger
from entity.DailyPriceOfCompany import DailyPriceOfCompany
from conf.YamlConfig import YamlConfig
from db.EsConnector import EsConnector
from lib.RangeDate import RangeDate


def get_history_price():
    target_company = YamlConfig().config.get("companys")
    es = EsConnector()
    rangeDate = RangeDate()
    dates = rangeDate.get_date_iter("2019-01-01", "2022-10-18")
    pool = ThreadPoolExecutor(max_workers=8)
    for company in target_company:
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol={company}&apikey=B7MFHYK85TIZ85G3".format(
            company=company)
        # 获得该公司的数据
        r = requests.get(url)
        data = r.json()

        while 'Note' in data.keys():
            time.sleep(30)
            r = requests.get(url)
            data = r.json()
        # 按照日期进行es写入
        for date in dates:
            pool.submit(insert_into_es, data, es, company, date)

def insert_into_es(data, es, company, date):
    try:
        daily_company_data = DailyPriceOfCompany.DailyPriceOfCompanyData(data.get("Time Series (Daily)").get(date))
        daily_data = DailyPriceOfCompany(company, date, daily_company_data)
        es.index("stockmanager", daily_data)
    except Exception as e:
        logger.warning(
            "Can not get the daily price of " + company + " and date = " + date + " with the error: " + str(
                data.keys()))



if __name__ == '__main__':
    get_history_price()

