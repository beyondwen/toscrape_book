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


class saveBookPipeline:
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', 'wenhao151', 'scrapy_db', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            update_sql = """
            insert into  book (name,url,password,save_state) value (%s,%s,%s,%s,%s)
            """
            self.cursor.execute(update_sql, (item['name'], item['url'], item['password'], item['save_state']))
            self.conn.commit()

        except Exception as e:
            with open('shibaifilename.txt', 'a') as f:
                f.write(item['name'])
                f.write('\n')

