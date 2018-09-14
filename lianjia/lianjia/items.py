# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import  Item,Field

class LianjiaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    place=Field()    #爬取链家租房信息的-地点
    size=Field()     #爬取链家租房信息的-房屋平米数
    price = Field()  # 爬取链家租房信息的-价格

    pass