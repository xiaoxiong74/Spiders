# WeiboSpider
This is a sina weibo spider built by scrapy



## 项目说明
本项目根据https://github.com/nghuyong/WeiboSpider/tree/search 做了部分修改

该项目爬取的数据字段说明，请移步:[数据字段说明与示例](./data_stracture.md)

### 克隆本项目 && 安装依赖
本项目Python版本为Python3.6
```bash
git clone git@github.com:nghuyong/WeiboSpider.git
cd WeiboSpider
pip install -r requirements.txt
```
除此之外，还需要安装mongodb，phantomjs和redis，百度或谷歌

### 购买账号
小号购买地址(**访问需要翻墙**): http://www.xiaohao.shop/ 

购买普通国内手机号注册的小号即可

![](./images/xiaohao.shop.png)

购买越多，sina/settings.py 中的延迟就可以越低，并发也就可以越大

**将购买的账号复制到`sina/account_build/account.txt`中，格式与`account_sample.txt`保持一致**。

### 构建账号池

```bash
python sina/account_build/login.py
```
运行截图:

![](./images/account_build_screenshot.png)

这是你的mongodb中将多一个账号表，如下所示:

![](./images/account.png)


### 初始化redis
分布式爬虫是所有的爬虫都从redis中获取URL

所以首先向redis中填充初始的URL

请将`sina/redis_init.py`中的 关键词 和 日期修改成你自己需要的

```bash
python sina/redis_init.py
```

### 运行爬虫
```bash
scrapy crawl weibo_spider 
```
可以打开新的终端，开多个进程。

因已设置日志文件，将setting的日志存储部分部分注销即可在终端显示爬取结果，即注销以下部分
# log_file_path = "log/scrapy_{}_{}_{}.log".format(to_day.year,to_day.month,to_day.day)
# LOG_LEVEL = "INFO"
# LOG_FILE = log_file_path

导入pycharm后，也可以直接执行`sina/spider/weibo_spider.py`

该爬虫是示例爬虫，将爬取的是2018-10-28 到 2018-11-06 关键词为重庆公交坠江微博数据和用户数据。

可以根据你的实际需求改写示例爬虫。
