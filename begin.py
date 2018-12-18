from scrapy import cmdline

# cmdline.execute("scrapy crawl bookstest -o books.csv --nolog".split())
cmdline.execute("scrapy crawl bookslocal".split())
