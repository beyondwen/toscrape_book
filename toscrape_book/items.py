# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    name = scrapy.Field()  # 书名
    url = scrapy.Field()  # 书名
    password = scrapy.Field()  # 书名
    save_state = scrapy.Field()  # 状态
    id = scrapy.Field()  # id
    # price = scrapy.Field()  # 价格
    # review_rating = scrapy.Field()  # 评价等级，1～5 星
    # review_num = scrapy.Field()  # 评价数量
    # upc = scrapy.Field()  # 产品编码
    # stock = scrapy.Field()  # 库存量
