# -*- coding: utf-8 -*-
# 为 Scrapy 增加代理 IP 功能。
# 将保存至 csv 文件的功能修改为保持到 MySQL，并在下载部分增加异常捕获和处理机制。
# 备注：代理 IP 可以使用 GitHub 提供的免费 IP 库。
# todo：把抓代理的功能写成单独的一个文件，返回list，然后倒入到这里（先手动添加代理IP到setting文件中，完成本次作业）
# todo：把抓cookie的也单独弄出来，这样抓代理的可以复用
# todo: 都写mysql里？读的时候从数据库读？
# https://www.kuaidaili.com/free/intr/   #  http://www.89ip.cn/

import scrapy
from scrapy.selector import Selector
from week02_work01.items import Week02Work01Item
from selenium import webdriver
import time
# from fake_useragent import UserAgent

class MaoyanSpiderSpider(scrapy.Spider):
    name = 'maoyan_spider'
    # allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        # url = 'https://maoyan.com/films?showType=3'
        url = 'file:///Users/tmp/Downloads/tmp/maoyantype3.html'
        # ua = UserAgent(verify_ssl=False)
        # print(ua.random)
        try:
            browser = webdriver.Chrome()
            browser.get(url)
            time.sleep(3)
            cookie = browser.get_cookies()
            # print(cookie)
        except Exception as e:
            print(e)
            # break
        finally:
            time.sleep(2)
            browser.close()
        headers = {
            'Cookie': str(cookie),
            # 'User-Agent': ua.random,
        }
        yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies:
            item = Week02Work01Item()
            child_tag = movie.xpath('./div[contains(@class,"movie-hover-title")]')
            film_title = child_tag[0].xpath('./span/text()')
            film_type = child_tag[1].xpath('./text()')
            film_time = child_tag[3].xpath('./text()')
            film_score = child_tag[0].xpath('./span/i/text()')
            film_starring = child_tag[2].xpath('./text()')
            item['film_title'] = film_title.extract_first().strip()
            item['film_type'] = film_type.extract()[1].replace('\n', '').strip()
            item['film_time'] = film_time.extract()[1].replace('\n', '').strip()
            try:
                item['film_score'] = film_score.extract()[0] + film_score.extract()[1]
            except Exception as e:
                item['film_score'] = None
            finally:
                print("%s 's score is %s." % (film_title, film_score))
                pass
            item['film_starring'] = film_starring.extract()[1].replace('\n', '').strip()
            yield item
