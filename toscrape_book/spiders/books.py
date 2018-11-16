# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

from ..items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['mebook.cc']
    start_urls = ['http://mebook.cc/']

    def parse(self, response):
        for le in response.css('.content'):
            url = le.xpath('./h2/a/@href').extract_first()
            yield scrapy.Request(url, callback=self.pares_detail)
        le = LinkExtractor(restrict_css='.current+a')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse)

    def pares_detail(self, response):
        le = LinkExtractor(restrict_css='.downbtn')
        links = le.extract_links(response)
        url = links[0].url
        yield scrapy.Request(url, callback=self.pares_downloadlink)

    def pares_downloadlink(self, response):
        book = BookItem()
        le = LinkExtractor(restrict_css='.list')
        sel = response.css('.desc>p::text')
        sel2 = response.css('h1 a::text')
        links = le.extract_links(response)
        url = links[0].url
        password = sel.extract()
        password1 = ''.join(password[5].split())
        password2 = password1[12:16]
        name = sel2.extract()
        book['name'] = name[0].strip()
        book['url'] = url.strip()
        book['password'] = password2
        yield book
