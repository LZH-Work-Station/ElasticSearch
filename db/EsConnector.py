from conf.YamlConfig import *
from loguru import logger
from elasticsearch import Elasticsearch


class EsConnector:

    def __init__(self):
        config = YamlConfig().config
        logger.info("Get ES configuration: " + str(config))
        self.ip_address = config.get("es").get("ip_address")
        self.port = config.get("es").get("port")
        self.es = self.getConnection()

    def getConnection(self):
        es = Elasticsearch("http://" + self.ip_address + ":" + str(self.port))
        logger.info("Connect to ES successfully")
        return es

    def index(self, index, id, document):
        try:
            logger.info("Insert to ES by metadata index: " + index + ", id: " + id + ", data: " + document)
            resp = self.es.index(index=index, id=id, document=document)
            logger.info(resp)
        except Exception as e:
            logger.error("Insert to ES failed with error: " + str(e))