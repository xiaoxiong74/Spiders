# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
class TencentPipeline(object):
    def __init__(self):
        #在初始化方法中打开文件
        self.fileName = open("tencent.json","wb")

    def process_item(self, item, spider):
        #把数据转换为字典再转换成json
        text = json.dumps(dict(item),ensure_ascii=False)+"\n"
        #写到文件中编码设置为utf-8
        self.fileName.write(text.encode("utf-8"))
        #返回item
        return item

    def close_spider(self,spider):
        #关闭时关闭文件
        self.fileName.close()