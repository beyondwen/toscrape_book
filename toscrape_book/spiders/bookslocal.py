# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.linkextractors import LinkExtractor
from ..items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'bookslocal'
    allowed_domains = ['localhost:8086', 'mebook.cc']
    start_urls = ['http://localhost:8086/list']

    detailUrl_var = ''
    dataId_var = ''
    bookName_var = ''

    def parse(self, response):
        try:
            for pb in response.css('.booktr'):
                detailUrl = pb.css('.du::text').extract()[0]
                dataId = pb.css('.bookid::text').extract()[0]
                bookName = pb.css('.bookName::text').extract()[0]
                global detailUrl_var
                global dataId_var
                global bookName_var
                detailUrl_var = detailUrl
                dataId_var = dataId
                bookName_var = bookName
                yield scrapy.Request(detailUrl, callback=self.pares_detail)
            le = LinkExtractor(restrict_xpaths='//*[@id="pageno"]')
            links = le.extract_links(response)
            if links:
                next_url = links[0].url
                yield scrapy.Request(next_url, callback=self.parse)
        except Exception as e:
            print(e)
            with open('失败链接.txt', 'a') as f:
                f.write(detailUrl)
                f.write('\n')
                f.write(dataId)
                f.write('\n')
                f.write(bookName)
                f.write('\n')

    def pares_detail(self, response):
        try:
            global detailUrl_var
            global dataId_var
            global bookName_var
            print(detailUrl_var)
            print(dataId_var)
            print(bookName_var)
            le = LinkExtractor(restrict_css='.downbtn')
            links = le.extract_links(response)
            single_url = links[0].url
            yield scrapy.Request(single_url, callback=self.pares_downloadlink)
        except Exception as e:
            with open('失败链接0.txt', 'a') as f:
                f.write(BooksSpider.detailUrl_var)
                f.write('\n')
                f.write(BooksSpider.dataId_var)
                f.write('\n')
                f.write(BooksSpider.bookName_var)
                f.write('\n')

    def pares_downloadlink(self, response):
        time.sleep(1)
        book = BookItem()
        le = LinkExtractor(restrict_css='.list')
        sel = response.css('.desc>p::text')
        links = le.extract_links(response)
        url = links[0].url
        password = sel.extract()
        password1 = ''.join(password[5].split())
        password2 = password1[12:16]
        book['url'] = url.strip()
        book['password'] = password2
        book['id'] = BooksSpider.dataId_var
        yield book
