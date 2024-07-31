# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class WbProPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='root0228.', database='worker')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql="insert into wb_scrapy(user,fansCount,followCount,transferCount) " \
              "values (%s, %s, %s, %s)"
        values = (item['user'], item['fansCount'], item['followCount'],item['transferCount'])
        self.cursor.execute(sql, values)
        self.conn.commit()
        return item
