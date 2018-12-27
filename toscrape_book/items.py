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
    savestate = scrapy.Field()  # 状态
    id = scrapy.Field()  # id
    detailurl = scrapy.Field()  # id
    type = scrapy.Field()  # id

