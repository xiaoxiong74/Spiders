# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LianjiaPipeline(object):

    def process_item(self, item, spider):
        try:
            place = str(item['place'])
            size = str(item['size'])
            price = str(item['price'])
            fb = open("cqlianjia.txt", "a+")
            fb.write(place+' || ' + size+' || ' + price + '\n')
            fb.close()
        except:
            pass

        return item