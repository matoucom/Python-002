# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

dbInfo = {
    'host' : 'geekserver',
    'port' : 5201,
    'user' : 'root',
    'password' : 'Xiaobai123!@#',
    'db' : 'maoyan'
}


class ConnDB(object):
    def __init__(self, dbInfo, item):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.item = item

    def run(self, item):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
        # print('aaaaaaaaaa')
        # print(item['film_title'])
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            cur.execute(
                """insert into films(film_title,film_type,film_time,film_score,film_starring)
                values(%s, %s, %s, %s, %s)""",
                (
                    item['film_title'],
                    item['film_type'],
                    item['film_time'],
                    item['film_score'],
                    item['film_starring']
                )
            )
            cur.close()
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        # 关闭数据库连接
        conn.close()


class Week02Work01Pipeline:
    def process_item(self, item, spider):
        film_title = item['film_title']
        film_type = item['film_type']
        film_time = item['film_time']
        film_score = item['film_score']
        film_starring = item['film_starring']
        output = f'{film_title}\t{film_type}\t{film_time}\t{film_score}\t{film_starring}\n\n'
        # print('bbbbbbb')
        with open('./maoyan.txt', 'a+', encoding='utf-8') as a:
            a.write(output)
        db = ConnDB(dbInfo, item)
        db.run(item)
        # print('cccccc')
        return item
