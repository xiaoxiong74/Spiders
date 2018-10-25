# -*- coding: utf-8 -*-
'''
@author: xiongyongfu
@contact: xyf_0704@sina.com
@file: beginspider.py
@Software: PyCharm
@time: 2018/10/24 9:38
@desc:
'''
from scrapy import cmdline

cmdline.execute("python sina/redis_init.py".split())
cmdline.execute("scrapy crawl sina".split())