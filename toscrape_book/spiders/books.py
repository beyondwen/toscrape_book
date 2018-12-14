# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor

from ..items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['mebook.cc']
    start_urls = ['http://mebook.cc/']

    def parse(self, response):
        try:
            for le in response.css('.content'):
                self.detail_url = le.xpath('./h2/a/@href').extract_first()
                yield scrapy.Request(self.detail_url, callback=self.pares_detail)
            le = LinkExtractor(restrict_css='.current+a')
            links = le.extract_links(response)
            if links:
                self.next_url = links[0].url
                yield scrapy.Request(self.next_url, callback=self.parse)
        except Exception as e:
            with open('shibaifileurl.txt', 'a') as f:
                f.write(self.next_url)
                f.write('\n')

    def pares_detail(self, response):
        try:
            le = LinkExtractor(restrict_css='.downbtn')
            links = le.extract_links(response)
            self.single_url = links[0].url
            yield scrapy.Request(self.single_url, callback=self.pares_downloadlink)
        except Exception as e:
            with open('shibaifile.txt', 'a') as f:
                f.write(self.single_url)
                f.write('\n')

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
        book['save_state'] = '0'
        yield book
