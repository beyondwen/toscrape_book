# # -*- coding: utf-8 -*-
#
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#
#
# # class BookPipeline(object):
# #     review_rating_map = {
# #         'One': 1,
# #         'Two': 2,
# #         'Three': 3,
# #         'Four': 4,
# #         'Five': 5,
# #     }
# #
# #     def process_item(self, item, spider):
# #         rating = item.get('review_rating')
# #         if rating:
# #             item['review_rating'] = self.review_rating_map[rating]
# #             return item
#
import MySQLdb


class MySQLPipeline:
    # def open_spider(self, spider):
    #     db = spider.settings.get('MYSQL_DB_NAME', 'scrapy_db')
    #     host = spider.settings.get('MYSQL_HOST', 'localhost')
    #     port = spider.settings.get('MYSQL_PORT', 3306)
    #     user = spider.settings.get('MYSQL_USER', 'root')
    #     passwd = spider.settings.get('MYSQL_PASSWORD', '123456')
    #     self.db_conn = MySQLdb.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
    #     self.db_cur = self.db_conn.cursor()
    #
    # def close_spider(self, spider):
    #     self.db_conn.commit()
    #     self.db_conn.close()
    #
    # def process_item(self, item, spider):
    #     self.insert_db(item)
    #     return item
    #
    # def insert_db(self, item):
    #     values = (
    #         item['name'],
    #         item['url'],
    #         item['password'],
    #         item['save_state'],
    #         item['id']
    #     )
    #     update_sql = """
    #          update book set name = %s,url=%s,password =%s,save_state=%s where id = %s
    #      """
    #     self.db_cur.execute(update_sql, values)

    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', 'wenhao151', 'scrapy_db', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        update_sql = """
            update book set name = %s,url=%s,password =%s,save_state=%s where id = %s
        """
        self.cursor.execute(update_sql, (item['name'], item['url'], item['password'],item['save_state'],item['id']))
        self.conn.commit()
