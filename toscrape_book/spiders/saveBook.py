import json
import time

import scrapy
from ..items import BookItem
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from scrapy.linkextractors import LinkExtractor
from selenium.webdriver.chrome.options import Options


class BooksSpider(scrapy.Spider):
    name = 'save2'
    allowed_domains = ['localhost:8086']
    start_urls = ['http://localhost:8086/list']

    browser = None

    def parse(self, response):
        f = open('D:\\pythonwork\\fullstack\\toscrape_book\\jsonFile.json', 'r')
        cookiessu = f.read()
        cookiessu = json.loads(cookiessu)
        # 进行循环
        for le in response.css('.booktr'):
            book = BookItem()
            # time.sleep(2)
            # 提取链接
            url1 = le.css('.bookUrl::text')
            # 提取密码
            pwd1 = le.css('.pwd::text')
            # id
            bookId1 = le.css('.bookid::text')
            # 书名
            bookname1 = le.css('.bookName::text')

            chrome_options = Options()
            chrome_options.add_argument('headless')
            # chrome_options.add_argument("window-size=1920,1080")
            chrome_options.add_argument('--start-maximized')
            chrome_options.add_argument('log-level=3')
            # browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome Beta\Application\chromedriver.exe')
            self.browser = webdriver.Chrome(chrome_options=chrome_options)
            # 打开浏览器
            # browser = webdriver.Chrome()
            # 抽取具体链接
            url = url1[0].extract()
            # 抽取具体密码
            pwd = pwd1[0].extract()
            bookId = bookId1[0].extract()
            bookname = bookname1[0].extract()
            # url = 'https://pan.baidu.com/s/1_QuWZDoyPmsXNtYsCqqirA'
            # pwd = 'ci7y'

            # 请求目标地址
            self.browser.get(url)
            time.sleep(1)
            # 浏览器最大化
            # browser.maximize_window()
            time.sleep(1)
            if cookiessu != "":
                for cssu in cookiessu:
                    print(cssu)
                    self.browser.add_cookie(cssu)
                time.sleep(1)
            # 获取输入分享密码的输入框
            try:
                input_ = self.browser.find_element(By.CLASS_NAME, "QKKaIE")
                # 输入分享密码
                input_.send_keys(pwd, Keys.ARROW_DOWN)
                # 获取提交按钮
                submit_button = self.browser.find_element(By.CLASS_NAME, "text")
                # 提交
                submit_button.click()
                time.sleep(2)
                # print(getCookie)
                # 保存到网盘
                self.clickSave()
                # 选取保存位置
                self.browser.find_element_by_xpath('//*[@node-path="/我的小书屋"]').click()
                time.sleep(2)
                self.finalSave()
                book['name'] = bookname
                book['url'] = url
                book['password'] = pwd
                book['save_state'] = 1
                book['id'] = bookId
            except:
                book['id'] = bookId
                book['save_state'] = 3
                print('保存失败')
                print('save faile :' + bookname)
            self.browser.close()
            self.browser.quit()
            yield book
        le = LinkExtractor(restrict_css='#weiye')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)

    def clickSave(self):
        try:
            self.browser.find_element_by_css_selector(".zbyDdwb").click()
            self.browser.find_element(By.CLASS_NAME, "x-button-box").find_element_by_xpath('//*[@data-button-id="b1"]').click()
            time.sleep(3)
        except:
            self.browser.find_element(By.CLASS_NAME, "x-button-box").find_element_by_xpath('//*[@data-button-id="b1"]').click()
            time.sleep(3)

    def finalSave(self):
        try:
            self.browser.find_element(By.CLASS_NAME, "dialog-footer").find_element_by_xpath('//*[@data-button-id="b35"]').click()
            time.sleep(3)
        except:
            self.browser.find_element(By.CLASS_NAME, "dialog-footer").find_element_by_xpath('//*[@data-button-id="b13"]').click()
            time.sleep(3)