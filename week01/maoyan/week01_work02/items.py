# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Week01Work02Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    film_title = scrapy.Field()
    film_type = scrapy.Field()
    film_time = scrapy.Field()


