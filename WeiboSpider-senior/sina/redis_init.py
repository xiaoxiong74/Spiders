#!/usr/bin/env python
# encoding: utf-8
import redis
import sys
import os

sys.path.append(os.getcwd())
from sina.settings import LOCAL_REDIS_HOST, LOCAL_REDIS_PORT

r = redis.Redis(host=LOCAL_REDIS_HOST, port=LOCAL_REDIS_PORT)

for key in r.scan_iter("weibo_spider*"):
    r.delete(key)

start_uids = [
    '2344728613',
    '2435949333',
    '5226087767'
   # '2803301701',  # 人民日报
   # '1288739185',  # 关晓彤
  #  '5499751075',  # 平安重庆
  #  '1699432410',  # 新华社
  #  '2189496674',  # 重庆头条
 #   '1768198384'   # 天猫
]
for uid in start_uids:
    r.lpush('weibo_spider:start_urls', "https://weibo.cn/%s/info" % uid)

print('redis初始化完毕')
