import scrapy
from tencent.items import TencentItem

class TencentpostitionSpider(scrapy.Spider):
    #爬虫名
    name = 'tencent'
    #爬虫域
    allowed_domains = ['tencent.com']
    #设置URL
    url = 'http://hr.tencent.com/position.php?&start='
    #设置页码
    offset = 0
    #默认url
    start_urls = [url+str(offset)]

    def parse(self, response):
        #xpath匹配规则
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()
            # 职位名
            item["positionname"] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详细链接
            item["positionLink"] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            try:
                item["positionType"] = each.xpath("./td[2]/text()").extract()[0]
            except:
                item["positionType"] = '空'
            # 招聘人数
            item["peopleNum"] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item["workLocation"] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item["publishTime"] = each.xpath("./td[5]/text()").extract()[0]
            #把数据交给管道文件
            yield item
        #设置新URL页码
        if(self.offset<2620):
            self.offset += 10
        #把请求交给控制器
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)