# # -*- coding: utf-8 -*-

import MySQLdb


class MySQLPipeline:
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', 'wenhao151', 'scrapy_db', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            select_sql = "select * from book_type where b_name = %s"
            value = [item['name']]
            self.cursor.execute(select_sql, value)
            result = self.cursor.fetchone()
            if result:
                pass
            else:
                update_sql = """
                             insert into book_type (b_name,b_detail_url,b_type) value (%s,%s,%s)
                         """
                self.cursor.execute(update_sql, ([item['name']],[item['detailurl']],[item['type']]))
                self.conn.commit()
        except Exception as e:
            with open('保存失败的文件.txt', 'a') as f:
                f.write(item['name'])
                f.write('\n')
