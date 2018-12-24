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
import time


class MySQLPipeline:
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', 'wenhao151', 'scrapy_db', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    # def process_item(self, item, spider):
    #     try:
    #         select_sql = "select * from book_type where b_name = %s"
    #         value = [item['name']]
    #         self.cursor.execute(select_sql, value)
    #         result = self.cursor.fetchone()
    #         if result:
    #             pass
    #         else:
    #             update_sql = """
    #                          insert into book_type (b_name,b_detail_url,b_type) value (%s,%s,%s)
    #                      """
    #             self.cursor.execute(update_sql, ([item['name']],[item['detailurl']],[item['type']]))
    #             self.conn.commit()
    #     except Exception as e:
    #         with open('保存失败的文件.txt', 'a') as f:
    #             f.write(item['name'])
    #             f.write('\n')

    # def process_item(self, item, spider):
    #     try:
    #         update_sql = """
    #                                      update book_type SET b_url = %s,b_password = %s  where id = %s
    #                                  """
    #         self.cursor.execute(update_sql, (item['url'], item['password'], item['id']))
    #         self.conn.commit()
    #     except Exception as e:
    #         with open('保存失败的文件.txt', 'a',encoding="utf-8") as f:
    #             f.write(item['name'])
    #             f.write('\n')

    def process_item(self, item, spider):
        try:
            update_sql = """
                                         update book_type SET b_save_state = %s  where id = %s
                                     """
            self.cursor.execute(update_sql, (item['savestate'], item['id']))
            self.conn.commit()
        except Exception as e:
            with open('保存失败的文件.txt', 'a', encoding="utf-8") as f:
                f.write(item['name'])
                f.write('\n')
