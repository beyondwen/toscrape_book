# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

from ..items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'books123'
    allowed_domains = ['mebook.cc']
    start_urls = ['http://mebook.cc/']

    def parse(self, response, ):
        for le in response.css('.content'):
            book = BookItem()
            book['name'] = le.xpath('./h2/a/@title').extract_first()
            yield book

        le = LinkExtractor(restrict_css='.current+a')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse)
        # self.parse_book
        # le = LinkExtractor(restrict_css='.content')
        # for link in le.extract_links(response):
        #     yield scrapy.Request(link.url, callback=self.parse_book)
        #
        # le = LinkExtractor(restrict_css='div.pagenavi+a')
        # links = le.extract_links(response)
        # if links:
        #     next_url = links[0].url
        #     yield scrapy.Request(next_url, callback=self.parse)

    # def parse_book(self, response):
    #     book = BookItem()
    #     sel = response.css('.content')
    #     book['name'] = sel.xpath('./h2.title[@*]/text()').extract_first()
    #     # book['price'] = sel.css('p.price_color::text').extract_first()
    #     # book['review_rating'] = sel.css('p.star-rating::attr(class)').re_first('star-rating ([A-Za-z]+)')
    #     # sel = response.css('table.table.table-striped')
    #     # book['upc'] = sel.xpath('(.//tr)[1]/td/text()').extract_first()
    #     # book['stock'] = sel.xpath('(.//tr)[last()-1]/td/text()').re_first('\((\d+) available\)')
    #     # book['review_num'] = sel.xpath('(.//tr)[last()]/td/text()').extract_first()
    #     yield book
#  当list 等于3时 取第1个
#  当list 等于4时 取第2个
