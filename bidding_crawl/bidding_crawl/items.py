# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiddingCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CCGV_ITEM(scrapy.Item):
    # 招标名称
    bid_title = scrapy.Field()
    # 发布时间
    release_time = scrapy.Field()
    # 地区
    bid_area = scrapy.Field()
    # 采购人
    bidders = scrapy.Field()
    # 招标内容
    bid_text = scrapy.Field()
