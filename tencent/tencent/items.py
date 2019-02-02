# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名
    positionname = scrapy.Field()
    #详细链接
    positionLink = scrapy.Field()
    #职位类别
    positionType = scrapy.Field()
    #招聘人数
    peopleNum = scrapy.Field()
    #工作地点
    workLocation = scrapy.Field()
    #发布时间
    publishTime = scrapy.Field()
