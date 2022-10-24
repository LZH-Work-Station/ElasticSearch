import sys
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
    # 连接es
    es = EsConnector()
    # 获得日期
    range_date = RangeDate()
    start_date = sys.argv[1]
    end_date = sys.argv[2]
    dates = range_date.get_date_iter(start_date, end_date)
    pool = ThreadPoolExecutor(max_workers=4)
    # 获得配置
    config = YamlConfig().config
    api_list = config.get('alphavantage').get('apikey')
    index = 0
    for company in target_company:
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol={company}&apikey={apikey}"\
            .format(company=company, apikey=api_list[index])
        # 获得该公司的数据
        r = requests.get(url)
        data = r.json()

        while 'Note' in data.keys():
            index = (index + 1) % len(api_list)
            url = url.format(apikey=api_list[index])
            r = requests.get(url)
            data = r.json()
        # 按照日期进行es写入
        logger.info("Request API with url: " + url)
        for date in dates:
            logger.info(date)
            pool.submit(insert_into_es, data, es, company, date)
        break



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
