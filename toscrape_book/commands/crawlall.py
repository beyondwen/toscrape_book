from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from toscrape_book.spiders.saveBook import BooksSpider
from toscrape_book.spiders.saveBook1 import BooksSpider1
from toscrape_book.spiders.saveBook2 import BooksSpider2

process = CrawlerProcess(get_project_settings())
process.crawl(BooksSpider)
process.crawl(BooksSpider1)
process.crawl(BooksSpider2)

process.start()
