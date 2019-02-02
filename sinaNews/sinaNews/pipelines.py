# -*- coding: utf-8 -*-

from scrapy import signals
import sys


class SinanewsPipeline(object):
    def process_item(self, item, spider):
        sonUrls = item['sonUrls']

        # 文件名为子链接url中间部分，并将 / 替换为 _，保存为 .txt格式
        filename = sonUrls[7:-6].replace('/','_')
        filename += ".txt"

        fp = open(item['subFilename']+'/'+filename, 'w')
        fp.write(item['content'])
        fp.close()

        return item