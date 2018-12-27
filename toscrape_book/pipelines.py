# # -*- coding: utf-8 -*-
import MySQLdb
import time


class MySQLPipeline:
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', 'wenhao151', 'scrapy_db', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            update_sql = """
                                         update book_type SET b_url = %s,b_password = %s  where id = %s
                                     """
            self.cursor.execute(update_sql, (item['url'], item['password'], item['id']))
            self.conn.commit()
        except Exception as e:
            with open('保存失败的文件.txt', 'a',encoding="utf-8") as f:
                f.write(item['name'])
                f.write('\n')
