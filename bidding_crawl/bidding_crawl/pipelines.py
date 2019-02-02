# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
from bidding_crawl.settings import *
import json
import pymongo
import datetime
import logging

logger = logging.getLogger(__name__)


class BiddingCrawlPipeline(object):
    def process_item(self, item, spider):
        return item


class TenderDB(object):
    """
    将数据存入数据库
    """

    def __init__(self, db_connect):
        # 连接数据库
        self.connect = db_connect
        self.cursor = self.connect.cursor()  # 创建指针对象
        self.count = 0

    @classmethod
    def from_crawler(cls, crawler):
        logger.info('连接数据库')
        connect = psycopg2.connect(database=PGDB_NAME, user=PGDB_USER, password=PGDB_PASSWD, host=PGDB_HOST,
                                   port=PGDB_PORT)
        return cls(connect)

    def process_item(self, item, spider):
        try:
            # 插入数据
            self.count += 1
            self.cursor.execute(
                """insert into tender_data_test values ('{}')""".format(json.dumps(dict(item))))
            # 提交sql语句
            self.connect.commit()
        except Exception as error:
            # 出现错误时打印错误日志
            print(error)
            # logging.error(error)
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
        print(self.count)
        print('关闭数据库连接')


class DBToMongodb(object):
    """
        将数据存入mongodb数据库
        """

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        logger.info('连接数据库')
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        logger.warning('开始标识！')

    def close_spider(self, spider):
        logger.info('关闭数据库')
        logger.warning('结束标识！')
        self.client.close()

    def process_item(self, item, spider):
        try:
            res = self.db['data'].find_one({"bid_title": item["bid_title"]}, {"release_time": 1, "_id": 1})
            if res is None:
                self.db['data'].insert_one(dict(item))
            else:
                if time_compare(item["release_time"], res["release_time"]):
                    self.db['data'].update_one({"bid_title": item["bid_title"]},
                                               {"$set": {"release_time": item["release_time"]}})
        except Exception as e:
            logger.error(e)
        return item


def time_compare(time1, time2):
    """
    时间比较
    :param time1: 2015-03-05 17:41
    :param time2: 2015-03-05 17:41
    :return: bool
    """

    d1 = datetime.datetime.strptime(time1, '%Y-%m-%d %H:%M')
    d2 = datetime.datetime.strptime(time2, '%Y-%m-%d %H:%M')
    if d1 > d2:
        return True
    else:
        return False
