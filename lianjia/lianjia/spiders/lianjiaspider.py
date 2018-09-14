# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from lianjia.items import LianjiaItem

class LianjiaSpider(scrapy.Spider):#必须继承scrapy.Spider

    name = "lianjia"   #名称
    start_urls = ['https://tj.lianjia.com/zufang/']   #URL列表


    def parse(self, response):
        item=LianjiaItem()

        infos=response.xpath('//div[@class="info-panel"]')

        for info  in infos:
            # 获取地点
            place = info.xpath('div/div/a[@class="laisuzhou"]/span/text()').extract()[0].replace('\xa0','')
            # 获取平米数
            size = info.xpath('div/div/span[@class="meters"]/text()').extract()[0].replace('\xa0','')
            # 获取价格
            price = info.xpath('div/div[@class="price"]/span/text()').extract()[0] + info.xpath(
                'div/div[@class="price"]/text()').extract()[0]

            item['place']=place
            item['size'] = size
            item['price'] = price

            yield  item   #返回数据

        #从新设置URL，从第2页到第100页  回调parse方法
        for i in   range(2,101):
            url = 'https://tj.lianjia.com/zufang/pg{}/'.format(str(i))
            yield Request(url, callback=self.parse)  ## 回调