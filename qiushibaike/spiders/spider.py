#!/usr/bin/env python
#coding=utf-8
from scrapy_redis.spiders import  RedisSpider
from scrapy.selector import  Selector
from scrapy.http import  Request
#from qiushibaike_redis.items import  QiushibaikeRedisItem
import scrapy
from qiushibaike.items import  QiushibaikeItem
from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector

class qiushibaike(scrapy.Spider):
    name = 'qiushibaike'
    redis_key = 'qiushibaike:start_urls'
    start_urls = ['http://www.qiushibaike.com/']
    def parse(self, response):
        selector = Selector(response)
        table = selector.xpath('//*[@class="article block untagged mb15"]')
        #print type(table)
        for line in table:
            item = QiushibaikeItem()
            item['content'] = line.xpath('a[1]/div[@class="content"]/span/text()').extract()[0]
            yield  item
