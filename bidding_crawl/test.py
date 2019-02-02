if __name__ == "__main__":
    # client = None
    # try:
    #     client = pymongo.MongoClient('mongodb://192.168.110.51:27017')
    #     db = client['test']
    #     res=db['tender'].find_one({"tender_title": "费县经济开发区朱龙河景观改造绿化工程项目公开招标公告"},
    #                       {"release_time": 1, "tender_title": 1, "_id": 0})
    #     print(res,type(res))
    # finally:
    #     client.close()

    import time, datetime
    import os

    count = 0
    while True:
        count += 1
        print(datetime.datetime.now(), '第%s次运行爬虫' % count)
        os.system("scrapy crawl ccgv")
        time.sleep(120)
