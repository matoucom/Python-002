# -*- coding: utf-8 -*-

# 使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

import scrapy


class MaoyanSpiderSpider(scrapy.Spider):
    name = 'maoyan_spider'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def parse(self, response):
        pass
