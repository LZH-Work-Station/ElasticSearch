import json

from conf.YamlConfig import *
from loguru import logger
from elasticsearch import Elasticsearch
from lib.EncodeMD5 import *


class EsConnector:

    def __init__(self):
        config = YamlConfig().config
        logger.info("Get ES configuration: " + str(config))
        self.ip_address = config.get("es").get("ip_address")
        self.port = config.get("es").get("port")
        self.es = self.getConnection()
        self.md5 = EncodeMD5()

    def getConnection(self):
        es = Elasticsearch("http://" + self.ip_address + ":" + str(self.port))
        logger.info("Connect to ES successfully")
        return es

    def index(self, index, data):
        try:
            data_in_json = json.dumps(data, default=lambda obj: obj.__dict__)
            id = self.md5.getMD5(data.type, data.date, data.company)
            logger.info("Insert to ES by metadata index: " + index + ", id: " + id + ", data: " + data_in_json)
            resp = self.es.index(index=index, id=id, document=data_in_json)
            logger.info(resp)
        except Exception as e:
            logger.error("Insert to ES failed with error: " + str(e))

    # TODO 增加删改查
    # 删除数据
    #def delete(self, ):
