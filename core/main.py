import requests
from elasticsearch import Elasticsearch
from loguru import logger
import json

#-----------------------------
# API key = 9Z5P8Q65555NYU47
#-----------------------------

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=9Z5P8Q65555NYU47'
r = requests.get(url)
data = str(r.json())

# data = data.replace("'", "\"")
logger.info(data)

# Create the client instance
es = Elasticsearch("http://192.168.231.137:9200")
logger.info(es)
resp = es.index(index="test-index", id=10, document=data)
print(resp['result'])
