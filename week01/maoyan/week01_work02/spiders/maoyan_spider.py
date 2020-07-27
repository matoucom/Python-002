# -*- coding: utf-8 -*-

# 使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

import scrapy
from week01_work02.items import Week01Work02Item
from scrapy.selector import Selector

class MaoyanSpiderSpider(scrapy.Spider):
    name = 'maoyan_spider'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        headers = {
            'Cookie': '__mta=50221593.1595494887043.1595497086353.1595749920643.3; uuid_n_v=v1; uuid=161BC870CCC311EA9DCC5DD453C9604E3E40326FE62D4B948818425CF525891F; _csrf=1863dba3df1c82f9c414c308ce99bedac4b63fe82f8aea72f44e840c825c1377; _lxsdk_cuid=1737ae7ed9bc8-0e2d21e998a24d-39647b08-1fa400-1737ae7ed9bc8; _lxsdk=161BC870CCC311EA9DCC5DD453C9604E3E40326FE62D4B948818425CF525891F; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595494887; mojo-uuid=64e19b1d874f43cb48d95bab68ae2bba; mojo-session-id={"id":"f4c4f85a8cef71731a94a7d39f478a07","time":1595860898144}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595860901; mojo-trace-id=2; __mta=50221593.1595494887043.1595749920643.1595860900954.4; _lxsdk_s=17390b8d1e4-7b4-2e-6d7%7C%7C4'
        }
        yield scrapy.Request(url=url, headers=headers, callback = self.parse)

    def parse(self, response):
        # print(response.text)
        # response.text.replace("<dd>", "</dd><dd>")
        # # for i in range(1, 11):

        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')[0:10]
        for movie in movies:
            item = Week01Work02Item()
            child_tag = movie.xpath('./div[contains(@class,"movie-hover-title")]')
            film_title = child_tag[0].xpath('./span/text()')
            # film_score = child_tag[0].xpath('./span/i/text()')
            film_type = child_tag[1].xpath('./text()')
            # film_starring = child_tag[2].xpath('./text()')
            film_time = child_tag[3].xpath('./text()')
            # film_title = movie.xpath('./div[1]/span[1]/text()')
            # film_score = movie.xpath('./div[1]/[@title]')
            # film_type = movie.xpath('./div[1]/span[2]/text()')
            print(film_title.extract_first().strip())
            # 一些电影没有评分，这里会报错"list index out of range"
            # print(film_score.extract()[0] + film_score.extract()[1])
            print(film_type.extract()[1].replace('\n', '').strip())
            # print(film_starring.extract()[1].replace('\n', '').strip())
            print(film_time.extract()[1].replace('\n', '').strip())
            # break
            item['film_title'] = film_title.extract_first().strip()
            item['film_type'] = film_type.extract()[1].replace('\n', '').strip()
            item['film_time'] = film_time.extract()[1].replace('\n', '').strip()
            yield item

        # film_title = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[1]/span[1]/text()')
        # film_score = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[1]/span[2]/i/text()')
        # film_type = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[2]/text()')
        # film_starring = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[3]/text()')
        # film_time = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[4]/text()')
        # print(film_title.extract_first().strip())
        # print(film_score.extract()[0] + film_score.extract()[1])
        # print(film_type.extract()[1].replace('\n', '').strip())
        # print(film_starring.extract()[1].replace('\n', '').strip())
        # print(film_time.extract()[1].replace('\n', '').strip())
        #
        # print('======================')
        #
        # film_title = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd')
        # film_score = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[2]/div[1]/div[2]/a/div/div[1]/span[2]/i/text()')
        # film_type = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[2]/div[1]/div[2]/a/div/div[2]/text()')
        # film_starring = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[2]/div[1]/div[2]/a/div/div[3]/text()')
        # film_time = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[2]/div[1]/div[2]/a/div/div[4]/text()')
        # print(film_title)
        # print(film_score.extract()[0] + film_score.extract()[1])
        # print(film_type.extract()[1].replace('\n', '').strip())
        # print(film_starring.extract()[1].replace('\n', '').strip())
        # print(film_time.extract()[1].replace('\n', '').strip())
