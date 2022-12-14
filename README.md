# ElasticSearchES概念

## 1. Elastic Search介绍

Elasticsearch 也是使用 Java 编写的，**它的内部使用 Lucene 做索引与搜索，但是它的目的是使全文检索变得简单， 通过隐藏 Lucene 的复杂性，取而代之的提供一套简单一致的 RESTful API。**

然而，Elasticsearch 不仅仅是 Lucene，并且也不仅仅只是一个全文搜索引擎。 它可以被下面这样准确的形容：

- 一个分布式的**实时文档存储，*每个字段* 可以被索引与搜索**
- 一个分布式**实时分析搜索引擎**
- 能胜任上百个服务节点的扩展，并支持 **PB** 级别的结构化或者非结构化数据





# 启动ES步骤

## 1. 配置nginx

```python
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    
    keepalive_timeout  65;

    server {
        listen       9200;
        server_name  localhost;

        location / {
            proxy_pass http://192.168.231.137:9200;
        }
    }

    
    server {
        listen       5601;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            proxy_pass http://192.168.231.137:5601;
        }
    }

}

```

## 2. 配置kibana

```python
# For more configuration options see the configuration guide for Kibana in
# https://www.elastic.co/guide/index.html

# =================== System: Kibana Server ===================
# Kibana is served by a back end server. This setting specifies the port to use.
#server.port: 5601

# Specifies the address to which the Kibana server will bind. IP addresses and host names are both valid values.
# The default is 'localhost', which usually means remote machines will not be able to connect.
# To allow connections from remote users, set this parameter to a non-loopback address.
server.host: "193.168.231.137"

# Enables you to specify a path to mount Kibana at if you are running behind a proxy.
# Use the `server.rewriteBasePath` setting to tell Kibana if it should remove the basePath
# from requests it receives, and to prevent a deprecation warning at startup.
# This setting cannot end in a slash.
#server.basePath: ""

# Specifies whether Kibana should rewrite requests that are prefixed with
# `server.basePath` or require that they are rewritten by your reverse proxy.
# Defaults to `false`.
#server.rewriteBasePath: false

# Specifies the public URL at which Kibana is available for end users. If
# `server.basePath` is configured this URL should end with the same basePath.
#server.publicBaseUrl: ""

# The maximum payload size in bytes for incoming server requests.
#server.maxPayload: 1048576

# The Kibana server's name. This is used for display purposes.
#server.name: "your-hostname"

# =================== System: Kibana Server (Optional) ===================
# Enables SSL and paths to the PEM-format SSL certificate and SSL key files, respectively.
# These settings enable SSL for outgoing requests from the Kibana server to the browser.
#server.ssl.enabled: false
#server.ssl.certificate: /path/to/your/server.crt
#server.ssl.key: /path/to/your/server.key

# =================== System: Elasticsearch ===================
# The URLs of the Elasticsearch instances to use for all your queries.
# elasticsearch.hosts: ["http://192.168.231.134:9200"]

# If your Elasticsearch is protected with basic authentication, these settings provide
# the username and password that the Kibana server uses to perform maintenance on the Kibana
# index at startup. Your Kibana users still need to authenticate with Elasticsearch, which
# is proxied through the Kibana server.
#elasticsearch.username: "kibana_system"
#elasticsearch.password: "pass"

# Kibana can also authenticate to Elasticsearch via "service account tokens".
# Service account tokens are Bearer style tokens that replace the traditional username/password based configuration.
# Use this token instead of a username/password.
# elasticsearch.serviceAccountToken: "my_token"

```

# 项目需求

## 1. 面板配置

1. 各个公司的股价折线图
2. 根据公司类型，总结各个板块占比
3. 根据公司类型获得增长最多的版块

# API总结

## 1. Time Series Stock Data APIs
**function=TIME_SERIES_INTRADAY:** 可以调取过去两个月短间隔（15分钟）的情况

**Options:**
- symbol=公司名
- interval=1min/5min/15min/30min/60min
- adjusted=true/false
- outputsize=compact/full
- datatype=json/csv


**function=TIME_SERIES_INTRADAY_EXTENDED:** 可以调取过去两年内短间隔的情况

**Options:**
- slice=year1month1/year1month2/.../year2month12
- ...

**Return:**
MetaData:{
1.Information:'Intraday open,high,low,close prices and volume'
2.Symbol:'IBM'
3.LastRefreshed
4.Interval
5.OutputSize
6.TIme Zone
}
TimeSeries{
    time:{
        1.open,2.high,3.low,4.close,5.volume
    }
}




