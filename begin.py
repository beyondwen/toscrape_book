from scrapy import cmdline

# cmdline.execute("scrapy crawl bookstest -o books.csv --nolog".split())
cmdline.execute("scrapy crawl saveBook".split())
cmdline.execute("scrapy crawl saveBook1".split())
cmdline.execute("scrapy crawl saveBook2".split())


