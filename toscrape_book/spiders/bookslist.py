# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.linkextractors import LinkExtractor
from ..items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'bookslist'
    allowed_domains = ['mebook.cc']
    start_urls = ['http://mebook.cc']

    def parse(self, response):
        for le in response.css('.content'):
            book = BookItem()
            detail_url = le.xpath('./h2/a/@href').extract_first()
            bookName = le.xpath('./h2/a/@title').extract_first()
            print(bookName)
            book['detail_url'] = detail_url
            book['name'] = bookName
            yield book
        le = LinkExtractor(restrict_css='.current+a')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            time.sleep(10)
            yield scrapy.Request(next_url, callback=self.parse)