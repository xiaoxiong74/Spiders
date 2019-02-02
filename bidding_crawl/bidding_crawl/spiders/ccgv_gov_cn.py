# -*- coding: utf-8 -*-
import scrapy
from bidding_crawl.items import CCGV_ITEM
import re
import logging

logger = logging.getLogger(__name__)


class AuthorSpider(scrapy.Spider):
    name = 'ccgv'
    url = ['http://www.ccgp.gov.cn/cggg/dfgg/gkzb/index.htm']
    for i in range(1, 25):
        url.append('http://www.ccgp.gov.cn/cggg/dfgg/gkzb/index_{}.htm'.format(i))

    start_urls = url

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        item = CCGV_ITEM()
        query = response.xpath('//ul[@class="c_list_bid"]/li')
        # print(response.url, '@' * 30, len(query))
        for q in query:
            try:
                item['bid_title'] = q.xpath('./a/@title').extract_first()
                info = q.xpath('./em')
                item['release_time'] = info[0].xpath('./text()').extract_first()
                item['bidders'] = info[2].xpath('./text()').extract_first()
                area_tmp = info[1].xpath('./text()').extract_first()
                if area_tmp:
                    item['bid_area'] = area_tmp
                else:
                    area_tmp2 = re.search(r'(.*省)|(.*市)|(.*[区|县])', item['bidders'])
                    if area_tmp2:
                        item['bid_area'] = area_tmp2.group()
            except Exception as e:
                logger.error(e, response.url, q, item['bid_title'])
            href = q.xpath('./a/@href').extract_first()
            request = scrapy.Request(response.urljoin(href), self.parse_text, dont_filter=False)
            request.meta['item'] = item
            yield request

        # next_page = response.css('.dw_page ul li')[-1].css('a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

    def parse_text(self, response):
        try:
            item = response.meta['item']
            text = response.xpath('//div[@class="vF_detail_content"]').extract_first()
            text = re.sub(r"'", '"', text)
            item['bid_text'] = text
        except Exception as e:
            logger.error(e)
        yield item
