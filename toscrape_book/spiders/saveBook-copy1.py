import scrapy
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ..items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'bookstestcopy1'
    allowed_domains = ['192.168.1.114:8086']
    start_urls = ['http://192.168.1.114:8086/list']

    def parse(self, response):
        for le in response.css('.booktr'):
            url1 = le.css('.bookUrl::text')
            pwd1 = le.css('.pwd::text')
            # book['url'] = url1.extract()
            # book['password'] = pwd1.extract()
            try:
                # browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome Beta\Application\chromedriver.exe')
                browser = webdriver.Chrome()

                # browser.set_window_size(1920,1080)
                url = url1[0].extract()
                pwd = pwd1[0].extract()
                # url = 'https://pan.baidu.com/s/1K0Hv7kxR7k4VHD9XyANW5Q'
                # pwd = 'stwh'
                # 你的百度去帐号，保存到你的网盘肯定需要你自己的帐号密码
                user_name = 'beyond文豪'
                password = 'wenhao176'
                # 请求目标地址
                browser.get(url)

                time.sleep(10)
                browser.maximize_window()
                time.sleep(10)

                # 获取输入分享密码的输入框
                input_ = browser.find_element(By.CLASS_NAME, "QKKaIE")
                # 输入分享密码
                input_.send_keys(pwd, Keys.ARROW_DOWN)
                # 获取提交按钮
                submit_button = browser.find_element(By.CLASS_NAME, "text")
                # 提交
                submit_button.click()

                # 休息一下加载新页面
                time.sleep(3)

                # 登陆自己的百度云
                browser.find_element(By.CLASS_NAME, "CDaavKb").find_element_by_xpath(
                    '//*[@node-type="header-login-btn"]').click()
                time.sleep(4)
                browser.find_element(By.CLASS_NAME, "tang-pass-footerBarULogin").click()

                # 输入用户名密码
                time.sleep(5)
                user_name_input = browser.find_element(By.ID, "TANGRAM__PSP_10__userName")
                pwd_input = browser.find_element(By.ID, "TANGRAM__PSP_10__password")
                user_name_input.send_keys(user_name, Keys.ARROW_DOWN)
                pwd_input.send_keys(password, Keys.ARROW_DOWN)

                # 点击登陆
                browser.find_element(By.ID, "TANGRAM__PSP_10__submit").click()
                time.sleep(6)

                # 保存到网盘
                browser.find_element_by_css_selector(".zbyDdwb").click()
                save_pan = browser.find_element(By.CLASS_NAME, "x-button-box").find_element_by_xpath(
                    '//*[@data-button-id="b1"]')
                save_pan.click()
                time.sleep(6)

                # 选取保存位置
                pdf_book = browser.find_element_by_xpath('//*[@node-path="/我的小书屋"]')
                pdf_book.click()
                time.sleep(6)

                browser.find_element(By.CLASS_NAME, "dialog-footer").find_element_by_xpath(
                    '//*[@data-button-id="b35"]').click()
                browser.close()
                # # 保存到网盘
                # browser.find_element_by_css_selector(".zbyDdwb").click()
                # # save_pan = browser.find_element(By.CLASS_NAME, "x-button-box").find_element_by_xpath('//*[@data-button-id="b1"]')
                # # save_pan.click()
                # time.sleep(2)
                #
                # # 登陆自己的百度云
                # browser.find_element(By.CLASS_NAME, "CDaavKb").find_element_by_xpath(
                #     '//*[@node-type="header-login-btn"]').click()
                # # login_btn.click()  # 跳转登陆界面
                # time.sleep(1)
                # browser.find_element(By.CLASS_NAME, "tang-pass-footerBarULogin").click()
                #
                #
                # # 输入用户名密码
                # time.sleep(1)
                # user_name_input = browser.find_element(By.ID, "TANGRAM__PSP_10__userName")
                # pwd_input = browser.find_element(By.ID, "TANGRAM__PSP_10__password")
                # user_name_input.send_keys(user_name, Keys.ARROW_DOWN)
                # pwd_input.send_keys(password, Keys.ARROW_DOWN)
                #
                # # 点击登陆
                # real_login_btn = browser.find_element(By.ID, "TANGRAM__PSP_10__submit")
                # real_login_btn.click()
                # time.sleep(2)
                #
                # save_pan = browser.find_element(By.CLASS_NAME, "x-button-box").find_element_by_xpath('//*[@data-button-id="b1"]')
                # save_pan.click()
                #
                # # 选取保存位置
                # pdf_book = browser.find_element_by_xpath('//*[@node-path="/我的小书屋"]')
                # pdf_book.click()
                #
                # ok_click = browser.find_element(By.CLASS_NAME, "dialog-footer").find_element_by_xpath(
                #     '//*[@data-button-id="b15"]')
                # ok_click.click()

                # browser.close()
            except:
                print('save faile :'+ url)

            # yield book
        # book = BookItem()
        # for le in response.css('.booktr'):
        #     url1 = le.css('.bookUrl::text')
        #     pwd1 = le.css('.pwd::text')
        #     book['url'] = url1.extract()
        #     book['password'] = pwd1.extract()

        # yield scrapy.Request(url, callback=self.save)
        # le = LinkExtractor(restrict_css='.current+a')
        # links = le.extract_links(response)
        # if links:
        #     next_url = links[0].url
        #     yield scrapy.Request(next_url, callback=self.parse)

    # def save(self):
    #     try:
    #         browser = webdriver.Chrome("D:\\pythonwork\\chromedriver.exe")
    #         url = "https://pan.baidu.com/s/1NhowUs5LKTHWE8zpx_QZcA"
    #         pwd = "k5ru"
    #         # 你的百度去帐号，保存到你的网盘肯定需要你自己的帐号密码
    #         user_name = '百度云帐号'
    #         password = '百度云密码'
    #         # 请求目标地址
    #         browser.get(url)
    #         # 获取输入分享密码的输入框
    #         input_ = browser.find_element(By.CLASS_NAME, "QKKaIE")
    #         # 输入分享密码
    #         input_.send_keys(pwd, Keys.ARROW_DOWN)
    #         # 获取提交按钮
    #         submit_button = browser.find_element(By.CLASS_NAME, "text")
    #         # 提交
    #         submit_button.click()
    #
    #         # 休息一下加载新页面
    #         time.sleep(2)
    #
    #         # 登陆自己的百度云
    #         login_btn = browser.find_element(By.CLASS_NAME, "CDaavKb").find_element_by_xpath(
    #             '//*[@node-type="header-login-btn"]')
    #         login_btn.click()  # 跳转登陆界面
    #         time.sleep(1)
    #         name_login = browser.find_element(By.CLASS_NAME, "tang-pass-footerBarULogin")
    #         name_login.click()  # 使用账号密码登陆
    #
    #         # 输入用户名密码
    #         time.sleep(1)
    #         user_name_input = browser.find_element(By.ID, "TANGRAM__PSP_10__userName")
    #         pwd_input = browser.find_element(By.ID, "TANGRAM__PSP_10__password")
    #         user_name_input.send_keys(user_name, Keys.ARROW_DOWN)
    #         pwd_input.send_keys(password, Keys.ARROW_DOWN)
    #
    #         # 点击登陆
    #         real_login_btn = browser.find_element(By.ID, "TANGRAM__PSP_10__submit")
    #         real_login_btn.click()
    #         time.sleep(2)
    #
    #         # 保存到网盘
    #         save_pan = browser.find_element(By.CLASS_NAME, "x-button-box").find_element_by_xpath(
    #             '//*[@data-button-id="b1"]')
    #         save_pan.click()
    #         time.sleep(2)
    #
    #         # 选取保存位置
    #         pdf_book = browser.find_element_by_xpath('//*[@node-path="/pdfbook"]')
    #         pdf_book.click()
    #
    #         ok_click = browser.find_element(By.CLASS_NAME, "dialog-footer").find_element_by_xpath(
    #             '//*[@data-button-id="b15"]')
    #         ok_click.click()
    #
    #         # browser.close()
    #     except:
    #         print
    #         'save faile ', url
