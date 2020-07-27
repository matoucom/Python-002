# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Week01Work02Pipeline:
    def process_item(self, item, spider):
        film_title = item['film_title']
        film_type = item['film_type']
        film_time = item['film_time']
        output = f'|{film_title}|\t|{film_type}|\t|{film_time}|\n\n'
        with open('./maoyan.txt', 'a+', encoding='utf-8') as a:
            a.write(output)
        return item

