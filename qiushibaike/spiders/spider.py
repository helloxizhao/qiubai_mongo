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
from time import  sleep
class qiushibaike(scrapy.Spider):
    name = 'qiushibaike'
   #  start_urls = []
   #  for url in range(1,11):
   #      start_urls.append('http://www.qiushibaike.com/8hr/page/'+str(url)+'/?s=4974987')
    def start_requests(self):
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
        urls = []
        for num in range(6,7):
            urls.append('http://www.qiushibaike.com/8hr/page/'+str(num)+'/?s=4974987')
        for url in urls:
            yield  scrapy.Request(url=url,headers=headers,callback=self.parse)
    def parse(self, response):
        selector = Selector(response)
        table = selector.xpath('//*[@class="article block untagged mb15"]')
        #print type(table)
        for line in table:
            item = QiushibaikeItem()
            item['content'] = line.xpath('a[1]/div[@class="content"]/span/text()').extract()[0]
            yield  item

